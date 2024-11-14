class pessoa():
    def __init__ (self, nome, idade):
        self.idade = int(idade)
        self.nome = str(nome)
        
    def exibir_informacoes(self):
        print(f'seu nome é {self.nome}')
        print(f'sua idade é{self.idade}')
        
        
pessoa = pessoa("guilherme", 14)
pessoa.exibir_informacoes()        