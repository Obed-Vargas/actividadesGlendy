class AFD: 
    def __init__(self, Q, sigma, delta, q0, F):
        self.sigma = sigma # alfabeto
        self.delta = delta # funcion de la transicion 
        self.q0 = q0       # estado inicial
        self.F = F         # estados finales de aceptacion
        
    def procesar(self, cadena):
        estado_actual = self.q0
        for simbolo in cadena:
            if simbolo not in self.sigma:
                return False # simbolo ilegal
            
            # transicion del estado tupla (estado_actual, simbolo)
            if (estado_actual, simbolo) in self.delta:
                estado_actual = self.delta[(estado_actual, simbolo)]
            else:
                return False # si no hay transicion valida 
            
        return estado_actual in self.F  


# --- Ejercicio 5 (AFD Equivalente) ---

# 1. Quintupla del AFD
Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q_trampa'} # conjunto de estados
sigma = {'0', '1'}                                  # alfabeto

# Funcion de transicion
delta = {
    ('q0', '0'): 'q2',         # Desde {A} con '0' va a {B}
    ('q0', '1'): 'q1',         # Desde {A} con '1' va a {B, C}
    
    ('q1', '0'): 'q3',         # Desde {B, C} con '0' va a {B, C, D}
    ('q1', '1'): 'q4',         # Desde {B, C} con '1' va a {E}
    
    ('q2', '0'): 'q5',         # Desde {B} con '0' va a {C, D}
    ('q2', '1'): 'q4',         # Desde {B} con '1' va a {E}
    
    ('q3', '0'): 'q5',         # Desde {B, C, D} con '0' va a {B, C, D}
    ('q3', '1'): 'q3',         # Desde {B, C, D} con '1' va a {B, E}
    
    ('q4', '0'): 'q5',         # Desde {E} con '0' va a {D}
    ('q4', '1'): 'q5',         # Desde {E} con '1' va a {D}
    
    ('q5', '0'): 'q5',         # Ciclo de transiciones internas
    ('q5', '1'): 'q2',
    
    ('q_trampa', '0'): 'q_trampa',
    ('q_trampa', '1'): 'q_trampa'
}

q0 = 'q0'                         # Estado inicial {A}
F = {'q1', 'q3', 'q4', 'q5'}      # Estados finales (contienen a C o E)

# Construccion del AFD
mi_afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['1', '01', '00', '10', '11', '000', '1010']
print("-- Pruebas Ejercicio 5 --")
for cadena in cadenas:
    resultado = mi_afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = cadena if cadena != '' else 'ε (cadena vacía)'
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")