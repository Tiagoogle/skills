# Modelo de dados v1.1 — registro de manifestação

A v1.0 da especificação original tinha três falhas estruturais que este modelo corrige:

1. **Consentimento único.** O campo `reporter_consent` misturava autorização para registrar com autorização para revelar identidade, embora o próprio documento (seção 10) diga que são coisas distintas. Agora são três campos.
2. **Não dava para medir o que o plano de riscos exige.** O plano pede comparação por idioma, formato de entrada e canal (R02, R04, §6.3), mas o modelo não tinha `language`, `input_modality` nem `recorded_by`. Sem esses campos, a auditoria de vieses fica impossível na prática.
3. **O encerramento não deixava rastro.** O plano exige ação, evidência, comunicação e contestação para encerrar (§6.4), mas o modelo não tinha onde guardar essas informações. Agora há o bloco `closure` e o histórico de classificação.

Chaves em inglês e valores em português foram mantidos por compatibilidade com a v1.0. O exemplo completo e válido está em `assets/registro-exemplo.json`. O validador está em `scripts/validar_registro.py`.

## Campos

| Campo | Tipo / domínio | Por que existe |
|---|---|---|
| `schema_version` | `"1.1"` | Migração controlada. |
| `id` | uuid | Identificador estável. |
| `received_at` | datetime ISO 8601 com fuso | Início de todos os prazos. |
| `channel` | `reuniao, campo, presencial, telefone, email, formulario, mensagem, audio, outro` | Paridade entre canais (R01). |
| `input_modality` | `escrito, oral_transcrito_humano, oral_transcrito_automatico, oral_registrado_por_terceiro, audio_original` | Viés de credibilidade e de transcrição automática (R04, R20). |
| `language` | código BCP 47 ou `variante_local:<nome>` | Viés linguístico (R02). |
| `recorded_by` | `proprio_manifestante, agente_de_campo, ouvidoria, terceiro, outro` | Mostra quem filtrou o relato. |
| `manifestation_type` | `reclamacao, duvida, pedido, sugestao, denuncia, elogio, outro` | Define fluxo e nível de sigilo. |
| `scope` | `individual, coletiva, indeterminada` | Alcance coletivo é critério de prioridade. |
| `territorial_units` | lista de ids de uma lista controlada | Substitui o texto livre `community`. Os limites de "comunidade" são disputados; use unidades territoriais definidas junto com as próprias comunidades e aceite mais de uma. |
| `location` | texto ou null | Só com a precisão necessária. Coordenadas exatas em território de conflito aumentam o risco de exposição. |
| `consent.record` | `granted, limited, refused, unknown` | Autorização para registrar. |
| `consent.identity_disclosure` | `granted, refused, not_requested` | Autorização para revelar a identidade a outras áreas. |
| `consent.contact_back` | `granted, refused, not_requested` | Autorização para retornar o contato. |
| `consent.collected_by`, `consent.collected_at` | texto, datetime | Rastreabilidade. |
| `legal_basis` | `consentimento, obrigacao_legal, legitimo_interesse, protecao_da_vida, exercicio_regular_de_direitos, a_definir_pelo_encarregado` | Ver a nota sobre LGPD abaixo. |
| `access_level` | `padrao, restrito, confidencial` | Denúncias e identidades protegidas não ficam no nível padrão. |
| `retention_until` | data | Retenção definida (LGPD, art. 6º, princípio da necessidade). |
| `reporter_identity` | referência protegida ou null | Nunca o nome em claro no registro analítico. |
| `original_statement` | texto não vazio e **imutável** | A síntese nunca substitui o relato. |
| `normalized_summary` | texto | Resumo neutro, sem juízo sobre veracidade. |
| `summary_confirmed_by_reporter` | `sim, nao, pendente, nao_aplicavel` | O plano (§6.2) exige devolver o entendimento à pessoa antes de classificar. |
| `topics` | lista: `agua, poeira, ruido, vibracao, transito, emprego, compras_locais, terras, reassentamento, patrimonio_cultural, saude, seguranca, meio_ambiente, barragem, compensacao, beneficios_comunitarios, conduta_empregados_contratadas, comunicacao, outro` | Foram incluídos `vibracao` (rachaduras por detonação, queixa frequente em mineração) e `barragem`. |
| `impact_claimed`, `requested_action` | texto ou null | O que a pessoa diz e o que pede. |
| `evidence` | lista: `documento, foto, audio, video, testemunho, laudo, nenhuma` | Testemunho é evidência (R04). |
| `evidence_status` | `nao_verificada, em_investigacao, verificada, sem_informacao_suficiente` | **Não existe** o estado "improcedente". Não encontrar evidência não prova que não houve dano. |
| `urgency_suggestion` | `imediata, alta, media, baixa, indeterminada` | Sugestão para revisão humana. |
| `urgency_rationale` | texto obrigatório | Prioridade sem justificativa não pode ser auditada. |
| `risk_flags` | lista: `saude, seguranca, direitos_humanos, barragem, terras, reassentamento, povos_indigenas_tradicionais, crianca_adolescente, violencia_ameaca, corrupcao, discriminacao, retaliacao, dano_ambiental_grave, crise_publica, patrimonio_cultural, autolesao` | Aciona escalonamento e revisão humana. |
| `screening` | `{lexical_level, lexical_flags, llm_flags, injection_suspected, lexical_coverage}` | Guarda o resultado das duas camadas de triagem, para medir onde cada uma falha. |
| `escalation` | `{required, reason, escalated_to, escalated_at, independent_channel}` | Escalonamento rastreável. `independent_channel` marca os casos que não podem ficar só com a equipe envolvida. |
| `status` | `novo, em_validacao, em_tratamento, aguardando_retorno, resolvido, encerrado, reaberto` | Foi incluído `reaberto`: a taxa de reabertura é indicador central. |
| `owner`, `due_date`, `due_date_approved_by` | texto, data, texto | Prazo sem aprovação não vai para a comunidade. |
| `source_references` | lista de `{doc_id, version, valid_until, excerpt}` | Sem documento vencido (R14). |
| `classification_history` | lista de `{at, actor, actor_type: agente/humano, topics, urgency, risk_flags, reason}` | Uma correção humana acrescenta uma entrada e não apaga a sugestão original. Esse histórico permite medir a taxa de correção e a aceitação automática (R06). |
| `human_review` | `required, completed, not_required` | |
| `closure` | null ou `{action_taken, action_evidence, communication_sent_at, contestation_channel_informed, affected_party_feedback, closed_by, closed_at}` | O encerramento precisa ser defensável. `affected_party_feedback` ∈ `satisfeito, parcialmente_satisfeito, insatisfeito, sem_retorno, nao_aplicavel`. |
| `reopen_count` | inteiro | Mostra encerramento artificial (R11). |
| `audit_log` | lista de `{at, actor, action, details}` | Só acrescenta; nunca edita. |

## Regras que o validador aplica

Erros (E) bloqueiam o registro. Avisos (W) exigem atenção humana.

| Código | Regra |
|---|---|
| E01 | Campos obrigatórios presentes, incluindo os três consentimentos. |
| E02 | Valores dentro do domínio. |
| E03 | `original_statement` não vazio. |
| E04 | Com sinal de risco, suspeita de injeção ou baixa cobertura léxica, `human_review` não pode ser `not_required`. |
| E05 | Urgência `imediata` exige escalonamento. Todo escalonamento precisa de motivo. Toda urgência precisa de justificativa. |
| E06 | Caso com risco ou escalonado só é encerrado depois de revisão humana concluída. |
| E07 | Encerramento exige ação, evidência, data da comunicação, canal de contestação informado e responsável humano. O agente não encerra casos. |
| E08 | `sem_retorno` não encerra caso com risco: falta de resposta não é concordância. |
| E09 | Não guardar identidade quando o registro foi recusado. |
| E10 | Proibido registrar chaves de atributo sensível ou perfilamento de pessoa (etnia, religião, orientação política, diagnóstico, "nível de influência", "nível de ameaça" etc.). |
| E11 | Todo prazo precisa de responsável. |
| E12 | O histórico de classificação precisa ter atores tipados. |
| E13 | A trilha de auditoria não pode estar vazia, e cada evento precisa estar completo. |
| E15 | Nenhuma fonte citada pode estar vencida. |
| E16 | **Regra da união:** se a pré-triagem léxica sinalizar risco, o registro não pode ficar sem `risk_flags`. Nível crítico exige escalonamento. Suspeita de injeção precisa ser registrada. Só uma pessoa pode descartar um sinal, e com justificativa no `audit_log`. |
| E18 | A base legal `consentimento` exige consentimento de registro concedido. |
| W05, W08, W09, W11, W12, W14, W15, W16, W17, W18 | Canal independente em casos de retaliação, violência ou corrupção; encerramento sem retorno; acesso de identidade e denúncia; prazo não aprovado; correção sem motivo; linguagem que culpa a pessoa; fonte sem validade; divergência de nível; transcrição automática não confirmada; base legal e retenção pendentes. |

## Nota sobre LGPD: por que consentimento não é a base padrão

O consentimento, pela LGPD (art. 5º, XII), precisa ser "livre, informado e inequívoco". Onde a comunidade depende economicamente da operação, a liberdade desse consentimento é questionável. Ele também pode ser revogado a qualquer momento, e um mecanismo de reclamação cujo registro some quando a pessoa revoga a autorização perde a trilha de auditoria. Por isso, a base legal do tratamento, isto é, a justificativa jurídica para usar o dado, deve ser definida pelo encarregado de dados. Os candidatos usuais são o legítimo interesse (art. 7º, IX, com registro das operações, art. 37), obrigações legais ou regulatórias (art. 7º, II), a proteção da vida (art. 7º, VII) e, para dados sensíveis, as hipóteses do art. 11. Independentemente da base escolhida, peça à pessoa autorização específica para revelar a identidade e para ser contatada: aí o consentimento continua sendo a ferramenta certa.

Exemplo: uma reclamação sobre poeira registrada como `legitimo_interesse` continua no histórico mesmo que a pessoa depois peça para não ser mais contatada. O que muda é `contact_back: refused`, e o caso segue sem retorno direto a ela.

## Painéis e reidentificação

Agregar os dados não basta para anonimizá-los. Em uma localidade de 40 famílias, "3 reclamações de retaliação na comunidade X em setembro" pode identificar quem reclamou. Use supressão de células pequenas: não mostre contagens abaixo de um limiar definido pelo comitê (5 é um ponto de partida usual em estatística oficial, mas é uma convenção, não uma exigência legal). Agregue também por períodos ou áreas maiores quando necessário.
