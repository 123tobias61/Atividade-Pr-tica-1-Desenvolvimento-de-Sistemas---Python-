class Anao:
    def __init__(self, tamanho, etnia, origem, preco, nome, personalidade):
        self.__tamanho = tamanho,
        self.__etnia = etnia,
        self.__origem = origem,
        self.__preco = preco,
        self.__nome = nome,
        self.__personalidade = personalidade,
        
    @property
    def nome(self):
        if self.__nome == "":
            return"Zé ninguem"
        else:
            return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome