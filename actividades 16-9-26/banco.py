# ==============================================================================
# ACTIVIDAD: SISTEMA DE VETO AUTOMÁTICO PARA CRÉDITO BANCARIO EN TIEMPO REAL
# ==============================================================================
# 
# DESCRIPCIÓN DEL PROBLEMA:
# Diseña un sistema de lógica proposicional que evalúe las solicitudes de
# crédito bancario en tiempo real.
# 
# REGLA DE NEGOCIO:
# Un cliente es APROBADO para un crédito si y solo si cumple TODAS las
# siguientes condiciones:
#   P: Sus ingresos mensuales son mayores a $15,000 MXN.
#   Q: Su historial crediticio en Buró es "Excelente".
#   R: Tiene una antigüedad laboral de al menos 1 año.
# 
# EXCEPCIÓN (VETO):
#   S: A MENOS QUE el cliente esté registrado en la Lista Negra de Fraude /
#      Lavado de Dinero (ALDF). Si se encuentra en esta lista, la solicitud
#      es RECHAZADA AUTOMÁTICAMENTE, independientemente de las demás condiciones.
# 
# INSTRUCCIONES:
# 1. Definir las variables proposicionales (P, Q, R, S).
# 2. Formular la expresión lógica para la aprobación del crédito.
# 3. Generar la tabla de verdad en Python usando 'sympy'.
# 4. Imprimir para cada caso si "Se otorgó el crédito" o "No se otorgó el crédito".
# 5. Demostrar la equivalencia lógica de las condiciones de denegación usando
#    las Leyes de De Morgan.
# ==============================================================================


from sympy import symbols, satisfiable
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent, truth_table, simplify_logic

P, Q, R, S = symbols('P Q R S')
# P: INGRESOS MAYORES A $15,000 MXN
# Q: HISTORIAL CREDITICIO EXCELENTE
# R: ANTIGÜEDAD LABORAL DE AL MENOS 1 AÑO
# S: REGISTRADO EN LISTA NEGRA DE FRAUDE

# Regla para otorgar el crédito: se aprueba si cumple P, Q y R, y NO está en S
regla_credito = And(P, Q, R, Not(S))
tabla = truth_table(regla_credito, [P, Q, R, S])

for v in tabla:
    # Comprobación similar a la de la presentación
    print("Se otorgó el crédito" if str(v[1]) == "True" else "No se otorgó el crédito")

# Equivalencia lógica de las condiciones de denegación
expA = Not(And(P, Q, R))
expB = Or(Not(P), Not(Q), Not(R))

son_equivalentes = Equivalent(expA, expB)
print(f"¿Son equivalentes?: {simplify_logic(son_equivalentes)}")