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


# --- Ejercicio 2 Corregido (AFD Equivalente) ---

# Estados del AFD:
# q0 = {1, 2}
# q1 = {1, 2, 3}
# q2 = {2}
# q3 = {2, 3}

Q = {'q0', 'q1', 'q2', 'q3', 'q_trampa'} 
sigma = {'a', 'b'}

delta = {
    # Desde q0 = {1, 2}:
    ('q0', 'a'): 'q1',         # Desde 1 va a 3 y desde 2 va a 1 (con epsilon va a 2) -> {1, 2, 3}
    ('q0', 'b'): 'q_trampa',   # Ni 1 ni 2 tienen salida directa con 'b'

    # Desde q1 = {1, 2, 3}:
    ('q1', 'a'): 'q1',         # Con 'a': de 1->3, de 2->1(2), de 3->2(1) -> {1, 2, 3}
    ('q1', 'b'): 'q3',         # Con 'b': de 3 tiene bucle a 3 y va a 2(1) -> {2, 3}

    # Desde q3 = {2, 3}:
    ('q3', 'a'): 'q1',         # Con 'a': de 2->1(2) y de 3->2(1) -> {1, 2, 3}
    ('q3', 'b'): 'q3',         # Con 'b': de 3 a 3 y a 2 -> {2, 3}

    ('q_trampa', 'a'): 'q_trampa',
    ('q_trampa', 'b'): 'q_trampa'
}

q0 = 'q0'    
F = {'q0', 'q1', 'q3'}  # Son de aceptación todos los que contienen al estado 2

# Construccion del AFD
mi_afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['', 'a', 'b', 'ab', 'ba', 'aab', 'bb']
print("-- Pruebas Ejercicio 2 (Corregido) --")
for cadena in cadenas:
    resultado = mi_afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = cadena if cadena != '' else 'ε (cadena vacía)'
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")