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

P, Q, R, S = symbols('P Q R S')

# P: Suelo seco
# Q: Temperatura alta
# R: Nivel de agua adecuado
# S: Sensor de lluvia activado

regla_riego = And(Or(And(P, Q), And(P, R)), Not(S))

tabla = truth_table(regla_riego, [P, Q, R, S])

for v in tabla:
    resultado = "bomba activada" if v[1] else "Bomba Apagada"
    print(f"{v[0]} -> {resultado}")

def evaluar_riego(suelo_seco, temp_alta, tanque_ok, lluvia):
    res = regla_riego.subs({P: suelo_seco, Q: temp_alta, R: tanque_ok, S: lluvia})
    return bool(res)

caso_1 = evaluar_riego(True, True, True, False)
print("Caso 1, Suelo seco, mucho calor, tanque adecuado y sin lluvia exterior:", "bomba activada" if caso_1 else "Bomba Apagada")

caso_2 = evaluar_riego(True, False, True, True)
print("Caso 2, Suelo seco, temperatura normal, tanque adecuado, pero lloviendo afueras:", "bomba activada" if caso_2 else "Bomba Apagada")

caso_3 = evaluar_riego(False, True, True, False)
print("Caso 3, Suelo húmedo, mucho calor, tanque adecuado y sin lluvia:", "bomba activada" if caso_3 else "Bomba Apagada")