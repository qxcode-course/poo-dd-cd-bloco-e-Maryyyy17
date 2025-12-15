from abc import ABC , abstractmethod

class Pagamento(ABC) :
    def __init__(self, valor : float , descricao : str) :
        self.__valor : float = valor
        self.__descricao : str = descricao

    def resumo (self) -> str :
        return f"Pagamento de R$ {self.__valor} : {self.__descricao}"

    def validar_Valor (self) :
        if self.__valor <= 0 :
            raise ValueError("falhou : valor inválido")

    @abstractmethod
    def processar (self) :
        pass

class CartaoDeCredito (Pagamento) :
    def __init__(self, num : int, nome : str, limite : float, valor : float, descricao : str) :
        super().__init__( valor, descricao)
        self.num : int = num
        self.nome : str = nome
        self.__limite : float = limite

    def resumo (self) :
        return f"Cartao de Crédito :" + super().resumo()

    def getLimite(self) -> float :
        return self.__limite

    def processar (self) :
        if self.__valor > self.__limite :
            print("pagamento recusado por limite insuficiente")
            return
        self.__limite-= self.__valor

def processar_pagamento (pagamentos : list[Pagamento]) :
    for i in pagamentos :
        i.validar_Valor()
        print(i.resumo())
        i.processar()
        if isinstance(i, CartaoDeCredito) :
            print(i.getLimite())

class Pix (Pagamento) :
    def __init__(self, valor : float, descricao : str, chave : str, banco : str) :
        super().__init__(valor, descricao)
        self.chave : str = chave
        self.banco : str = banco

    def processar(self) :
        print(f" PIX enviado via {self.banco} usando chave {self.chave}")


class Boleto (Pagamento) :
        def __init__(self, valor : float, descricao : str, codigoBarra : str, dataVencimento :int ) :
            super().__init__( valor, descricao)
            self.__codigoBarra : str = codigoBarra
            self.__dataVencimento : int = dataVencimento

        def getCodigo (self) -> str :
            return self.__codigoBarra

        def getVencimento (self) -> int :
            return self.__dataVencimento

        def processar (self) :
            if self.getVencimento() :
                print("Boleto gerado. Aguardando pagamento...")

pagamento = [Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO",), CartaoDeCredito( "1234 5678 9101 1121", "cliente M", 500,400, "Tenis esportivo"), Boleto(89.90, "livro de Python", "123456789000", 20250110)]

processar_pagamento(pagamento)

