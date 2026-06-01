# ============================================================
#  PROBLEMA B - Monedas
#  MM3014 Teoría de Probabilidades - Parcial 4
# ============================================================

#  ESTRUCTURA GENERAL DEL EXPERIMENTO:
#  - Se define 3 monedas justas (cara o cruz)

# ============================================================
# CÓMO MODIFICAR EN EL PARCIAL
# 1) Cambiar el número de monedas:
#    - 3 monedas
#    - 4 monedas
#    - n monedas
#
# 2) Cambiar el evento:
#    ejemplo:
#    exactamente 2 caras
#    al menos 1 cara
#    todas caras
#
# 3) Si piden variable aleatoria: definir X
#    Ejemplo:
#    X = número de caras
#    X = número de cruces
#
# 4) Fórmulas importantes:
# P(E) ≈ conteo / N
# E[X] = Σ x·P(X=x)
#
# En simulación: E[X] ≈ (x1·conteo1 + x2·conteo2 + ...)/N
# ============================================================

# Parametros
import random
random.seed(2026)
N = 10000   # número de repeticiones (NO cambiar)

# Definir las monedas 
# H= cara, T = cruz
moneda1 = ['H', 'T']
moneda2 = ['H', 'T']
moneda3 = ['H', 'T']

# a. Estimar la probabilidad de obtener exactamente 2 caras
# P(exactamente 2 caras)

# Espacio muestral:
# Cada moneda tiene 2 resultados posibles:
# H = cara
# T = cruz

# Total de resultados: 2^3 = 8

# Casos favorables: HHT, HTH,THH
# Total favorables = 3

# Espacio muestral completo: {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}
# Total = 8 resultados

# Valor exacto: P(exactamente 2 caras) = 3/8 = 0.3750

# Simulación: P ≈ conteo / N


# Para conteo de cuantos resultados tienen exactamente 2 caras
conteo_2_caras = 0

# Repetir el experimento N veces
for _ in range(N):
    # Tirar las monedas y el resultado es al azar
    resultado = [random.choice(moneda1), random.choice(moneda2), random.choice(moneda3)]

    # Contar cuántas caras (H) hay en el resultado
    num_caras = resultado.count('H')

    # Verificar si hay exactamente 2 caras
    if num_caras == 2:
        conteo_2_caras += 1


# Calcular la probabilidad estimada
prob_2_caras = conteo_2_caras / N


print(
    f"P(exactamente 2 caras) = {prob_2_caras:.4f} "
    f"(valor exacto 3/8 ≈ 0.3750)"
)

# -----------------------------------------------------------------------------
# b. Sea X el número de caras. Estimar E[X]

#Sea X el número de caras (H) que salen al tirar las 3 monedas
#Como solo hay 3 monedas,entonces X puede ser 0, 1, 2 o 3

# E[X] = 0*P(X=0) + 1*P(X=1) + 2*P(X=2) + 3*P(X=3)

# En simulación, E[X] ≈ (0*conteo_X_0 + 1*conteo_X_1 + 2*conteo_X_2 + 3*conteo_X_3) / N


# Valores posibles:
# X = 0 → TTT
# X = 1 → HTT, THT, TTH
# X = 2 → HHT, HTH, THH
# X = 3 → HHH
conteo_X_0 = 0
conteo_X_1 = 0
conteo_X_2 = 0
conteo_X_3 = 0

# Repetir el experimento N veces
for _ in range(N):
    resultado = [random.choice(moneda1), random.choice(moneda2), random.choice(moneda3)]
    num_caras = resultado.count('H')

    if num_caras == 0:
        conteo_X_0 += 1
    elif num_caras == 1:
        conteo_X_1 += 1
    elif num_caras == 2:
        conteo_X_2 += 1
    elif num_caras == 3:
        conteo_X_3 += 1

# Calcular valor esperado 
# Valor esperado:
# E[X] = Σ x·P(X=x) = 0·P(X=0) + 1·P(X=1) + 2·P(X=2) + 3·P(X=3)
# Aproximación por simulación: P(X=k) ≈ conteo_X_k / N
# Entonces: 
# E[X] = 0*P(X=0) + 1*P(X=1) + 2*P(X=2) + 3*P(X=3)

E = (0 * conteo_X_0 + 1 * conteo_X_1 + 2 * conteo_X_2 + 3 * conteo_X_3) / N

print(f"E[X] = {E:.4f} (valor exacto 3/2 = 1.5000)")


#Cuando son monedas justas
#E[X] = n*p = n(1/2)