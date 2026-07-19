# Módulo F — Stress Test

Simula cenários adversos para verificar sobrevivência em condições desfavoráveis. Regra: toda
projeção otimista exige stress test em cenário adverso. **Sobrevivência em cenário pessimista é
pré-requisito de Go** — um negócio que não sobrevive a uma queda de 50% na receita em 6 meses
não é um negócio viável, é uma aposta.

## Os três cenários de stress

| Cenário | Premissa | Variáveis ajustadas | Pergunta-chave |
|---------|----------|---------------------|----------------|
| Pessimista | Prob. 25-30% | Receita −50% em 6m; CAC +30%; churn +50%; burn mantido | Negócio sobrevive 12 meses sem nova captação? |
| Severo | Prob. 10-15% | Receita −75% em 3m; CAC +60%; churn +100%; burn −25% | Negócio sobrevive 6 meses? Quanto precisa cortar? |
| Black Swan | Prob. 1-5% | Perda de cliente-chave (>40% receita); regulação proibitiva; shutdown | Existe pivot viável? Quanto vale o asset residual? |

## Cálculo de runway em stress

```
runway = caixa atual / burn mensal líquido ajustado
```

O burn ajustado incorpora variações **simultâneas** (efeito composto, não isolado): queda de
receita aumenta o burn líquido; aumento de churn acelera a queda de receita; aumento de CAC
reduz a eficiência de aquisição.

**Exemplo prático:** startup com R$3M em caixa, burn de R$250k/mês e receita de R$180k/mês tem
runway nominal de 12 meses.
- **Pessimista** (receita −50% → R$90k; CAC +30%): burn líquido sobe para R$340k/mês → runway
  cai para **8.8 meses**.
- **Severo**: runway cai para **4.2 meses** — abaixo do mínimo operacional de 6 meses, ativando
  gatilho de contingência.

## Plano de contingência por cenário

Para cada um dos **top 5 riscos vermelhos** da matriz (Módulo C), estruture um plano
predefinido — em crise, decisões se executam em dias, não em semanas.

| Componente | Descrição | Exemplo |
|------------|-----------|---------|
| Gatilho | Métrica observável com threshold claro | MRR cair 30% em 2 meses consecutivos. |
| Ação imediata (0-30 dias) | Cortes e realocações para preservar caixa | Congelar contratações; cortar marketing pago 60%; burn → R$150k/mês. |
| Ação tática (30-90 dias) | Reestruturação para sobreviver no novo patamar | Pivot para segmento de maior ticket; renegociar contratos; reduzir headcount 25%. |
| Custo de implementação | Impacto financeiro e operacional estimado | R$200k em severance + 60 dias de perda de produtividade. |
| Critério de sucesso | Condição de recuperação ou descontinuação | Voltar a R$120k MRR em 6 meses OU descontinuar. |

## Gatilhos de pivot e descontinuação

Stress test sem critério de decisão é exercício acadêmico. Defina, **antes de qualquer crise**,
gatilhos **numéricos e datados**:
- *"Se MRR ficar abaixo de R$X por N meses consecutivos, ativamos pivot para segmento Y."*
- *"Se churn ultrapassar Z% por 2 trimestres, descontinuamos o produto."*

A principal razão de startups falharem não é a crise (inevitável), mas a **relutância dos
founders em ativar contingências** por otimismo irracional. Com gatilhos predefinidos e
acordados com conselho/investidores, a decisão se torna objetiva. Recomende formalizá-los em
term sheet ou acordo de acionistas, criando obrigação contratual de ativação.

## Output do módulo

Simulador de stress (3 cenários com runway) + mapa de sobrevivência + gatilhos de decisão.

> Stress test não é pessimismo; é realismo. Negócios que não sobrevivem a uma queda de 50% na
> receita em 6 meses não são negócios viáveis, são apostas disfarçadas.
