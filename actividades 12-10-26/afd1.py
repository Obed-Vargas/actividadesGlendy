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
    
    
    #AFD que solo acepta la palabra "01"
    #1. Quintupla del AFD
    Q={'q0', 'q1', 'q2', 'q_trampa'} # conjunto de estados
    sigma={'0', '1'} # alfabeto
    #funcion de la funcion
    
    delta={
        ('q0', '0'): 'q1',      #avanza a q1
        ('q0', '1'): 'q_trampa',
        ('q1', '0'): 'q_trampa', 
        ('q1', '1'): 'q2',      #avanza a q2
        ('q2', '0'): 'q_trampa',
        ('q2', '1'): 'q_trampa',
        ('q_trampa', '0'): 'q_trampa',
        ('q_trampa', '1'): 'q_trampa'
    }
    
    q0='q0' # estado inicial
    F={'q2'} # conjunto final de aceptacion