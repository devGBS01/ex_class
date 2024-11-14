class carro():
    def __init__(self, cor, velocidade, marcar):
        self.cor = cor
        self.velocidade = velocidade
        self.marcar = marcar
        
    def exibir_detalhes(self):
        print(f'o carro é {self.cor} ele é da marcar {self.marcar} e possui uma velocidade de {self.velocidade}')
        
        
carro = carro("amarelo", "213847k/s", "toyota")
carro.exibir_detalhes()