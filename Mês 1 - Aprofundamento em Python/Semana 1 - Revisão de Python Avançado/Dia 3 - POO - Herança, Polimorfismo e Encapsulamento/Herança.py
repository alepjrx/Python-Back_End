'''
Herança -
 - Permite que uma classe (filha) herde atributos e métodos de outra classe (pai)
 - Evita a repetição de código e melhora a organização
'''

class Animal: #criada a classe base, servirá como superclasse para outras classes que herdarão suas características
    def __init__(self,nome):
        self.nome = nome #self se refere ao próprio objeto, e self.nome = nome significa que estamos armazenando o valor passado como argumento no atributo nome

    def fazer_som(self): #criado um método chamado fazer_som
        pass #significa que esse método não irá fazer nada na classe animal, e será sobrescrito (redefinido) nas classes filhas

class Cachorro(Animal): #criada a classe filha "Cachorro" que herda de animal. O (Animal) indica que Cachorro herda todos os atributos e métodos de Animal
    def fazer_som(self): #sobrescrevemos o método fazer_som(), que agora retorna "Au au!" quando chamado. Como animal não possuía implementação para esse método, agora Cachorro tem um comportamento específico
        return "Au au!"

meu_cachorro = Cachorro('Rex') #criamos um objeto da classe Cachorro chamado meu_cachorro. O valor "Rex" é passado para o construtor __init__ da classe Animal, pois Cachorro herdou esse método
print(meu_cachorro.fazer_som()) #chamamos o método fazer_som() do objeto meu_cachorro. Como cachorro sobrescreveu esse método, ele retorna "Au au!"

'''
Resumo do funcionamento da Herança:
 - Cachorro herda o atributo (nome) de (Animal)
 - Cachorro sobrescreve o método (fazer_som()), definindo um comportamento específico
 - Criamos um objeto Cachorro('Rex') e ele pode usar os atributos herdados (nome) e os métodos sobrescritos (fazer_som())
'''