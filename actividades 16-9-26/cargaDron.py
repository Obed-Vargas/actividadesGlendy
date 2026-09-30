from sympy import symbols, satisfiable
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent, truth_table, simplify_logic

P, Q, R, S = symbols('P Q R S')
#P CARGA DE BATERÍA
#Q ALTURA DEL DRON
#R ZONA DESPEJADA
#S BOTÓN DE EMERGENCIA

regla_drone = And(P, Q, R, Not(S))
tabla = truth_table(regla_drone, [P, Q, R, S])

for v in tabla:
    #print(f"{v[0]} -> Resultado: {v[1]}")
    print("Carga liberada" if v[1] == "True" else "Carga no liberada")

# liberación de la carga del dron

expA = Not(And(P, Q))
expB = Or(Not(P), Not(Q))

son_equivalentes = Equivalent(expA, expB)
print(f"¿Son equivalentes?: {simplify_logic(son_equivalentes)}")