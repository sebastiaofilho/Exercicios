class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def Nome(self, nome):
        self.nome = nome
        return nome

    def Fome(self, comida):
        self.fome -= comida
        return self.fome

    def Saude(self, pontos):
        self.saude += pontos
        return self.saude

    def Idade(self, ano):
        self.idade += ano
        return self.idade

    def Humor(self):
        Humor = 50 + self.saude - self.fome
        return Humor


tama = Tamagushi("Tata", 50, 100, 5)
tama.Saude(-50)
tama.Fome(30)
Humor = tama.Humor()
print(tama.fome)
print(tama.saude)
print(Humor)
print(tama.nome)