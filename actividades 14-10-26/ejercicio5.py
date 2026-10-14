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


# --- Ejercicio 5 (AFD Directo) ---

# 1. Quintupla del AFD
Q = {'A', 'B', 'C', 'D', 'E'}  # conjunto de estados
sigma = {'0', '1'}             # alfabeto

# Funcion de transicion exacta del diagrama
delta = {
    ('C', '0'): 'D',
    ('C', '1'): 'A',
    
    ('A', '0'): 'B',
    ('A', '1'): 'B',
    
    ('B', '0'): 'C',
    ('B', '1'): 'E',
    
    ('D', '0'): 'B',
    ('D', '1'): 'B',
    
    ('E', '0'): 'D',
    ('E', '1'): 'D'
}

q0 = 'C'        # Estado inicial (indicado por la flecha)
F = {'C', 'E'}  # Estados finales de aceptacion (doble circulo)

# Construccion del AFD
mi_afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['', '10', '01', '100', '011', '110', '000']
print("-- Pruebas Ejercicio 5 --")
for cadena in cadenas:
    resultado = mi_afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = cadena if cadena != '' else 'ε (cadena vacía)'
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")