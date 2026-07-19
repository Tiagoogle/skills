# Módulo C — Mapeamento de Riscos e Potencial Exponencial

Viabilidade é necessária mas insuficiente. Aplique **dois frameworks em paralelo**: matriz de
risco 5×5 e scorecard de potencial exponencial. A combinação sinaliza o **Triângulo de Ouro**.

## Matriz de Risco 5×5

Classifique cada risco em duas dimensões:
- **Probabilidade**: 1 = raro … 5 = quase certo.
- **Impacto**: 1 = cosmético … 5 = existencial.

Severidade = probabilidade × impacto:

| Faixa | Cor | Ação |
|-------|-----|------|
| 1-6 | 🟢 Verde | Monitorar |
| 8-12 | 🟡 Amarelo | Mitigar |
| 15-25 | 🔴 Vermelho | Bloqueador — exigir plano de mitigação antes de prosseguir |

### Seis categorias de risco cobertas

| Categoria | Exemplos |
|-----------|----------|
| Mercado | Mudança de preferência do cliente, entrada de jogador bem-capitalizado, comoditização, mudança regulatória setorial. |
| Operacional | Falha de fornecedor crítico, perda de capacidade produtiva, dependência de pessoa-chave, incidentes de qualidade. |
| Financeiro | Burn acima do previsto, captação não-realizada, inadimplência atípica, câmbio/juros adversos. |
| Regulatório | Mudança de legislação, revogação de licença, processo judicial, infração LGPD/GDPR, sanção antitruste. |
| Tecnológico | Obsolescência da stack, quebra de segurança, falha de escala técnica, dependência de plataforma de terceiros. |
| Time | Saída de co-fundador, conflito societário, dificuldade de atração, desalinhamento cultural em scaling. |

## Scorecard de Potencial Exponencial (0-100)

Crescimento exponencial emerge de **alavancas estruturais** onde o crescimento de hoje reduz o
custo marginal do crescimento de amanhã. Atribua os pontos e some.

| Alavanca | Como funciona | Pts máx |
|----------|---------------|---------|
| 1. Network Effects | Cada novo usuário aumenta o valor para os existentes (plataformas de dois lados, marketplaces, redes). Sem ele, escala é linear. | 25 |
| 2. Economias de Escala | Custo marginal decrescente; margem cresce com volume (infra, manufacturing, SaaS com serving barato). | 20 |
| 3. Automação / Alavancagem Tech | Entregar valor com time pequeno (software, IA); receita por empregado cresce sem custo proporcional. | 20 |
| 4. Viralidade | Usuários trazem novos sem custo de aquisição; coeficiente viral > 1 permite crescer sem marketing. | 15 |
| 5. Dados Acumulados (Data Flywheel) | Mais uso → mais dados → melhor produto → mais uso. Defensibilidade ML-driven. | 10 |
| 6. Economias de Escopo | Lançar produtos adjacentes com custo marginal baixo, reaproveitando infra, cliente e dados. | 10 |

### Interpretação do score exponencial

| Faixa | Leitura |
|-------|---------|
| < 25 | Fundamentalmente linear. Pode ser lucrativo, mas raramente atrai VC ou atinge escala unicórnio. |
| 25-50 | Potencial exponencial parcial. Geralmente suficiente para seed / Series A. |
| 50-75 | Trajetória exponencial clara. Atraente para VCs de growth. |
| > 75 | Excepcional. Tipicamente reservado a network effects dominantes em mercados massivos. |

> **Triângulo de Ouro:** negócios excepcionais combinam (1) viabilidade ≥ 7.0, (2) matriz de
> risco sem bloqueadores vermelhos sem mitigação, e (3) score exponencial ≥ 50. A presença
> simultânea dos três é indicador robusto de oportunidade de alto potencial.

## Output do módulo

Matriz de risco (com top 5 vermelhos e mitigação) + scorecard de potencial exponencial (0-100
com justificativa por alavanca).
