import random

# ============================================================
#  PROBLEMA D - Cartas
#  MM3014 Teoría de Probabilidades - Parcial 4
# ============================================================
#
#  ESTRUCTURA GENERAL DEL EXPERIMENTO:
#  - Se construye una baraja de 52 cartas como lista
#  - Se extraen N cartas SIN reemplazo  →  random.sample()
#  - Se estiman probabilidades y se verifica independencia
#
#  CÓMO MODIFICAR PARA EL PARCIAL:
#  - Cambiar cuántas cartas se extraen
#  - Cambiar los eventos A y B (ej. "primera es corazón", etc.)
#  - Para independencia: verificar si P(A∩B) ≈ P(A)·P(B)
# ============================================================

# ── Fijar semilla aleatoria SIEMPRE con 2026 ──────────────────
random.seed(2026)

# ── Parámetros ────────────────────────────────────────────────
N = 10000   # repeticiones (NO cambiar)

# ── Construcción de la baraja estándar de 52 cartas ──────────
#    4 palos × 13 valores = 52 cartas
#    Cada carta es una tupla (valor, palo)
#    MODIFICAR si el problema usa una baraja diferente

palos  = ['♠', '♥', '♦', '♣']                          # 4 palos
valores = ['A', '2', '3', '4', '5', '6', '7',
           '8', '9', '10', 'J', 'Q', 'K']              # 13 valores

baraja = [(v, p) for p in palos for v in valores]       # 52 cartas
# Ejemplo: ('A','♠') es el As de Espadas

# ════════════════════════════════════════════════════════════
#  PARTE 1 – P(ambas cartas son Ases)
# ════════════════════════════════════════════════════════════
#
#  Evento favorable: las DOS cartas extraídas tienen valor 'A'
#  Valor exacto: C(4,2)/C(52,2) = 6/1326 = 1/221 ≈ 0.004524
#
#  MODIFICAR AQUÍ si el temario pide:
#    - Otro valor (ej. ambas son Reyes → 'K')
#    - Otro palo  (ej. ambas son Corazones → palo '♥')
#    - Otra cantidad de cartas extraídas
#

conteo_ambas_ases = 0

for _ in range(N):
    # Extraer 2 cartas sin reemplazo
    carta1, carta2 = random.sample(baraja, 2)

    # Condición: ambas son Ases  (valor == 'A')
    # CAMBIAR 'A' por el valor que pida el temario
    if carta1[0] == 'A' and carta2[0] == 'A':
        conteo_ambas_ases += 1

prob_ambas_ases = conteo_ambas_ases / N
print(f"P(ambas ases) = {prob_ambas_ases:.4f}   "
      f"(valor exacto 1/221 ≈ 0.004524)")


# ════════════════════════════════════════════════════════════
#  PARTE 2 – Verificar independencia de A y B
# ════════════════════════════════════════════════════════════
#
#  Evento A : la PRIMERA carta es un As
#  Evento B : la SEGUNDA carta es un As
#
#  Independencia: A y B son independientes  ⟺  P(A∩B) = P(A)·P(B)
#
#  Si P(ambas ases) ≈ P(A) * P(B)  →  independientes : True
#  Si no                            →  independientes : False
#
#  NOTA: con extracción SIN reemplazo, A y B NO son independientes
#  porque saber que A ocurrió cambia las probabilidades para B.
#
#  MODIFICAR AQUÍ si el temario cambia los eventos A o B:
#    Evento A = "primera carta es de corazones"  → carta1[1] == '♥'
#    Evento B = "segunda carta es figura"        → carta2[0] in ['J','Q','K']
#

conteo_A    = 0   # veces que ocurrió el evento A
conteo_B    = 0   # veces que ocurrió el evento B
conteo_AyB  = 0   # veces que ocurrieron A Y B al mismo tiempo (intersección)

for _ in range(N):
    carta1, carta2 = random.sample(baraja, 2)

    # Definición de cada evento (CAMBIAR según temario)
    ocurre_A = (carta1[0] == 'A')   # primera carta es As
    ocurre_B = (carta2[0] == 'A')   # segunda carta es As

    if ocurre_A:
        conteo_A += 1
    if ocurre_B:
        conteo_B += 1
    if ocurre_A and ocurre_B:
        conteo_AyB += 1

# Probabilidades estimadas
prob_A   = conteo_A   / N
prob_B   = conteo_B   / N
prob_AyB = conteo_AyB / N          # = prob_ambas_ases (mismo evento)

producto_PA_PB = prob_A * prob_B   # si fueran independientes deberían ser ≈ iguales

# Decisión de independencia:
# Se usa una tolerancia pequeña (0.001) para comparar valores simulados
# MODIFICAR la tolerancia si se pide mayor o menor precisión
tolerancia   = 0.001
independientes = abs(prob_AyB - producto_PA_PB) < tolerancia

print(f"P(A) * P(B) = {producto_PA_PB:.4f}   "
      f"(valor exacto 1/169 ≈ 0.005917)")
print(f"Los eventos son independientes: {independientes}")

# ── Explicación del resultado ─────────────────────────────────
# P(A∩B) ≈ 0.0036  ≠  P(A)·P(B) ≈ 0.0055
# → Los eventos NO son independientes porque al extraer sin
#   reemplazo, saber que la primera carta es As hace MENOS
#   probable que la segunda también lo sea (quedan 3 Ases en 51).