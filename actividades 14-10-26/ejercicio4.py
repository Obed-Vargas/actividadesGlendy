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


# --- Ejercicio 4 Corregido (AFD Equivalente) ---

# Mapeo de conjuntos de estados:
# q0 = {1, 2}
# q1 = {1, 2, 3}
# q2 = {2, 3}
# q3 = {2, 3, 4} (Aceptacion por contener a 4)
# q4 = {4}       (Aceptacion)

Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q_trampa'}
sigma = {'a', 'b'}

delta = {
    # Desde q0 = {1, 2}:
    ('q0', 'a'): 'q1',         # Pasa a {1, 2, 3}
    ('q0', 'b'): 'q2',         # Pasa a {2, 3}
    
    # Desde q1 = {1, 2, 3}:
    ('q1', 'a'): 'q1',         # Mantiene {1, 2, 3}
    ('q1', 'b'): 'q3',         # Pasa a {2, 3, 4}
    
    # Desde q2 = {2, 3}:
    ('q2', 'a'): 'q_trampa',   # Ni 2 ni 3 tienen salida con 'a'
    ('q2', 'b'): 'q3',         # Pasa a {2, 3, 4}
    
    # Desde q3 = {2, 3, 4}:
    ('q3', 'a'): 'q4',         # Solo el estado 4 responde a 'a' (bucle en 4) -> {4}
    ('q3', 'b'): 'q3',         # Permanece en {2, 3, 4}
    
    # Desde q4 = {4}:
    ('q4', 'a'): 'q4',         # Bucle en 4
    ('q4', 'b'): 'q_trampa',   # El estado 4 no tiene salida con 'b'
    
    ('q_trampa', 'a'): 'q_trampa',
    ('q_trampa', 'b'): 'q_trampa'
}

q0 = 'q0'              # Estado inicial {1, 2}
F = {'q3', 'q4'}       # Estados de aceptacion (los que contienen al estado 4)

# Construccion del AFD
mi_afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['bb', 'abb', 'bbb', 'bba', 'abbaa', 'a', 'b', 'ba']
print("-- Pruebas Ejercicio 4 --")
for cadena in cadenas:
    resultado = mi_afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = cadena if cadena != '' else 'ε (cadena vacía)'
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")