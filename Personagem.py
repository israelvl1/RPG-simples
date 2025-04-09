import random
class Personagem: # Definição da classe Personagem
    def __init__(self, nome, vida, sexo):
        self.nome = nome        # Nome do personagem
        self.vida = vida        # Vida atual
        self.sexo = sexo        # Sexo do personagem
        self.pocoes = 3  # número inicial de poções (ou o que preferir)
        self.max_pocoes = 8 # maxímo de poções
        self.dano_max = 15  # dano base

        
    def esta_vivo(self): # estr vivo só se a vida for maior que 0
        return self.vida > 0

    def atacar(self, inimigo): # atacar inimigo
        if not self.esta_vivo(): # se não tiver vivo não pode atacar mais
            print(f"{self.nome} não pode atacar porque foi derrotado.")
            return

        if not inimigo.esta_vivo(): # se o inimigo estiver morto, então não tem como atacar ele
            print(f"{inimigo.nome} já está derrotado.")
            return
        chance = random.randint(1, 100)  # Número entre 1 e 100
        if chance <= 60:  # 30% de chance
            dano = random.randint(1, self.dano_max) #jogar tipo um dado de 15 lados para dar um número de dano causado
            inimigo.vida -= dano # diminuir vida do inimigo
            print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")
        else:
            print(f"{self.nome} errou ataque contra {inimigo.nome}")
        if not inimigo.esta_vivo(): # se o inimigo estiver morto mostra que ele foi derrotado
            print(f"{inimigo.nome} foi derrotado!")
        else: #se não mostrar quanto de vida ele tem
            print(f"{inimigo.nome} agora tem {inimigo.vida} de vida.\n")
            
    def tomar_pocao(self): # o heroi pode tomar poção para recuperar vida
        if self.pocoes > 0: # se tiver poções
            cura = 20 # a cura é fixa de 20
            self.vida += cura  # cura pode ultrapassar a vida inicial
            self.pocoes -= 1 # diminuir o número de poções
            print(f"{self.nome} tomou uma poção e recuperou {cura} de vida!")
            print(f"Agora tem {self.vida} de vida (pode estar com bônus).") #a vida pode ultrapassar a quantidade vida original
            print(f"Poções restantes: {self.pocoes}\n") # mostra o número restante de poções
        else:
            print(f"{self.nome} não tem mais poções!")   #caso naõ tenha poçaõ     
            
    
    def tentar_ganhar_pocao(self): # o heroi tentar ganhar um poção
        chance = random.randint(1, 100)  # Número entre 1 e 100
        if chance <= 30:  # 30% de chance
            if self.pocoes < self.max_pocoes: # não pode ultrapassar o número maxímo de poções
                self.pocoes += 1 #adicionar mais um poção
                print(f"{self.nome} encontrou uma poção! Agora tem {self.pocoes}.")
            else: # caso chegue no maximo
                print(f"{self.nome} encontrou uma poção, mas já está com o máximo de {self.max_pocoes}.")
        else: # caso não encontre
            print(f"{self.nome} não encontrou nenhuma poção.")
            
    def encontrar_espada(self): # o heroi tentar achar uma espada
        chance = random.randint(1, 100)

        if chance <= 10: # 10% de chance
            print(f"{self.nome} encontrou uma espada negra... Ela parece poderosa, mas algo está errado!")
            self.dano_max += 40 #aumenta o dano do heroi
            dano_maldicao = random.randint(10, 40)
            self.vida -= dano_maldicao # dano da maldição
            print(f"A maldição da espada causou {dano_maldicao} de dano em {self.nome}!")
            if self.vida < 0:
                self.vida = 0
            print(f"Vida atual: {self.vida}")
        elif chance <= 20: # 20% de chance
            print(f"{self.nome} encontrou uma espada escura! Seu dano aumentou!")
            self.dano_max += 30
        elif chance <= 30: # 30% de chance
            print(f"{self.nome} encontrou uma espada brilhante! Seu dano aumentou!")
            self.dano_max += 20
        elif chance <= 50: # 50% de chance
            print(f"{self.nome} encontrou uma espada nova! Seu dano aumentou!")
            self.dano_max += 10
        else:
            print(f"{self.nome} não encontrou nenhuma espada.")
