# Módulo B — Avaliação de Viabilidade [CORE]

Núcleo analítico do agente. Seis dimensões independentes, cada uma avaliada em escala 0-10 com
critérios objetivos, integrando o SWOT quantitativo. O score consolidado ponderado classifica
o negócio em **Go / No-Go / Go-Conditional**.

## As seis dimensões (pesos e critérios)

| Dimensão | Peso | O que avalia | Critério para score 8+ |
|----------|------|--------------|------------------------|
| Mercado | 20% | TAM/SAM/SOM, CAGR, fragmentação competitiva, tendências macro | TAM > R$500M, CAGR > 15%, fragmentação média |
| Produto | 20% | Proposta de valor, PMF, diferenciação, defensabilidade, maturidade tech | Diferenciação clara, MVP validado, defesa via dados/tech |
| Financeiro | 25% | Unit economics (CAC, LTV, payback), projeções, runway, margem | LTV/CAC > 3, payback < 18m, margem bruta > 40%, runway > 12m |
| Operacional | 15% | Capacidade de execução, processos, supply chain, escalabilidade | Processos documentados, escala sem explosão de custo |
| Regulatório | 10% | Compliance, licenças, riscos jurídicos, privacidade de dados | Sem licenças críticas pendentes, LGPD ok, baixo risco |
| Time | 10% | Experiência do fundador, completude, alignment, track record | Fundador com domínio setorial, time cobre funções críticas |

## Escala de scoring 0-10 com âncoras objetivas

Aplicadas uniformemente, com **adaptação por estágio**: ideação avalia tração/financeiro com
mais tolerância; scaling avalia operacional/regulatório com mais rigor. Aplicar critérios de
scaling a um MVP produziria universalmente No-Go, ignorando a natureza iterativa.

| Score | Classificação | Âncora objetiva |
|-------|---------------|-----------------|
| 0-2 | Crítico | Dimensão em colapso. Bloqueador absoluto. Ex.: TAM < R$10M, CAC > LTV, time sem fundador técnico em tech business. |
| 3-4 | Insuficiente | Dimensão frágil. Reformulação necessária antes de investimento sério. Corrigível em 6-12 meses. |
| 5-6 | Moderado | Dimensão aceitável com pontos cegos. Prosseguimento possível com monitoramento e mitigação ativa. |
| 7-8 | Forte | Dimensão sólida. Suporta investimento e scaling. Refinamentos pontuais. |
| 9-10 | Excepcional | Classe mundial. Vantagem competitiva sustentável. Rara em estágios iniciais. |

## Integração SWOT → Score

Inovação metodológica central. Cada item do SWOT recebe **peso 1-5** conforme magnitude:

```
score_dimensão = base_analítica + Σ(forças × peso)/5 − Σ(fraquezas × peso)/5
                 (limitado entre 0 e 10)
```

- Forças **somam** ao score da dimensão correspondente.
- Fraquezas **subtraem**.
- Ameaças reduzem score de **Mercado** ou **Regulatório**.
- Oportunidades elevam score de **Mercado**.

Exemplo: uma força de peso 5 em produto adiciona +1 ao score de Produto; uma ameaça de peso 5
em mercado subtrai 1 do score de Mercado.

## Matriz de decisão final

Score consolidado = média **ponderada** das seis dimensões (Financeiro 25% e Mercado 20% pesam
mais por determinarem o teto; Produto 20% é o vetor de execução).

| Recomendação | Score | Critério adicional |
|--------------|-------|--------------------|
| **GO** | ≥ 7.0 | Nenhuma dimensão abaixo de 5. Prosseguir com investimento e execução. |
| **GO-CONDITIONAL** | 5.5 — 6.9 | Pontos críticos identificáveis. Prosseguir condicionado a validações listadas. |
| **NO-GO** | < 5.5 | Reformular radicalmente ou descontinuar. |

> **Regra de Bloqueio:** score ≤ 2 em **qualquer** dimensão força No-Go independentemente da
> média — uma dimensão em colapso indica bloqueador estrutural não-corrigível no curto prazo.
