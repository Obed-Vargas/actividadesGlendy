class AFD: 
    def __init__(self, Q, sigma, delta, q0, F):
        self.sigma = sigma  # alfabeto
        self.delta = delta  # funcion de transicion 
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
                return False  # si no hay transicion valida (va a pozo/trampa)
            
        return estado_actual in self.F  


# --- Ejercicio 1 del PDF ---

# 1. Quintupla del AFD
Q = {'0', '1', '2', '3', '4'}  # conjunto de estados
sigma = {'a', 'b'}            # alfabeto

# Funcion de transicion basada en el diagrama
delta = {
    ('0', 'a'): '1',
    ('0', 'b'): '3',
    ('1', 'a'): '2',
    ('1', 'b'): '4',
    ('3', 'a'): '2',
    ('3', 'b'): '4'
}

q0 = '0'        # estado inicial
F = {'2', '4'}  # estados finales de aceptacion (doble circulo)

# Construccion del AFD
mi_afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['aa', 'ab', 'ba', 'bb', 'a', 'b', 'aaa', 'aba']
print("-- Pruebas Ejercicio 1 --")
for cadena in cadenas:
    resultado = mi_afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    print(f"La cadena '{cadena}' es {veredicto}.")