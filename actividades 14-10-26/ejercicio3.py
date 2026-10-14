class AFD: 
    def __init__(self, Q, sigma, delta, q0, F):
        self.sigma = sigma  # alfabeto
        self.delta = delta  # funcion de la transicion 
        self.q0 = q0        # estado inicial
        self.F = F          # estados finales de aceptacion
        
    def procesar(self, cadena):
        estado_actual = self.q0
        for simbolo in cadena:
            if simbolo not in self.sigma:
                return False  # simbolo ilegal
            
            # transicion del estado tupla (estado_actual, simbolo)
            if (estado_actual, simbolo) in self.delta:
                estado_actual = self.delta[(estado_actual, simbolo)]
            else:
                return False  # si no hay transicion valida 
            
        return estado_actual in self.F  


# --- Ejercicio 2 (AFD Equivalente) ---

# 1. Quintupla del AFD
Q = {'q0', 'q1', 'q2'}  # conjunto de estados
sigma = {'a', 'b'}     # alfabeto

# Funcion de transicion
delta = {
    ('q0', 'a'): 'q1',  # Desde {1, 2} con 'a' pasa a {1, 2, 3}
    ('q0', 'b'): 'q2',  # Desde {1, 2} con 'b' no hay salida directa desde 1 ni 2 (rechaza)
    
    ('q1', 'a'): 'q1',  # Desde {1, 2, 3} con 'a' pasa a {1, 2, 3}
    ('q1', 'b'): 'q1',  # Desde {1, 2, 3} con 'b' pasa a {2, 3} (incluido en q1)
    
    ('q2', 'a'): 'q1',  # Desde {2} con 'a' pasa a {1, 2}
    ('q2', 'b'): 'q2'   
}

q0 = 'q0'              # Estado inicial {1, 2}
F = {'q0', 'q1', 'q2'}

# Construccion del AFD
mi_afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['', 'a', 'b', 'ab', 'ba', 'aab', 'bb']
print("-- Pruebas Ejercicio 2 --")
for cadena in cadenas:
    resultado = mi_afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = cadena if cadena != '' else 'ε (cadena vacía)'
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")