# EJERCICIO 6: Sistema de Bloqueo de Transacciones Sospechosas (Pasarela de Pagos)
# 
# Descripción:
# Motor de reglas en tiempo real en Python para bloquear automáticamente
# transacciones sospechosas por sospecha de fraude antes de procesar el cobro.
# 
# Variables Proposicionales:
# P: La compra supera el monto límite habitual del cliente ($10,000 MXN)
# Q: La ubicación IP de la transacción no coincide con el país del tarjetahabiente
# R: Se detectaron más de 3 intentos fallidos de contraseña en los últimos 5 minutos
# S: La tarjeta está inscrita en el programa de autenticación reforzada 3D Secure (Verificada)
# 
# Regla del Negocio:
# "La transacción se bloqueará por sospecha de fraude si la compra supera el monto habitual y la
#  ubicación IP no coincide, o si existen más de 3 intentos fallidos de contraseña; A MENOS QUE la
#  tarjeta cuente con autenticación reforzada 3D Secure."

from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, truth_table

P, Q, R, S = symbols('P Q R S')

# P: Supera monto límite
# Q: IP no coincide
# R: Más de 3 intentos fallidos
# S: Cuenta con 3D Secure

regla_bloqueo = And(Or(And(P, Q), R), Not(S))

tabla = truth_table(regla_bloqueo, [P, Q, R, S])

for v in tabla:
    resultado = "TRANSACTION BLOQUEADA" if v[1] else "Transacción Permitida"
    print(f"{v[0]} -> {resultado}")

def evaluar_bloqueo(monto_alto, ip_no_coincide, intentos_fallidos, tiene_3d_secure):
    res = regla_bloqueo.subs({P: monto_alto, Q: ip_no_coincide, R: intentos_fallidos, S: tiene_3d_secure})
    return bool(res)

caso_1 = evaluar_bloqueo(True, True, False, False)
print("Caso 1, Monto alto, IP diferente, sin intentos fallidos y sin 3D Secure:", "TRANSACTION BLOQUEADA" if caso_1 else "Transacción Permitida")

caso_2 = evaluar_bloqueo(True, True, False, True)
print("Caso 2, Monto alto e IP diferente, pero la tarjeta tiene autenticación 3D Secure activa:", "TRANSACTION BLOQUEADA" if caso_2 else "Transacción Permitida")

caso_3 = evaluar_bloqueo(False, False, True, False)
print("Caso 3, Monto habitual e IP correcta, pero con más de 3 intentos fallidos y sin 3D Secure:", "TRANSACTION BLOQUEADA" if caso_3 else "Transacción Permitida")