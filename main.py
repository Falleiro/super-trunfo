import random


class Carta:
    def __init__(self, nome, comprimento, peso, gestacao, independencia, risco_extincao ):
        self.nome = nome
        self.comprimento = comprimento
        self.peso = peso
        self.gestacao = gestacao
        self.independencia = independencia
        self.risco_extincao = risco_extincao

    def __str__(self):
        return f'Nome: {self.nome} - Comprimento: {self.comprimento}cm - Peso: {self.peso}kg - Gestação: {self.gestacao} dias - Independência: {self.independencia} - Risco de Extinção: {self.risco_extincao}'


class Baralho:
    def __init__(self):
        self.cartas = []

        self.cartas.append(Carta("Cachorro Caramelo", 60, 18, 63, 60, 5))
        self.cartas.append(Carta("Leão", 200, 190, 110, 88, 20))
        self.cartas.append(Carta("Baleia azul", 2400, 150000, 360, 65, 40))
        self.cartas.append(Carta("Rinonceronte Branco", 400, 2300, 500, 30, 80))
        self.cartas.append(Carta("Camelo", 225, 500, 400, 99, 56))
        self.cartas.append(Carta("Gorila Africano", 150, 200, 257, 100, 30))

    def embaralhar(self):
        return random.shuffle(self.cartas)

    def pegar_carta(self):
        return self.cartas.pop()

    def __getitem__(self, item):
        return self.cartas[item]


baralho = Baralho()
baralho.embaralhar()

print('-----------------------------------------------------------------------------------------------------')
print('Cartas:')
for carta in baralho:
    print(carta)
print('-----------------------------------------------------------------------------------------------------\n')

carta_jogador = baralho.pegar_carta()
print('Voce pegou a carta {}'.format(carta_jogador))



