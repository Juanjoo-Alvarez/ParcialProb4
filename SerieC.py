import random

# ============================================================
#  PROBLEMA C - Canicas de colores
#  MM3014 Teoría de Probabilidades - Parcial 4
# ============================================================
#
#  ESTRUCTURA GENERAL DEL EXPERIMENTO:
#  - Se define una "urna" (lista) con objetos de distintos tipos
#  - Se extraen N elementos SIN reemplazo  →  random.sample()
#  - Se cuentan los casos favorables y se divide entre total
#
#  CÓMO MODIFICAR PARA EL PARCIAL:
#  - Cambiar la composición de la urna (cantidad de cada color)
#  - Cambiar cuántas canicas se extraen (k en random.sample)
#  - Cambiar la condición que se evalúa (ej. "ambas azules", etc.)
# ============================================================

# ── Fijar semilla aleatoria SIEMPRE con 2026 ──────────────────
random.seed(2026)

# ── Parámetros del experimento ────────────────────────────────
N = 10000   # número de repeticiones (NO cambiar)

# ── Definición de la urna (AQUÍ SE PUEDE MODIFICAR) ──────────
# Caja 1: 5 rojas, 3 azules, 2 verdes  →  10 canicas en total
caja1 = ['R']*5 + ['A']*3 + ['V']*2   # R=roja, A=azul, V=verde

# Caja 2: 2 rojas, 5 azules, 3 verdes  →  10 canicas en total
caja2 = ['R']*2 + ['A']*5 + ['V']*3


# ════════════════════════════════════════════════════════════
#  PARTE 1 – P(ambas rojas) con UNA sola caja (caja1)
# ════════════════════════════════════════════════════════════
#
#  Experimento: extraer 2 canicas de caja1 SIN reemplazo
#  Evento favorable: las dos canicas son rojas
#
conteo_ambas_rojas = 0

for _ in range(N):
    # random.sample(urna, k) → extrae k elementos sin reemplazo
    extraccion = random.sample(caja1, 2)

    # Condición: AMBAS son rojas
    # MODIFICAR AQUÍ si el temario pide otro color u otra cantidad
    if extraccion[0] == 'R' and extraccion[1] == 'R':
        conteo_ambas_rojas += 1

prob_ambas_rojas = conteo_ambas_rojas / N
print(f"P(ambas rojas) = {prob_ambas_rojas:.4f}   "
      f"(valor exacto 2/9 ≈ 0.2222)")


# ════════════════════════════════════════════════════════════
#  PARTE 2 – P(Caja 1 | una roja y una verde)   [Bayes]
# ════════════════════════════════════════════════════════════
#
#  Experimento:
#    1. Elegir una caja AL AZAR (prob 1/2 cada una)
#    2. Extraer 2 canicas sin reemplazo de esa caja
#
#  Evento A : las canicas son {una roja, una verde}  (en cualquier orden)
#  Evento B : la extracción vino de la Caja 1
#  Queremos: P(B | A)  =  casos(B y A) / casos(A)
#
#  MODIFICAR AQUÍ si el temario cambia:
#    - La condición observada  (ej. "una azul y una verde")
#    - El número de cajas
#    - La composición de las cajas
#

conteo_una_roja_una_verde   = 0   # veces que el evento A ocurrió
conteo_caja1_dado_evento_A  = 0   # veces que A ocurrió Y vino de Caja 1

for _ in range(N):
    # Paso 1: elegir caja (0 → caja1, 1 → caja2)
    caja_elegida = random.choice([caja1, caja2])
    es_caja1     = (caja_elegida is caja1)   # True / False

    # Paso 2: extraer 2 canicas sin reemplazo
    extraccion = random.sample(caja_elegida, 2)

    # Condición observada: UNA roja y UNA verde (sin importar orden)
    # set({'R','V'}) cubre ambos órdenes  →  {'R','V'} == {'V','R'}
    if set(extraccion) == {'R', 'V'}:
        conteo_una_roja_una_verde += 1
        if es_caja1:
            conteo_caja1_dado_evento_A += 1

# Probabilidad condicional P(Caja1 | una roja y una verde)
if conteo_una_roja_una_verde > 0:
    prob_caja1_condicional = conteo_caja1_dado_evento_A / conteo_una_roja_una_verde
else:
    prob_caja1_condicional = 0.0

print(f"P(Caja 1 | una roja y una verde) = {prob_caja1_condicional:.4f}   "
      f"(valor exacto 5/8 = 0.675)")