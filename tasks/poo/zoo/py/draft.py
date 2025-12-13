from abc import ABC, abstractmethod

class Animal :
    def __init__(self, name : str) :
        self.__name : str = name

    def mostrar_Nome (self) -> str :
        return f"Eu sou um(a) {self.__name}"

    def getName (self) -> str :
        return self.__name

    def setName (self, nome : str) :
        self.__name = nome

    @abstractmethod
    def fazer_som (self) :
        pass

    @abstractmethod
    def mover (self) :
        pass

class Lion (Animal) :
    def __init__(self, name : str) :
        super().__init__(name)

    def fazer_som(self) :
        print("ROARRRRRR")

    def mover(self) :
        print("TUM - TUM - TUM")

class Elephant (Animal) :
    def __init__(self, name : str) :
        super().__init__(name)

    def fazer_som(self) :
        print("FUMMMMMMMM")

    def mover (self) :
        print("BUM - BUM - BUM")

class Snake (Animal) :
    def __init__(self, name : str) :
        super().__init__(name)

    def fazer_som(self) :
        print("SSSSSSSSSS")

    def mover (self) :
        print("SSSSSSSSSSSSS")

def apresentar_animal (animal : Animal) :
    Animal.mostrar_Nome
    animal.fazer_som()
    animal.mover()

listaAnimal : list[Animal] = [Lion("Simba"), Elephant("Dumbo"), Snake("DJ")]
for i in listaAnimal :
    apresentar_animal(i)