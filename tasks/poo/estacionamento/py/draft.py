from abc import ABC, abstractmethod

class Veiculo (ABC) :
    def __init__(self, id : str, tipo : str, horaEntrada : int) :
        self.__id : str = id
        self.tipo : str = tipo
        self.horaEntrada : int = horaEntrada

    def getEntrada (self) -> int :
        return self.horaEntrada
    
    def setEntrada (self, hora : int) :
        self.horaEntrada = hora

    def getTipo (self) -> str :
        return self.tipo
    
    def getId (self) -> str :
        return self.__id
    
    @abstractmethod 
    def calcularValor(self, saida : int) :
        pass

class Estacionamento(Veiculo) :
    def __init__(self, id : str, tipo : str, horaEntrada : int,) :
        super().__init__(id, tipo, horaEntrada)
        self.veiculo : list[Veiculo] = []
        self.horaAtual : int = 0
    
    def procurarVeiculo (self, id : str) :
        for i in self.veiculo :
            if i.getId == id :
                print (i)

    def estacionar (self, veiculo : Veiculo) :
        self.veiculo.append(veiculo)
        veiculo.setEntrada(self.horaAtual)

    def pagar (self,  : str) :
        