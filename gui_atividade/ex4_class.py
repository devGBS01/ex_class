class Animal():
        
    def emitir_som(self):
        pass

           
        
        
class Cachorro(Animal):
    def emitir_som(self):
       print("au au")
        
        
        
class Gato(Animal):
    def emitir_som(self):
       print("miau")
       
Cachorro = Cachorro()
gato = Gato()
Cachorro.emitir_som()
gato.emitir_som()