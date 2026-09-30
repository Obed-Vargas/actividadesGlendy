#Instrucciones: Escribe la solución del siguiente problema en tu entorno de desarrollo (VS Code / Google Colab) e integra las capturas de pantalla o entrega el archivo .py / .ipynb correspondiente

#Problema: Sistema de Control de Acceso a Centro de Datos de Alta Seguridad
#Una firma de infraestructura en la nube te solicita programar un motor de reglas determinista en Python utilizando la librería sympy.logic.

#Regla del Negocio:
#Un empleado obtendrá acceso físico a la sala de servidores (A) si cumple con:

#Poseer una Tarjeta RFID Válida (P)
#Y pasar la Verificación Biométrica (Q)
#O bien poseer una Clave de Maestro SuperAdmin (R)
#A MENOS QUE se haya activado el Protocolo de Bloqueo de Emergencia (S).
#Requerimientos del Código:
#Modelado SymPy (10 Pts): Importa los módulos de sympy, declara los símbolos P, Q, R, S y construye la fórmula simbólica de la regla de acceso (regla_acceso).
#Tabla de Verdad (10 Pts): Genera e imprime en consola la tabla de verdad completa (2^4 = 16 combinaciones). El programa debe imprimir la frase "¡ACCESO CONCEDIDO!" únicamente cuando la combinación de entrada resulte verdadera.
#Función de Evaluación en Tiempo Real (10 Pts): Diseña la función evaluar_acceso(rfid, bio, super_key, emergencia) que reciba valores booleanos, reemplace en la fórmula simbólica usando .subs() y retorne True o False.
#Casos de Prueba Obligatorios (10 Pts): Ejecuta la función con los siguientes 3 escenarios e imprime el veredicto en consola:
#- Caso A: Empleado con RFID válida y Biometría correcta, sin clave SuperAdmin y sin emergencia activa.
#- Caso B: SuperAdmin ingresando con su Clave de Maestro sin RFID ni Biometría, pero con el Protocolo de Emergencia activado.
#- Caso C: Usuario con RFID válida, pero fallando la verificación biométrica y sin clave SuperAdmin.

from sympy import symbols, satisfiable
from sympy.logic.boolalg import And, Or, Not, truth_table

P, Q, R, S = symbols('P Q R S')


#tabla de verdad
regla_acceso = And(Or(And(P, Q), R), Not(S))

tabla = truth_table(regla_acceso, [P, Q, R, S])
 
for v in tabla:
    resultado = "ACCESO CONCEDIDO" if v[1] else "Acceso Denegado"
    print(f"{v[0]} -> {resultado}")
    

#evaluar_acceso    
def evaluar_acceso(rfid, bio, super_key, emergencia):
    res = regla_acceso.subs({P: rfid, Q: bio, R: super_key, S: emergencia})
    return bool(res)
    
#casos de prueba
# Caso A: RFID válida, Biometría correcta, sin SuperAdmin, sin emergencia
caso_a = evaluar_acceso(True, True, False, False)
print("Caso A:", "¡ACCESO CONCEDIDO!" if caso_a else "Acceso Denegado")

# Caso B: SuperAdmin sin RFID ni Biometría, pero con Emergencia activada
caso_b = evaluar_acceso(False, False, True, True)
print("Caso B:", "¡ACCESO CONCEDIDO!" if caso_b else "Acceso Denegado")

# Caso C: RFID válida, falla Biometría, sin SuperAdmin
caso_c = evaluar_acceso(True, False, False, False)
print("Caso C:", "¡ACCESO CONCEDIDO!" if caso_c else "Acceso Denegado")