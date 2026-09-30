# EJERCICIO 5: Sistema de Control de Bomba de Riego Hidropónico
# 
# Descripción:
# Motor de reglas determinista en Python para la activación de una bomba
# de riego basado en la humedad del suelo, temperatura, nivel de agua
# en el tanque de reserva y sensor de lluvia exterior.
# 
# Variables Proposicionales:
# P: La humedad del suelo es inferior al 30% (Suelo seco)
# Q: La temperatura ambiente es superior a 30°C (Mucho calor)
# R: El nivel de agua en el tanque de reserva es adecuado
# S: Sensor de lluvia exterior activado (Está lloviendo)
# 
# Regla del Negocio:
# "El sistema activará la bomba de riego si el suelo está seco y la temperatura
#  es alta, o si el suelo está seco y el tanque tiene nivel de agua adecuado;
#  SIEMPRE Y CUANDO el sensor de lluvia exterior no esté activado."

from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, truth_table

# 1. Modelado SymPy - Declaración de Símbolos
P, Q, R, S = symbols('P Q R S')

# 2. Construcción de la Regla de Activación de Riego
regla_riego = And(Or(And(P, Q), And(P, R)), Not(S))

# 3. Generación de la Tabla de Verdad (16 combinaciones posibles)
print("=== TABLA DE VERDAD ===")
tabla = truth_table(regla_riego, [P, Q, R, S])

for v in tabla:
    resultado = "¡BOMBA ACTIVADA!" if v[1] else "Bomba Apagada"
    print(f"{v[0]} -> {resultado}")

# 4. Función de Evaluación en Tiempo Real
def evaluar_riego(suelo_seco, temp_alta, tanque_ok, lluvia):
    """
    Evalúa la regla de negocio sustituyendo los valores booleanos en la fórmula simbólica.
    """
    res = regla_riego.subs({P: suelo_seco, Q: temp_alta, R: tanque_ok, S: lluvia})
    return bool(res)

# 5. Ejecución de Casos de Prueba
print("\n=== CASOS DE PRUEBA ===")

# Caso A: Suelo seco y temperatura alta, tanque no adecuado, sin lluvia
caso_a = evaluar_riego(True, True, False, False)
print("Caso A:", "¡BOMBA ACTIVADA!" if caso_a else "Bomba Apagada")

# Caso B: Suelo seco y tanque adecuado, pero está lloviendo
caso_b = evaluar_riego(True, False, True, True)
print("Caso B:", "¡BOMBA ACTIVADA!" if caso_b else "Bomba Apagada")

# Caso C: Suelo húmedo (no seco), temperatura alta y tanque adecuado, sin lluvia
caso_c = evaluar_riego(False, True, True, False)
print("Caso C:", "¡BOMBA ACTIVADA!" if caso_c else "Bomba Apagada")