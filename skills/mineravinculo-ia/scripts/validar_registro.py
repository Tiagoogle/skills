#!/usr/bin/env python3
"""
Valida registros de manifestação contra o modelo de dados v1.1 e as regras de
salvaguarda do MineraVínculo IA (ver references/modelo-de-dados.md).

O validador não julga o mérito do relato. Ele verifica se o registro respeita
as travas que não podem depender de boa vontade: texto original preservado,
revisão humana onde há risco, escalonamento coerente com a pré-triagem,
encerramento com evidência, consentimentos separados, ausência de atributos
sensíveis inferidos e documentos vigentes.

Uso:
  python validar_registro.py registro.json
  python validar_registro.py lote.json          # lista de registros
  python validar_registro.py registro.json --hoje 2026-09-25

Saída: JSON com erros (bloqueiam) e avisos (exigem atenção). Código de saída
1 se houver qualquer erro. Só usa a biblioteca padrão.
"""

import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from triagem import triar  # noqa: E402

ENUMS = {
    "channel": {"reuniao", "campo", "presencial", "telefone", "email", "formulario", "mensagem", "audio", "outro"},
    "input_modality": {"escrito", "oral_transcrito_humano", "oral_transcrito_automatico",
                       "oral_registrado_por_terceiro", "audio_original"},
    "recorded_by": {"proprio_manifestante", "agente_de_campo", "ouvidoria", "terceiro", "outro"},
    "manifestation_type": {"reclamacao", "duvida", "pedido", "sugestao", "denuncia", "elogio", "outro"},
    "scope": {"individual", "coletiva", "indeterminada"},
    "legal_basis": {"consentimento", "obrigacao_legal", "legitimo_interesse", "protecao_da_vida",
                    "exercicio_regular_de_direitos", "a_definir_pelo_encarregado"},
    "access_level": {"padrao", "restrito", "confidencial"},
    "summary_confirmed_by_reporter": {"sim", "nao", "pendente", "nao_aplicavel"},
    "evidence_status": {"nao_verificada", "em_investigacao", "verificada", "sem_informacao_suficiente"},
    "urgency_suggestion": {"imediata", "alta", "media", "baixa", "indeterminada"},
    "status": {"novo", "em_validacao", "em_tratamento", "aguardando_retorno", "resolvido", "encerrado", "reaberto"},
    "human_review": {"required", "completed", "not_required"},
}
ENUMS_LISTA = {
    "topics": {"agua", "poeira", "ruido", "vibracao", "transito", "emprego", "compras_locais", "terras",
               "reassentamento", "patrimonio_cultural", "saude", "seguranca", "meio_ambiente", "barragem",
               "compensacao", "beneficios_comunitarios", "conduta_empregados_contratadas",
               "comunicacao", "outro"},
    "evidence": {"documento", "foto", "audio", "video", "testemunho", "laudo", "nenhuma"},
    "risk_flags": {"saude", "seguranca", "direitos_humanos", "barragem", "terras", "reassentamento",
                   "povos_indigenas_tradicionais", "crianca_adolescente", "violencia_ameaca", "corrupcao",
                   "discriminacao", "retaliacao", "dano_ambiental_grave", "crise_publica",
                   "patrimonio_cultural", "autolesao"},
}
CONSENT_ENUMS = {
    "record": {"granted", "limited", "refused", "unknown"},
    "identity_disclosure": {"granted", "refused", "not_requested"},
    "contact_back": {"granted", "refused", "not_requested"},
}
OBRIGATORIOS = [
    "schema_version", "id", "received_at", "channel", "input_modality", "language", "recorded_by",
    "manifestation_type", "scope", "territorial_units", "consent", "legal_basis", "access_level",
    "original_statement", "normalized_summary", "topics", "urgency_suggestion", "urgency_rationale",
    "risk_flags", "screening", "escalation", "status", "human_review", "classification_history",
    "audit_log",
]
# Chaves que indicam registro ou inferência de atributo sensível ou perfilamento
# de pessoas. Necessidade de acessibilidade autodeclarada é permitida à parte.
CHAVES_PROIBIDAS = {
    "etnia", "raca", "cor", "religiao", "orientacao_sexual", "identidade_de_genero",
    "orientacao_politica", "filiacao_partidaria", "diagnostico", "condicao_de_saude",
    "vulnerabilidade_individual", "score_de_influencia", "nivel_de_influencia",
    "lideranca_influente", "nivel_de_ameaca", "perfil_de_risco_pessoa", "grau_de_hostilidade",
}
ATORES_AUTOMATICOS = {"agente", "ia", "mineravinculo", "mineravinculo_ia", "sistema", "bot"}
PALAVRAS_CULPABILIZANTES = ("improcedente", "infundad", "mentira", "falso", "falsa", "exagero", "oportunis")


class Relatorio:
    def __init__(self, rid):
        self.rid = rid
        self.erros = []
        self.avisos = []

    def erro(self, codigo, campo, msg):
        self.erros.append({"codigo": codigo, "campo": campo, "mensagem": msg})

    def aviso(self, codigo, campo, msg):
        self.avisos.append({"codigo": codigo, "campo": campo, "mensagem": msg})

    def como_dict(self):
        return {"id": self.rid, "valido": not self.erros, "erros": self.erros, "avisos": self.avisos}


def _data(valor):
    if not valor or not isinstance(valor, str):
        return None
    try:
        return dt.date.fromisoformat(valor[:10])
    except ValueError:
        return None


def _chaves_recursivas(obj, prefixo=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            caminho = f"{prefixo}.{k}" if prefixo else k
            yield k, caminho
            yield from _chaves_recursivas(v, caminho)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _chaves_recursivas(v, f"{prefixo}[{i}]")


def validar(reg, hoje):
    r = Relatorio(reg.get("id") if isinstance(reg, dict) else None)
    if not isinstance(reg, dict):
        r.erro("E00", "", "Registro deve ser um objeto JSON.")
        return r

    # E01 campos obrigatórios
    for campo in OBRIGATORIOS:
        if campo not in reg:
            r.erro("E01", campo, "Campo obrigatório ausente.")

    # E02 domínios
    for campo, dominio in ENUMS.items():
        v = reg.get(campo)
        if v is not None and v not in dominio:
            r.erro("E02", campo, f"Valor '{v}' fora do domínio {sorted(dominio)}.")
    for campo, dominio in ENUMS_LISTA.items():
        v = reg.get(campo)
        if v is None:
            continue
        if not isinstance(v, list):
            r.erro("E02", campo, "Deve ser uma lista.")
            continue
        for item in v:
            if item not in dominio:
                r.erro("E02", campo, f"Valor '{item}' fora do domínio.")
    consent = reg.get("consent") or {}
    if not isinstance(consent, dict):
        r.erro("E02", "consent", "Deve ser um objeto com consentimentos separados.")
        consent = {}
    for campo, dominio in CONSENT_ENUMS.items():
        v = consent.get(campo)
        if v is None:
            r.erro("E01", f"consent.{campo}", "Consentimento ausente. Registro, identidade e retorno são autorizações distintas.")
        elif v not in dominio:
            r.erro("E02", f"consent.{campo}", f"Valor '{v}' fora do domínio {sorted(dominio)}.")

    # E03 texto original preservado
    original = reg.get("original_statement")
    if not isinstance(original, str) or not original.strip():
        r.erro("E03", "original_statement", "Texto original vazio. A síntese nunca substitui o relato.")
        original = ""

    risk_flags = reg.get("risk_flags") or []
    screening = reg.get("screening") or {}
    escalation = reg.get("escalation") or {}
    status = reg.get("status")
    human_review = reg.get("human_review")

    # E16 coerência com a pré-triagem (regra da união: qualquer camada que sinalize, escala)
    tri = triar(original)
    if tri["nivel"] != "nenhum" and not risk_flags:
        cats = ", ".join(s["categoria"] for s in tri["sinais"])
        r.erro("E16", "risk_flags", f"Pré-triagem sinaliza [{cats}] e o registro não tem risk_flags. "
                                    "Só uma pessoa pode descartar um sinal, com justificativa no audit_log.")
    if tri["nivel"] == "critico" and not escalation.get("required"):
        r.erro("E16", "escalation.required", "Pré-triagem em nível crítico exige escalonamento.")
    if screening.get("lexical_level") and screening.get("lexical_level") != tri["nivel"]:
        r.aviso("W16", "screening.lexical_level",
                f"Nível gravado '{screening.get('lexical_level')}' difere do recalculado '{tri['nivel']}'.")
    if tri["suspeita_injecao"] and not screening.get("injection_suspected"):
        r.erro("E16", "screening.injection_suspected", "Texto contém padrão de injeção de instruções não registrado.")

    # Risco conta se QUALQUER camada o indicar: registro ou pré-triagem.
    ha_risco = bool(risk_flags) or tri["nivel"] != "nenhum"

    # E04 revisão humana onde há risco
    precisa_revisao = ha_risco or tri["revisao_humana_obrigatoria"] or screening.get("injection_suspected")
    if precisa_revisao and human_review == "not_required":
        r.erro("E04", "human_review", "Há sinal de risco, injeção ou baixa cobertura léxica: revisão humana não pode ser dispensada.")

    # E05 escalonamento coerente
    if reg.get("urgency_suggestion") == "imediata" and not escalation.get("required"):
        r.erro("E05", "escalation.required", "Urgência imediata exige escalonamento.")
    if escalation.get("required") and not escalation.get("reason"):
        r.erro("E05", "escalation.reason", "Escalonamento sem motivo registrado.")
    if not reg.get("urgency_rationale"):
        r.erro("E05", "urgency_rationale", "Urgência sugerida sem justificativa explícita.")
    if set(risk_flags) & {"retaliacao", "violencia_ameaca", "corrupcao"} and not escalation.get("independent_channel"):
        r.aviso("W05", "escalation.independent_channel",
                "Casos de retaliação, violência ou corrupção devem poder seguir para instância independente.")

    # E06/E07/E08 encerramento
    if status in ("resolvido", "encerrado"):
        closure = reg.get("closure") or {}
        for campo in ("action_taken", "action_evidence", "communication_sent_at", "closed_by", "closed_at"):
            if not closure.get(campo):
                r.erro("E07", f"closure.{campo}", "Encerramento exige ação, evidência, comunicação e responsável humano.")
        if closure.get("contestation_channel_informed") is not True:
            r.erro("E07", "closure.contestation_channel_informed", "A pessoa precisa ter sido informada de como contestar.")
        if str(closure.get("closed_by", "")).strip().lower() in ATORES_AUTOMATICOS:
            r.erro("E07", "closure.closed_by", "O agente não pode encerrar casos.")
        if (escalation.get("required") or ha_risco) and human_review != "completed":
            r.erro("E06", "human_review", "Caso com risco ou escalonado não pode ser encerrado sem revisão humana concluída.")
        if closure.get("affected_party_feedback") == "sem_retorno":
            if ha_risco:
                r.erro("E08", "closure.affected_party_feedback",
                       "Ausência de retorno não é concordância: caso com risco não pode ser encerrado assim.")
            else:
                r.aviso("W08", "closure.affected_party_feedback", "Encerramento sem retorno da pessoa: registrar tentativa de contato.")

    # E09 identidade e consentimento
    identidade = reg.get("reporter_identity")
    if identidade and consent.get("record") == "refused":
        r.erro("E09", "reporter_identity", "Identidade registrada apesar de recusa de registro.")
    if identidade and consent.get("identity_disclosure") != "granted" and reg.get("access_level") == "padrao":
        r.aviso("W09", "access_level", "Identidade sem autorização de divulgação deve ter acesso restrito ou confidencial.")
    if reg.get("manifestation_type") == "denuncia" and reg.get("access_level") == "padrao":
        r.aviso("W09", "access_level", "Denúncia com nível de acesso padrão: avaliar restrição.")

    # E10 atributos sensíveis e perfilamento
    for chave, caminho in _chaves_recursivas(reg):
        if str(chave).lower() in CHAVES_PROIBIDAS:
            r.erro("E10", caminho, "Atributo sensível ou perfilamento de pessoa não pode ser registrado nem inferido.")

    # E11 prazos
    if reg.get("due_date") and not reg.get("owner"):
        r.erro("E11", "owner", "Prazo sem responsável.")
    if reg.get("due_date") and not reg.get("due_date_approved_by"):
        r.aviso("W11", "due_date_approved_by", "Prazo sem aprovação: não pode ser comunicado à comunidade.")

    # E12 histórico de classificação
    hist = reg.get("classification_history") or []
    if not hist:
        r.aviso("W12", "classification_history", "Sem histórico: a sugestão original do agente precisa ser preservada.")
    else:
        for i, h in enumerate(hist):
            if h.get("actor_type") not in ("agente", "humano"):
                r.erro("E12", f"classification_history[{i}].actor_type", "actor_type deve ser 'agente' ou 'humano'.")
            if h.get("actor_type") == "humano" and not h.get("reason"):
                r.aviso("W12", f"classification_history[{i}].reason", "Correção humana sem motivo registrado.")

    # E13 trilha de auditoria
    log = reg.get("audit_log") or []
    if not log:
        r.erro("E13", "audit_log", "Trilha de auditoria vazia.")
    for i, ev in enumerate(log):
        for campo in ("at", "actor", "action"):
            if not ev.get(campo):
                r.erro("E13", f"audit_log[{i}].{campo}", "Evento de auditoria incompleto.")

    # W14 linguagem culpabilizante
    resumo = str(reg.get("normalized_summary", "")).lower()
    if any(p in resumo for p in PALAVRAS_CULPABILIZANTES):
        r.aviso("W14", "normalized_summary", "Resumo com linguagem que julga o relato. Use estados verificáveis.")

    # E15 fontes vigentes
    for i, fonte in enumerate(reg.get("source_references") or []):
        if not fonte.get("doc_id") or not fonte.get("version"):
            r.erro("E15", f"source_references[{i}]", "Fonte sem identificador ou versão.")
        validade = _data(fonte.get("valid_until"))
        if validade and validade < hoje:
            r.erro("E15", f"source_references[{i}].valid_until", "Documento vencido não pode sustentar resposta.")
        elif not fonte.get("valid_until"):
            r.aviso("W15", f"source_references[{i}].valid_until", "Fonte sem data de validade.")

    # W17 transcrição automática
    if reg.get("input_modality") == "oral_transcrito_automatico" and reg.get("summary_confirmed_by_reporter") != "sim":
        r.aviso("W17", "summary_confirmed_by_reporter",
                "Transcrição automática sem confirmação da pessoa: erro de ASR pode apagar sinais de risco.")
    if tri["cobertura_lexica"] == "idioma_incerto":
        r.aviso("W17", "language", "Possível outro idioma ou variante: exigir tradução ou mediação humana.")

    # E18 base legal
    if reg.get("legal_basis") == "consentimento" and consent.get("record") != "granted":
        r.erro("E18", "legal_basis", "Base legal 'consentimento' sem consentimento de registro concedido.")
    if reg.get("legal_basis") == "a_definir_pelo_encarregado":
        r.aviso("W18", "legal_basis", "Base legal pendente de definição pelo encarregado (LGPD, arts. 7º e 11).")
    if not reg.get("retention_until"):
        r.aviso("W18", "retention_until", "Prazo de retenção não definido.")

    return r


def main():
    parser = argparse.ArgumentParser(description="Valida registros de manifestação (modelo v1.1).")
    parser.add_argument("arquivo", help="JSON com um registro ou uma lista de registros.")
    parser.add_argument("--hoje", help="Data de referência AAAA-MM-DD para validade de documentos.")
    args = parser.parse_args()

    hoje = dt.date.fromisoformat(args.hoje) if args.hoje else dt.date.today()
    with open(args.arquivo, encoding="utf-8") as f:
        dados = json.load(f)
    registros = dados if isinstance(dados, list) else [dados]
    resultados = [validar(reg, hoje).como_dict() for reg in registros]
    saida = {
        "total": len(resultados),
        "validos": sum(1 for x in resultados if x["valido"]),
        "resultados": resultados,
    }
    print(json.dumps(saida, ensure_ascii=False, indent=2))
    sys.exit(0 if all(x["valido"] for x in resultados) else 1)


if __name__ == "__main__":
    main()
