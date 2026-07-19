# Implantação e Uso

O texto canônico do prompt (para colar em system prompt / custom instructions de qualquer LLM)
está em [`prompt-mestre.md`](prompt-mestre.md). Adapte apenas a seção `[CONFIGURÁVEL]`.

## Configurações recomendadas para LLMs

| Parâmetro | Valor | Justificativa |
|-----------|-------|---------------|
| Temperature | 0.3 — 0.5 | Baixa temperatura para consistência analítica. Alta prejudica replicabilidade de scoring. |
| Top-p | 0.9 | Padrão. Alguma diversidade lexical sem comprometer precisão factual. |
| Max tokens | 6000+ | Análises completas exigem 4000-6000 tokens de output. Configure alto para evitar cortes. |
| Context window | Máximo disponível | Documentos de apoio (planos, financials) podem ser extensos. Use modelo com 100k+ tokens. |
| System prompt prioridade | Alta | Em APIs, garanta aderência às diretivas. |
| Streaming | Habilitado | Para análises longas, melhora a experiência de uso. |

## Roteiro de deployment por plataforma (resumo)

- **ChatGPT (Custom GPT):** cole o prompt em *Instructions*; adicione conversation starters
  ("Avalie este plano de negócio", "Estruture OKRs trimestrais", "Faça due diligence",
  "Aplique stress test", "Calcule valuation"); ative Code Interpreter e Web Browsing.
- **Claude (Projects):** cole em *Custom instructions*; anexe planos e materiais em *Project
  knowledge*; aproveite o contexto grande para planos completos.
- **Gemini (Gems):** cole em *Instructions*; se necessário, acrescente "Seja exaustivo na
  análise" (Gemini tende a ser mais conciso).

## Exemplos de primeira mensagem por perfil

**Empreendedor em validação (Modo Mentor):**
> "Avalie meu plano de negócio. Startup SaaS B2B de gestão de estoque para microvarejistas,
> estágio de MVP com 38 clientes pagantes e R$42k MRR. Quero avaliação de viabilidade completa
> com Lean Canvas e estruturação de OKRs para o próximo trimestre. Tom didático, sou
> first-time founder."

**Investidor em due diligence (Modo Executivo):**
> "Faça due diligence técnica e financeira de uma oportunidade de Series A. Empresa: fintech de
> crédito para MEIs, MRR R$680k, 18 meses de operação, captable com 3 seed investors. Tenho
> data room com financials e deck. Quero matriz de risco, scorecard exponencial e valuation
> range via VC Method e Scorecard Method. Direto ao ponto."

**Consultor com cliente PME (Modo Analista):**
> "Estou apoiando uma PME tradicional (indústria de embalagens, R$45M de receita anual) que
> quer transformação digital. Preciso de diagnóstico completo com BMG + SWOT + 5 Forças,
> viabilidade de construir vertical de e-commerce própria vs parceria com marketplace, e plano
> de ataque em 3 horizontes. Exaustivo em frameworks, com cálculos suportando recomendações."

## Iteração e refinamento

Trate o skill como instrumento iterativo. Documente gaps (tom, foco, excessos) e ajuste a seção
`[CONFIGURÁVEL]` preservando os módulos centrais. Recomendação final: trate o agente como um
consultor júnior experiente — exija estrutura, peça evidências, desafie hipóteses e use o output
como **input para a decisão humana final**, nunca como substituto dela.
