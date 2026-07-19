# Módulo D — Plano de Ataque [CORE]

Converte diagnóstico em execução. Combina OKRs (meta-setting), roadmap de três horizontes
(sequenciamento), pirâmide de métricas com North Star, e AARRR (funil de crescimento).

## Estruturação de OKRs

3 a 5 **Objectives** estratégicos, cada um com 3 a 4 **Key Results** quantificáveis.
Objectives são qualitativos, ambiciosos e inspiradores; KRs são quantitativos, mensuráveis e
com prazo. Rejeite OKRs ambíguos ("melhorar produto"); aceite mensuráveis ("elevar NPS de 32
para 50", "crescer MRR de R$80k para R$250k").

Exemplo (startup SaaS B2B):

| Obj | Descrição | Key Results |
|-----|-----------|-------------|
| O1 | Validar product-market fit no segmento prioritário | KR1: 50 entrevistas concluídas. KR2: NPS ≥ 40 (de 22). KR3: Retenção D30 ≥ 45% (de 28%). KR4: 15 case studies. |
| O2 | Construir máquina de aquisição previsível | KR1: CAC pago < R$450 (de R$890). KR2: 4 canais orgânicos ativos. KR3: Coeficiente viral ≥ 0.3. KR4: Outbound = 30% dos leads. |
| O3 | Atingir unit economics saudável para escalar | KR1: LTV/CAC ≥ 3.5 (de 2.1). KR2: Payback < 12m (de 19m). KR3: Margem bruta ≥ 65% (de 52%). KR4: Burn ≤ R$180k/mês (de R$290k). |

## Pirâmide de métricas (North Star)

- **North Star Metric (NSM)** — topo: valor central entregue ao cliente. Única, mensurável,
  correlacionada com sucesso de longo prazo.
- **Input Metrics** — meio: vetores que movem a NSM, sob controle direto do time.
- **Output Metrics** — base: consequências derivadas (receita, margem, valuation).

North Star por modelo de negócio:

| Modelo | North Star candidate | Racional |
|--------|----------------------|----------|
| SaaS B2B | Net Revenue Retention (NRR) | Combina retenção + expansão. NRR > 100% = growth sem novos clientes. |
| Marketplace | GMV / dia ativo | Volume bruto transacionado por usuário ativo. |
| Consumer SaaS | Time spent in app / semana | Engajamento profundo precede retenção e monetização. |
| E-commerce | Pedidos / cliente ativo / mês | Frequência prevê LTV melhor que ticket médio. |
| Fintech crédito | Juros recebidos / inadimplência | Spread efetivo = saúde do livro de crédito. |
| Media / Content | Tempo de atenção / usuário / dia | Atenção é o insumo monetizável. |

## AARRR (Pirate Metrics)

Funil de Dave McClure conectando a NSM às ações. Estruture **sempre na sequência** para que
ganhos em um estágio não prejudiquem os seguintes (armadilha do foco só em Acquisition):

- **Acquisition** — marketing.
- **Activation** — produto/onboarding.
- **Retention** — Customer Success.
- **Revenue** — Sales/Pricing.
- **Referral** — Produto/Marketing.

## Roadmap de três horizontes

| Horizonte | Função | Entregáveis esperados |
|-----------|--------|-----------------------|
| H1 — 90 dias | Validar | Testar hipóteses de PMF, validar canal principal, confirmar unit economics preliminar. Ex.: MVP estável, 50 clientes pagantes piloto, dashboard de métricas v1. |
| H2 — 12 meses | Executar | Escalar canal validado, refinar produto, unit economics saudável. Ex.: R$250k MRR, CAC < R$450, retenção D90 > 60%, time de 12, Series A (se aplicável). |
| H3 — 36 meses | Escalar | Capturar potencial exponencial, expansão/adjacências, defensibilidade estrutural. Ex.: R$5M+ ARR, 2 países, produto adjacente, valuation Series B/C. |

## Marcos críticos com gatilhos de decisão

Marcos são **gatilhos de decisão binários**, não entregáveis genéricos.

| Marco | Critério de sucesso | Gatilho de contingência |
|-------|---------------------|-------------------------|
| M1 (Dia 30) | MVP em produção com 10 usuários ativos | Se não: parar e revisar arquitetura técnica. |
| M2 (Dia 60) | Retenção D7 ≥ 35% | Se não: pivotar proposição de valor ou segmento. |
| M3 (Dia 90) | 50 clientes pagantes, NPS ≥ 40 | Se não: redirecionar esforços para PMF antes de escalar. |
| M4 (Mês 6) | MRR R$80k, CAC < R$600 | Se não: revisar modelo de go-to-market. |
| M5 (Mês 12) | MRR R$250k, LTV/CAC ≥ 3 | Se não: avaliar pivot ou descontinuação. |

## Alocação de recursos (regra 70/20/10)

Alocação em três dimensões: **capital**, **time** e **foco executivo**. Default recomendado:
- **70%** — prioridade principal do horizonte atual.
- **20%** — iniciativas secundárias que preparam o próximo horizonte.
- **10%** — experimentação de ideias que podem se tornar o horizonte seguinte.

Alocação uniforme é sintoma de falta de priorização e deve ser questionada.

## Output do módulo

OKR tree + roadmap de 3 horizontes + plano de alocação de recursos.
