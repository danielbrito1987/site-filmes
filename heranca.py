class Pai():
    def __init__(self, sobrenome, cor_olhos):
        print("Construtor da Classe Pai")
        self.sobrenome = sobrenome
        self.cor_olhos = cor_olhos

    def show_info(self):
        print("Sobrenome - " + self.sobrenome)
        print("Cor dos Olhos - " + self.cor_olhos)

class Filho(Pai):
    def __init__(self, sobrenome, cor_olhos, num_brinquedos):
        print("Construtor da Classe Filho")
        Pai.__init__(self, sobrenome, cor_olhos)
        self.num_brinquedos = num_brinquedos

    def show_info(self):
        print("Sobrenome - " + self.sobrenome)
        print("Cor dos Olhos - " + self.cor_olhos)
        print("Numero de Brinquedos - " + str(self.num_brinquedos))

daniel_brito = Pai("Brito", "Marrom")
#daniel_brito.show_info()

julia_brito = Filho("Brito", "Castanho", 4)
julia_brito.show_info()
#print(julia_brito.sobrenome)
#print(julia_brito.num_brinquedos)
