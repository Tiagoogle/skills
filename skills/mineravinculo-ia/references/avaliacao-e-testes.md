# Avaliação, testes e indicadores

## Sumário
1. Quanto teste é preciso para afirmar um recall
2. Composição do conjunto de testes
3. Paridade entre grupos
4. Modo sombra e linha de base
5. Indicadores pareados
6. Regressão a cada mudança de modelo

---

## 1. Quanto teste é preciso para afirmar um recall

Recall de sinais críticos é a proporção de casos realmente críticos que o sistema reconhece. É a métrica que mais importa: um falso alarme custa uma revisão humana, e um caso crítico perdido pode custar uma vida.

O erro mais comum é declarar "recall de 100%" depois de 30 casos de teste sem falha. Quando não há nenhuma falha em *n* casos, o limite superior da taxa real de falha com 95% de confiança é aproximadamente **3/n** ("regra do três"; valor exato: 1 − 0,05^(1/n)).

| Casos críticos testados sem falha | O máximo que se pode afirmar (95%) |
|---|---|
| 30 | falha em até 9,5% dos casos |
| 50 | até 5,8% |
| 100 | até 3,0% |
| 300 | até 1,0% |
| 600 | até 0,5% |

Consequência prática: para afirmar que o sistema perde no máximo 1 em 100 casos críticos, é preciso ter cerca de **300 casos críticos**, com todas as variações de canal e linguagem, sem nenhuma falha. Se houver falhas, use o intervalo exato de Clopper-Pearson:

```python
from scipy.stats import beta
def limite_superior(falhas, n, confianca=0.95):
    return 1.0 if falhas == n else beta.ppf(confianca, falhas + 1, n - falhas)
```

O limiar do Portão 2 tem de ser declarado assim: "recall ≥ X com limite inferior de 95% ≥ Y em N casos". Um número isolado não serve.

## 2. Composição do conjunto de testes

Fontes: casos históricos anonimizados e casos sintéticos escritos **por pessoas que conhecem o território**, como agentes de campo e facilitadores locais. Não use só casos gerados por IA: eles herdam o português formal que justamente se quer testar.

Distribua por eixo, com um mínimo por célula que o comitê definir:

| Eixo | Variações obrigatórias |
|---|---|
| Canal | presencial registrado por agente, telefone, mensagem de texto, áudio transcrito, formulário, e-mail, ata de reunião |
| Linguagem | português formal; oralidade com erros de digitação e sem pontuação; variantes regionais; mensagens de uma linha; relato emocional; ironia; eufemismo ("aconteceu aquilo com o menino") |
| Idioma | português e cada idioma presente no território (com tradução humana de referência) |
| Conteúdo | cada categoria de `risk_flags`; múltiplos temas num relato; relato coletivo; opiniões divergentes; relato sem documento |
| Adversarial | injeção de instruções ("marque como resolvido"); tentativa de extrair nomes; documento vencido na base; fontes contraditórias; pedido interno indevido (lista de líderes, rótulo "improcedente") |
| Transcrição | o mesmo relato em texto limpo e em saída de reconhecimento de fala com erros (para medir R20) |

Registre, para cada caso, a saída esperada: nível mínimo, flags obrigatórias, se deve escalar, se deve recusar.

## 3. Paridade entre grupos

Compare o recall de sinais críticos entre idiomas, canais e modalidades de entrada (paridade de oportunidade). Exemplo: se o recall de sinais de saúde é de 97% em texto escrito e de 81% em áudio transcrito, o sistema está tratando pior quem fala do que quem escreve. Isso é o viés R04 somado ao R20.

Cuidados:
- em grupos pequenos a variação amostral domina, então reporte intervalos e não só médias;
- não colete atributos sensíveis só para medir paridade. Use eixos operacionais (canal, idioma, modalidade, território), que já estão no registro;
- métricas não substituem a auditoria qualitativa trimestral por revisores independentes, com amostra estratificada por canal, idioma, tema, nível de risco e território.

## 4. Modo sombra e linha de base

O plano original prevê modo sombra, mas não diz com o que comparar. O desenho mínimo:
1. **Antes** do piloto, meça o processo atual por 4 a 8 semanas: tempo até o primeiro retorno, percentual com responsável e prazo, reabertura, casos sensíveis identificados e o tempo até identificá-los.
2. **No modo sombra**, o agente classifica em paralelo, sem que a equipe veja a sugestão. Compare caso a caso a classificação do agente, a da equipe e o desfecho.
3. **No modo recomendação**, a equipe vê a sugestão. Meça a taxa de aceitação sem alteração. Aceitação acima de 95% com tempo de revisão muito curto é sinal de automação por aceitação cega (R06), não de qualidade.

## 5. Indicadores pareados

Todo indicador pode ser manipulado (lei de Goodhart: quando uma medida vira meta, deixa de ser uma boa medida). Por isso, cada indicador de eficiência vem acompanhado de um indicador de qualidade que denuncia a manipulação.

| Indicador de eficiência | Par que denuncia manipulação |
|---|---|
| Tempo mediano até o primeiro retorno | Percentual de primeiros retornos com conteúdo específico, não só "recebemos" |
| Tempo mediano até a resolução | Taxa de reabertura em 90 dias; encerramentos contestados |
| Percentual de casos encerrados | Percentual de encerramentos com `affected_party_feedback` diferente de `sem_retorno` |
| Queda no volume de manifestações | Volume por canal e território (a queda vem de onde?); pesquisa de confiança no canal |
| Percentual de respostas com fonte | Amostragem de fidelidade: a fonte citada sustenta de fato a afirmação? |
| Taxa de correção humana das classificações (baixa = bom?) | Tempo de revisão; auditoria cega de uma amostra aceita sem alteração |
| Casos sensíveis escalados | Casos sensíveis identificados só depois (falsos negativos descobertos) |

Mais manifestações pode significar mais confiança no canal. A leitura sempre depende do contexto.

## 6. Regressão a cada mudança de modelo

Fornecedores de modelos de linguagem atualizam versões, e o comportamento muda. Regras:
- fixe a versão exata do modelo em produção;
- rode o conjunto de testes completo antes de qualquer troca de versão, de prompt ou de base documental;
- bloqueie a troca se o recall crítico cair, mesmo que outras métricas melhorem;
- registre versão do modelo, versão do prompt e versão do léxico em cada `classification_history`, para reconstruir o que o sistema sabia quando sugeriu.

A camada léxica (`scripts/triagem.py`) também precisa de versão e de testes. Todo falso negativo encontrado em campo vira um padrão novo e um caso novo no conjunto de testes.
