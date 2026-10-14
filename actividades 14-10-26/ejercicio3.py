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


# --- Ejercicio 3 (AFD Equivalente) ---

# 1. Quintupla del AFD
Q = {'q0', 'q1', 'q2', 'q_trampa'} # conjunto de estados
sigma = {'a', 'b'}                 # alfabeto

# Funcion de transicion
delta = {
    ('q0', 'a'): 'q1',          # Desde {0,1,4} con 'a' pasa a {2,3,5}
    ('q0', 'b'): 'q_trampa',
    
    ('q1', 'a'): 'q2',          # Desde {2,3,5} con 'a' pasa a {1,3,4}
    ('q1', 'b'): 'q_trampa',
    
    ('q2', 'a'): 'q1',          # Desde {1,3,4} con 'a' pasa a {2,3,5}
    ('q2', 'b'): 'q_trampa',
    
    ('q_trampa', 'a'): 'q_trampa',
    ('q_trampa', 'b'): 'q_trampa'
}

q0 = 'q0'           # Estado inicial {0, 1, 4}
F = {'q1', 'q2'}    # Estados de aceptacion (contienen a 3 o 5)

# Construccion del AFD
mi_afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['a', 'aa', 'aaa', 'aaaa', 'b', 'ab', '']
print("-- Pruebas Ejercicio 3 --")
for cadena in cadenas:
    resultado = mi_afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = cadena if cadena != '' else 'ε (cadena vacía)'
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")