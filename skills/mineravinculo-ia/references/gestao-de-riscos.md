# Gestão de riscos e governança — Modo B (implantar ou auditar)

## Sumário
1. Premissa
2. Espinha dorsal: critérios de eficácia do Princípio 31 dos UNGPs
3. Matriz de classificação
4. Registro de riscos (R01–R25)
5. Fatores contextuais de vulnerabilidade
6. Governança e independência
7. Portões de implantação
8. Incidentes
9. Critérios de parada
10. Contestação e reparação
11. Checklist de aprovação
12. Formato do parecer

---

## 1. Premissa

Para comunidades vulneráveis, a principal salvaguarda é limitar a autoridade do modelo, não torná-lo mais persuasivo. O agente registra, organiza e acompanha. Ele não decide quem merece ser ouvido, qual relato é verdadeiro, qual dano é aceitável nem qual solução será imposta. Se as reclamações caírem porque ficou mais difícil reclamar, o agente falhou, mesmo que os indicadores operacionais melhorem.

## 2. Espinha dorsal: critérios de eficácia do Princípio 31 dos UNGPs

Os Princípios Orientadores da ONU sobre Empresas e Direitos Humanos (2011), Princípio 31, definem oito critérios para mecanismos não judiciais de reclamação. O guia do ICMM de 2019 sobre reclamações locais adota os mesmos critérios. Os documentos originais citavam os UNGPs, mas não os usavam como critério de auditoria. Aqui eles organizam o parecer.

| Critério (UNGP 31) | Pergunta de auditoria | Evidência mínima | Controles desta skill |
|---|---|---|---|
| Legítimo | As comunidades confiam no mecanismo e há proteção contra interferência de quem é alvo da reclamação? | Instância independente definida e operando; casos contra a própria equipe ou a segurança seguem outra rota | `independent_channel`, §6 |
| Acessível | Todos os grupos conseguem usar, inclusive sem internet, sem escrita e em outro idioma? | Volume e tempo de resposta por canal, idioma e modalidade; canal não digital com a mesma qualidade | R01, R02, R20; campos `channel`, `language`, `input_modality` |
| Previsível | Há etapas, prazos e resultados possíveis conhecidos? | Prazos publicados; percentual de casos com prazo aprovado | `due_date_approved_by`, E11 |
| Equitativo | A pessoa tem acesso a informação e a assessoria em condições justas? | Assessoria técnica independente disponível onde cabe (PNAB, art. 3º, V); tradução | §6, R24 |
| Transparente | A pessoa acompanha o andamento, e o público vê o desempenho agregado? | Retorno periódico; relatório público agregado com supressão de células pequenas | Rascunho padrão, R22 |
| Compatível com direitos | Os resultados respeitam direitos, e o mecanismo não bloqueia a via judicial? | Não se exige renúncia a direitos; encaminhamento externo disponível | §10, E07 |
| Fonte de aprendizado contínuo | O que se aprende volta para a operação? | Análise de reincidência por tema; mudanças operacionais registradas | `reopen_count`, indicadores |
| Baseado em diálogo | Os usuários participaram do desenho e da avaliação? | Registro das objeções e do que mudou; avaliação comunitária como critério de expansão | Portões 1 e 4 |

## 3. Matriz de classificação

Combine **probabilidade**, **severidade** e **irreversibilidade**. Um risco de baixa probabilidade é crítico se o dano for grave ou difícil de reparar.

| Nível | Critério | Exemplo | Regra |
|---|---|---|---|
| Crítico | Morte, violência, perda de direitos, retaliação, deslocamento indevido, dano grave irreversível | Identificação de denunciante em conflito fundiário; atraso no PAE | Não automatizar; escalar imediatamente; revisão independente |
| Alto | Dano relevante à saúde, segurança, renda, participação ou reputação coletiva | Reclamações repetidas sobre água sem investigação | Revisão humana antes de qualquer comunicação; prazo prioritário |
| Médio | Atraso, informação incorreta ou tratamento desigual reparável | Tema ou prazo classificado errado | Revisão pelo responsável; correção documentada |
| Baixo | Sem impacto material provável | Erro de formatação interna | Fluxo normal; acompanhar tendência |

O agente sugere nível e motivo. Ele não pode rebaixar sozinho um caso para "baixo" nem encerrá-lo por falta de resposta.

## 4. Registro de riscos

R01–R18 vêm do plano original, condensados. R19–R25 são lacunas que o plano não cobria.

| ID | Risco | Controle preventivo | Controle detectivo | Dono |
|---|---|---|---|---|
| R01 | Exclusão digital | Canais equivalentes; atendimento itinerante | Volume e tempo por canal; busca ativa quando houver queda atípica | Coordenação social |
| R02 | Viés linguístico | Tradução humana; glossário; testes por idioma | Auditoria de amostras por idioma | Dados + equipe comunitária |
| R03 | Viés de representação histórica | Não usar volume como medida de necessidade; amostragem ativa | Escutas independentes por grupo | Comitê de salvaguardas |
| R04 | Viés de credibilidade (escrita formal > oralidade) | Separar "sem evidência" de "improcedente"; aceitar testemunho | Prioridade e encerramento por `input_modality` | Ouvidoria |
| R05 | Inferência de atributos sensíveis | Bloqueio no prompt e no validador (E10) | Testes de saída; varredura de logs | Privacidade |
| R06 | Automação por aceitação cega | Justificativa visível; aprovação em temas críticos | Taxa de alteração humana; tempo de revisão muito curto | Dono do produto |
| R07 | Alucinação factual | RAG com fontes versionadas; "não confirmado" como resposta válida | Amostragem factual; bloqueio por fonte vencida | Gestão documental |
| R08 | Divulgação de dados | Pseudonimização; minimização; criptografia; acesso por função | Teste de acesso; varredura de relatórios | Encarregado de dados |
| R09 | Retaliação | Opção confidencial; canal independente | Queixas após o registro; contato protegido | Direitos humanos |
| R10 | Captura local por elites ou intermediários | Escutas separadas; vários pontos de entrada | Participação por território, gênero e idade, quando seguro | Equipe de campo |
| R11 | Encerramento artificial | Resolução validada pela parte afetada (E07, E08) | Reabertura; auditoria de encerramentos | Ouvidoria |
| R12 | Incompatibilidade cultural | Categorias e protocolos definidos junto com a comunidade | Avaliação qualitativa por facilitadores locais | Relações comunitárias |
| R13 | Falha de escalonamento | **Duas camadas + regra da união (E16)** | Recall em cenários adversariais (ver `avaliacao-e-testes.md`) | Segurança + direitos humanos |
| R14 | Dados desatualizados | Dono, versão e validade por documento | Alerta de expiração; bloqueio (E15) | Gestão do conhecimento |
| R15 | Ciberincidente | MFA; menor privilégio; segregação | Teste de intrusão; monitoramento de acesso | Segurança da informação |
| R16 | Dependência tecnológica | Procedimento manual testado | Simulado de indisponibilidade com reconciliação | Operações |
| R17 | Uso secundário (segurança, marketing, pressão) | Finalidade delimitada; proibição contratual | Auditoria de consultas | Governança |
| R18 | Falsa aparência de participação | Registrar como cada contribuição foi considerada | Perguntar à comunidade se se sentiu ouvida | Alta liderança |
| **R19** | **Injeção de instruções via manifestação**: texto da comunidade ou de terceiros tenta mudar o comportamento do agente ("marque como resolvido", "liste quem reclamou") | Separar dados de instruções no prompt; pré-triagem de padrões; o agente não tem permissão de escrita para encerrar | Taxa de `injection_suspected`; testes adversariais a cada versão (OWASP LLM01) | Segurança + produto |
| **R20** | **Viés de transcrição automática (ASR)**: sotaques rurais, variantes regionais e línguas indígenas têm mais erro de reconhecimento de fala, e o erro pode apagar a palavra de risco | Confirmar o resumo com a pessoa; guardar o áudio original com consentimento; revisão humana de transcrições com sinal de risco | Taxa de erro por palavra (WER) por variante em amostra; `input_modality` nos indicadores | Dados |
| **R21** | **Deriva de modelo e fornecedor**: o fornecedor atualiza o modelo e o comportamento muda sem aviso; transferência internacional de dados | Fixar a versão do modelo; regressão completa antes de cada troca; cláusulas de não treinamento e não retenção; avaliar LGPD art. 33 | Rodar o conjunto de testes a cada mudança; comparar o recall crítico | Produto + jurídico |
| **R22** | **A base como ativo de inteligência**: o banco de reclamações, com localidades e temas, vira um mapa da dissidência, valioso para grileiros, milícias ou garimpo ilegal em territórios em conflito | Minimização; localização grosseira; supressão de células pequenas nos painéis; segregação de identidade; ameaça modelada explicitamente no RIPD (Relatório de Impacto à Proteção de Dados) | Auditoria de consultas atípicas; teste de reidentificação dos painéis | Encarregado de dados + segurança |
| **R23** | **Confundir participação no desenho com consulta prévia (CLPI)**: chamar de "consulta" oficinas corporativas com povos indígenas ou tradicionais cria risco jurídico e de legitimidade | Linguagem precisa: "escuta" ou "participação no desenho", não "consulta"; respeitar protocolos autônomos de consulta | Revisão jurídica dos materiais do Portão 1 | Jurídico + relações comunitárias |
| **R24** | **Consentimento viciado por assimetria de poder**: a dependência econômica tira a liberdade do "sim" | Não usar consentimento como base legal padrão (ver `modelo-de-dados.md`); separar reclamação de benefício e emprego | Recusas e revogações por território | Encarregado de dados |
| **R25** | **Fluxo paralelo ao PAE de barragem**: o agente triando uma emergência atrasa o acionamento do plano | Emergência de barragem pula a triagem (§5.6 do protocolo); integração documentada com o PAE | Simulado conjunto com a equipe de segurança de barragens | Segurança de barragens |

## 5. Fatores contextuais de vulnerabilidade

"Comunidade vulnerável" não é rótulo fixo e não é inferido pelo modelo. Trabalhe com fatores contextuais e autodeclarados, confirmados só quando necessários para dar proteção ou acessibilidade.

| Fator | Salvaguarda mínima |
|---|---|
| Baixa conectividade | Canal presencial, telefone, registro por agente treinado |
| Baixa alfabetização ou outro idioma | Comunicação oral, tradução, pictogramas, checagem de entendimento |
| Povos indígenas e tradicionais | Protocolo culturalmente adequado; interlocutores reconhecidos pelo próprio grupo; protocolo autônomo de consulta, se houver |
| Mulheres e cuidadoras | Horários flexíveis; atendimento reservado; equipe diversa |
| Crianças e adolescentes | Não coletar diretamente sem protocolo específico (LGPD, art. 14); encaminhar à proteção |
| Pessoas com deficiência | Canal acessível; alternativa humana |
| Migrantes e temporários | Não exigir documento migratório; não retaliação |
| Dependência econômica da operação | Separar reclamação de decisões de emprego e benefício |
| Histórico de conflito ou violência | Avaliação de segurança; confidencialidade; escalonamento independente |
| Isolamento territorial | Atendimento itinerante; prazos compatíveis |
| Moradia em ZAS de barragem | Integração com o PAE; comunicação de risco em linguagem acessível |

## 6. Governança e independência

**Comitê de salvaguardas**: relacionamento comunitário, direitos humanos, privacidade, segurança da informação, jurídico, operação, dados e representantes comunitários com condições reais de participar. O comitê aprova escopo, critérios de risco, testes, incidentes críticos e continuidade.

**Evitar cooptação** (o plano original citava o risco, mas não dizia como evitá-lo): os representantes comunitários são escolhidos pelas próprias comunidades, não pela empresa. A remuneração é transparente e não depende de aprovar o sistema. As atas registram os votos divergentes. A participação não é apresentada como aprovação.

**Instância independente**: o plano original falava em "instância independente" sem defini-la. As opções concretas, da mais independente para a menos, são:
1. assessoria técnica independente (ATI) escolhida pelas comunidades e paga pelo empreendedor sem interferir nela, figura prevista na PNAB (Lei 14.755/2023, art. 3º, V) para populações atingidas por barragens;
2. ouvidoria externa contratada com mandato protegido e reporte ao conselho;
3. ouvidoria interna com reporte fora da linha operacional.

Casos contra a própria equipe do agente, a segurança, as contratadas ou autoridades locais seguem pela opção mais independente disponível.

| Decisão | Responsável | Revisão obrigatória |
|---|---|---|
| Finalidade e escopo | Patrocinador executivo | Comitê de salvaguardas |
| Base documental | Dono do conhecimento | Relacionamento comunitário + jurídico |
| Categorias e critérios | Produto + equipe social | Representantes comunitários |
| Liberação do piloto | Comitê | Auditoria independente |
| Incidente crítico | Líder de resposta | Direitos humanos + alta liderança |
| Expansão | Patrocinador | Evidências do piloto + avaliação das partes afetadas |
| Suspensão | **Qualquer responsável por salvaguarda** | Comunicação posterior ao comitê |

A suspensão só é segura se houver um procedimento manual testado (R16). Sem esse procedimento, desligar o agente gera acúmulo de casos, e o próprio acúmulo vira dano.

## 7. Portões de implantação

Os portões são liberados por **critério cumprido**, não por data.

- **Portão 0 — Justificativa.** Por que um agente? Quais tarefas continuam humanas? Quais alternativas de menor risco foram consideradas? Qual é a linha de base do processo atual? Sem medir o processo atual (tempo até o primeiro retorno, taxa de reabertura, casos sem responsável), não há como provar que o agente melhorou algo. Não implantar se o objetivo real for reduzir acesso, controlar reputação ou substituir equipe de escuta.
- **Portão 1 — Preparação participativa.** Escutas separadas e acessíveis com os grupos afetados. Registrar objeções, mudanças incorporadas, temas que não serão automatizados e canais alternativos. Com povos indígenas ou tradicionais, o calendário é o do protocolo do próprio povo (R23).
- **Portão 2 — Teste técnico e de direitos.** Factualidade, segurança, privacidade, idioma, acessibilidade, vieses por canal, cenários críticos e injeção. A exigência de recall de sinais críticos é maior do que a de conveniência operacional. Ver `avaliacao-e-testes.md`.
- **Portão 3 — Piloto limitado.** Duração, local, usuários, canais, classes de dados e critérios de parada definidos. Modo sombra (o agente sugere, mas a equipe trabalha como antes e as duas saídas são comparadas) antes do modo recomendação. Todas as comunicações externas com revisão humana.
- **Portão 4 — Expansão.** Só com evidência de que o agente não reduziu acesso, não aumentou exposição, não atrasou casos sensíveis e não criou disparidades relevantes. A avaliação da comunidade é critério de aprovação, não comentário.

**Cronograma indicativo de 90 dias do plano original**: vale como referência apenas em territórios sem povos indígenas ou tradicionais e sem conflito ativo. Duas semanas para "consulta participativa" (dias 16–30) não cabem no tempo de decisão coletiva de nenhuma comunidade organizada.

## 8. Incidentes

| Severidade | Exemplos | Resposta |
|---|---|---|
| 1 — crítica | Vazamento de identidade; retaliação; resposta que gerou risco imediato; decisão indevida sobre direitos; perda de registro sensível; atraso em emergência de barragem | Suspender a função; acionar resposta executiva e de direitos humanos; avaliar comunicação à ANPD e aos titulares (LGPD, art. 48) |
| 2 — alta | Falha sistemática de idioma; grupo excluído; atraso em saúde ou segurança; documento vencido em resposta; injeção bem-sucedida | Interromper o fluxo afetado; corrigir antes de continuar |
| 3 — moderada | Erro pontual de classificação, prazo ou síntese sem dano confirmado | Corrigir; notificar o responsável; checar recorrência |
| 4 — baixa | Formato; inconveniente | Manutenção normal |

Resposta mínima a um incidente crítico: preservar logs, limitar o acesso aos dados envolvidos, proteger a pessoa afetada, interromper a automação, informar a instância independente e avaliar a comunicação às autoridades. A correção não apaga o registro do erro. O relatório pós-incidente traz causa, grupos afetados, decisões, reparação oferecida, controles alterados e evidência de que o problema não se repetiu. Quando há dano, reparação e proteção vêm antes do ajuste do modelo.

## 9. Critérios de parada

Suspender, total ou parcialmente, quando houver:
- vazamento ou tentativa comprovada de identificar denunciantes;
- retaliação associada ao canal;
- perda de acesso de um grupo relevante sem canal equivalente funcionando;
- falha recorrente em reconhecer saúde, segurança, direitos ou emergência de barragem;
- documento vencido ou informação inventada em comunicação externa;
- decisão automática sobre compensação, terra, reassentamento, emprego ou encerramento;
- impossibilidade de reconstruir o histórico ou a trilha de auditoria;
- recusa da comunidade em continuar por perda de confiança não resolvida;
- troca de finalidade, fornecedor, **versão do modelo**, território ou tipo de dado sem nova avaliação.

A retomada exige análise de causa, correção, teste independente e comunicação clara aos afetados.

## 10. Contestação e reparação

Canal gratuito, acessível e independente do agente. A contestação preserva o caso original e abre uma nova camada de análise, sem penalizar quem discorda. Em direitos, terras, reassentamento, saúde, segurança ou violência, oferecer encaminhamento a mecanismos externos (Defensoria Pública, Ministério Público, órgãos ambientais), sem exigir renúncia a outras vias.

A LGPD (art. 20) garante pedir revisão de decisões tomadas unicamente por tratamento automatizado, mas **não exige que essa revisão seja feita por uma pessoa**: a exigência de "pessoa natural" saiu do texto com a Lei 13.853/2019. A revisão humana desta skill é, portanto, um compromisso de governança acima do mínimo legal. Ela não deve ser apresentada como mera conformidade.

## 11. Checklist de aprovação

**Governança**
- [ ] Responsáveis executivo e operacional identificados.
- [ ] Comitê com direitos humanos, privacidade, dados, operação e representação comunitária escolhida pelas comunidades.
- [ ] Autoridade de suspensão documentada e procedimento manual testado.
- [ ] Instância independente definida (ATI, ouvidoria externa ou interna com reporte independente).
- [ ] Fornecedor sujeito a auditoria, confidencialidade, não uso secundário, não treinamento e versão fixada.

**Comunidade e direitos**
- [ ] Grupos afetados participaram do desenho; objeções registradas.
- [ ] Canais não digitais equivalentes funcionando.
- [ ] Comunicação sobre IA, dados, revisão humana e contestação compreensível e testada com usuários reais.
- [ ] Proteção contra retaliação e encaminhamento independente.
- [ ] O sistema não substitui consulta, negociação, consentimento, reparação nem o PAE.

**Dados e modelo**
- [ ] Finalidade e base legal de cada campo documentadas; RIPD elaborado (LGPD, art. 38).
- [ ] Identidade protegida; acesso mínimo; supressão de células pequenas nos painéis.
- [ ] Documentos com dono, versão e validade.
- [ ] Conjunto de testes cobrindo idiomas, canais, modalidades, casos críticos e injeção, com tamanho suficiente para o limiar de recall declarado.
- [ ] Inferência de atributos sensíveis bloqueada (prompt + validador).

**Operação**
- [ ] Pré-triagem léxica ativa, com regra da união.
- [ ] Casos críticos com revisão humana obrigatória.
- [ ] Nenhuma promessa não aprovada sai do sistema.
- [ ] Encerramento exige evidência, comunicação e contestação.
- [ ] Indicadores por grupo, canal e modalidade, quando for seguro.
- [ ] Linha de base do processo atual medida antes do piloto.

## 12. Formato do parecer (Modo B)

```
PARECER DE IMPLANTAÇÃO — [projeto / território] — [data]
Escopo avaliado: [documentos, sistema, fase]
Veredito: APTO | APTO COM CONDICIONANTES | NÃO APTO
Bloqueadores (impedem o próximo portão): [item — evidência faltante — dono — como fechar]
Avaliação por critério UNGP 31: [critério — atende / parcial / não atende — evidência]
Riscos R01–R25 sem controle ou sem dono: [...]
Lacunas normativas: [norma — requisito — status — fonte em marco-normativo.md]
Premissas questionáveis: [o que o projeto supõe e por que pode estar errado]
Recomendações priorizadas: [ação — impacto — esforço — prazo sugerido]
Incertezas deste parecer: [o que não foi possível verificar]
```
