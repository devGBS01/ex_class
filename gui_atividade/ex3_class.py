class ContaBancaria():
    def __init__(self, titular,  saldo=0):
        self.titular = titular
        self.__saldo = saldo
        
    def depositar(self, dinheiro):
        self.deposito = 0
        self.dinheiro = dinheiro
        self.__saldo += self.dinheiro
        
        

    def sacar (self, saque):
        self.saque = saque
        if self.saque > self.__saldo:
            print("não há saldo suficiente")
            
        else:
            self.__saldo = self.__saldo - self.saque
            print(f'o saldo está {self.__saldo}')
            
            
conta = ContaBancaria("guilherme")
conta.depositar(10000)
conta.sacar(500)
        
        
        
        