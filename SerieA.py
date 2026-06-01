# ============================================================
#  PROBLEMA A - Dados
#  MM3014 Teoría de Probabilidades - Parcial 4
# ============================================================

#  ESTRUCTURA GENERAL DEL EXPERIMENTO:
#  - Se define 2 dados justos de 6 caras cada uno

#  ============================================================
# CÓMO MODIFICAR EN EL PARCIAL
#
# 1) Cambiar el espacio muestral:
#    - más dados
#    - menos dados
#    - otra cantidad de caras
#
# 2) Cambiar el evento:
#    ejemplo:
#    suma == 7
#    suma > 8
#    ambos iguales
#
# 3) Cambiar condición (si es condicional):
#    ejemplo:
#    al menos uno par
#    ambos pares
#    al menos uno > 4

# ============================================================

# Parametros
import random
random.seed(2026)
N = 10000   # número de repeticiones (NO cambiar)

# Definir los dados
dado1 = [1, 2, 3, 4, 5, 6]
dado2 = [1, 2, 3, 4, 5,6]


# --------------------------------------------------------------
# a. Estimar la probabilidad de que la suma sea igual a 7

# Cosas de teoría ----------------------------------------------
# P(suma=7)

# Evento: E = { (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) }
# |E| = 6

# Espacio muestral: |S| = 36

# Valor exacto: P(E)=6/36=1/6≈0.1667

# Simulación: P(E) ≈ conteo / N

# Se tiran los dos dados y el resultado es al azar


# ---------------------------------------------------------------
#Para la suma 
conteo_suma_7 = 0

for _ in range(N):

    # Tirar los dados
    resultado_dado1 = random.choice(dado1)
    resultado_dado2 = random.choice(dado2)

    # Calcular la suma de los resultados
    suma = resultado_dado1 + resultado_dado2

    if suma == 7:
        conteo_suma_7 += 1

prob_suma_7 = conteo_suma_7 / N
print ("Inciso a:")
print(f"P(suma = 7) = {prob_suma_7:.4f}   "
      f"(valor exacto 6/36 ≈ 0.1667)")



#b. Estimar la probabilidad de que la suma sea igual a 7, dado que al menos uno de los dados es par 

# Esto es una condicional
#P(suma=7∣al menos uno es par) = veces que suma 7 y al menos uno es par / veces que al menos uno es par
#P(E|F) = P(E∩F) / P(F)

# E = { suma = 7 }
# F = { al menos uno es par }

# A = conteo de E∩F = conteo de veces que suma 7 y al menos uno es par
# B = conteo de F = conteo de veces que al menos uno es par

# Aproximación por simulación: P(E|F) ≈ A/B


# Inicializar los contadores
A= 0
B = 0

# Repetir el experimento N veces
for _ in range(N):

    # Tirar los dados
    resultado_dado1 = random.choice(dado1)
    resultado_dado2 = random.choice(dado2)

    # Calcular la suma de los resultados
    suma = resultado_dado1 + resultado_dado2


    # Verificar si al menos uno de los dados es par
    al_menos_uno_par = (resultado_dado1 % 2 == 0 or resultado_dado2 % 2 == 0 )

    if al_menos_uno_par:
        B += 1

        # Verificar si la suma es igual a 7
        if suma == 7:
            A += 1

# Calcular la probabilidad condicional
if B> 0:
    prob_condicional = A / B
else:
    prob_condicional = 0

print ("Inciso b:")
print(f"P(suma = 7 | al menos uno es par) = {prob_condicional:.4f}")