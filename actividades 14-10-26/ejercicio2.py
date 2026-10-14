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


# --- Ejercicio 2 (AFD Equivalente) ---

# 1. Quintupla del AFD
Q = {'q0', 'q1', 'q_trampa'} # conjunto de estados
sigma = {'a', 'b'}           # alfabeto

# Funcion de transicion
delta = {
    ('q0', 'a'): 'q1',         # Con 'a' se llega al estado 3 (q1)
    ('q0', 'b'): 'q1',         # Con 'b' se llega al estado 3 (q1)
    ('q1', 'a'): 'q_trampa',   # Desde el estado 3 no hay salida con 'a'
    ('q1', 'b'): 'q1',         # Con 'b' tiene bucle en el estado 3
    ('q_trampa', 'a'): 'q_trampa',
    ('q_trampa', 'b'): 'q_trampa'
}

q0 = 'q0'    # representa {1, 2}
F = {'q0'}   # es de aceptacion por incluir al estado 2

# Construccion del AFD
mi_afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['', 'a', 'b', 'ab', 'bb', 'aab', 'bba']
print("-- Pruebas Ejercicio 2 (con sintaxis AFD) --")
for cadena in cadenas:
    resultado = mi_afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = cadena if cadena != '' else 'ε (cadena vacía)'
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")