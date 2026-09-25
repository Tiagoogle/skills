#!/usr/bin/env python3
"""
Regressão da pré-triagem léxica. Rode após qualquer mudança no léxico.

Cada caso em evals/triagem-regressao.json pode declarar:
  nivel_minimo          nível que a triagem tem de atingir ou superar
  nivel_maximo          nível que a triagem não pode superar (falsos positivos)
  categorias            categorias que têm de aparecer
  categorias_proibidas  categorias que não podem aparecer
  injecao               se a suspeita de injeção tem de ser detectada

Todo falso negativo encontrado em campo deve virar um caso novo aqui.

Uso:
  python scripts/testar_triagem.py
  python scripts/testar_triagem.py caminho/para/casos.json
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from triagem import triar  # noqa: E402

ORDEM = {"nenhum": 0, "alto": 1, "critico": 2}
PADRAO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evals", "triagem-regressao.json")


def main():
    caminho = sys.argv[1] if len(sys.argv) > 1 else PADRAO
    with open(caminho, encoding="utf-8") as f:
        casos = json.load(f)

    falhas = 0
    for i, caso in enumerate(casos, 1):
        r = triar(caso["texto"])
        cats = {s["categoria"] for s in r["sinais"]}
        problemas = []
        if "nivel_minimo" in caso and ORDEM[r["nivel"]] < ORDEM[caso["nivel_minimo"]]:
            problemas.append(f"nível {r['nivel']} < mínimo {caso['nivel_minimo']}")
        if "nivel_maximo" in caso and ORDEM[r["nivel"]] > ORDEM[caso["nivel_maximo"]]:
            problemas.append(f"nível {r['nivel']} > máximo {caso['nivel_maximo']} ({sorted(cats)})")
        faltando = set(caso.get("categorias", [])) - cats
        if faltando:
            problemas.append(f"faltam categorias {sorted(faltando)}")
        indevidas = set(caso.get("categorias_proibidas", [])) & cats
        if indevidas:
            problemas.append(f"categorias indevidas {sorted(indevidas)}")
        if "injecao" in caso and r["suspeita_injecao"] != caso["injecao"]:
            problemas.append(f"injeção esperada={caso['injecao']} obtida={r['suspeita_injecao']}")

        if problemas:
            falhas += 1
            print(f"FALHA {i:02d}: {caso['texto'][:70]}")
            for p in problemas:
                print(f"         - {p}")
        else:
            print(f"ok    {i:02d}: {caso['texto'][:70]}")

    print(f"\n{len(casos) - falhas}/{len(casos)} casos passaram.")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
