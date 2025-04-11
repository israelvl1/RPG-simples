import random
class Personagem: # Definição da classe Personagem
    def __init__(self, nome, vida, sexo):
        self.nome = nome        # Nome do personagem
        self.vida = vida        # Vida atual
        self.sexo = sexo        # Sexo do personagem
        self.pocoes = []  # lista que guarda tipos de poções
        self.max_pocoes = 8
        self.dano_max = 15  # dano base
        self.revive = True  # começa com a poção da fênix
        self.max_vida = vida

    def esta_vivo(self):
        self.vida = max(0, self.vida)  # Garante que a vida nunca fique negativa
        return self.vida > 0

    def atacar(self, inimigo): # método que atacar o inimigo
        if not self.esta_vivo(): # não atacar se o inimigo estiver morto
            print(f"{self.nome} não pode atacar porque foi derrotado.")
            return

        if not inimigo.esta_vivo():# não atacar se o inimigo tive sido derrotado
            print(f"{inimigo.nome} já está derrotado.")
            return

        dano = random.randint(1, self.dano_max) # atacar com chance de 1 a ao dano max
        chance = random.randint(1, 100)

        if chance <= 80:  # 80% de chance de acertar 
            inimigo.vida -= dano #itrar vida do inimigo
            inimigo.vida = max(0, inimigo.vida)  # evita que fique negativo
            print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!") 
        else: # caso erre o ataque
            print(f"{self.nome} errou o ataque contra {inimigo.nome}!")

        if not inimigo.esta_vivo(): # se o inimigo está vivo 
            print(f"{inimigo.nome} foi derrotado!")# se ele tiver morto
        else:# se ele estiver vivo
            print(f"{inimigo.nome} agora tem {inimigo.vida} de vida.\n")
    
            
    def tomar_pocao(self): #método para beber poção e recuperar vida
        if not self.pocoes: # caso não tenha poção
            print(f"{self.nome} não tem mais poções!")
            return
    
        tipo = self.pocoes.pop(0)  # pega a primeira poção da lista # as poções são divididas em tipo de raridade
    
        if tipo == "lendaria": # poção lendaria da 100 de vida
            cura = 100
        elif tipo == "poderosa":# poção poderosa da 50 de vida
            cura = 50
        elif tipo == "comum": # poção comum da 20 de vida
            cura = 20
        elif tipo == "misteriosa": # poção misteriosa devolve metade da vida total inicial
            cura = self.max_vida // 2
        else: # se não tiver for nenhum desses tipos, não dá vida de volta
            cura = 0

        self.vida += cura # dar mais vidade dependendo da poção
        print(f"{self.nome} tomou uma poção {tipo} e recuperou {cura} de vida!")
        print(f"Agora tem {self.vida} de vida.")
        print(f"Poções restantes: {len(self.pocoes)}\n")
         
    def tentar_ganhar_pocao(self): # método para achar poção
        chance = random.randint(1, 100) # de 1 a 100
        
        print(f"\n🔍 {self.nome} está explorando em busca de poções...") # procurar poção

        if chance <= 40: # tem 40% de não achar nada
            print(f"{self.nome} não encontrou nenhuma poção.")
            return

        if len(self.pocoes) >= self.max_pocoes: # se encontrar, mas o loot estiver cheio
            print(f"{self.nome} encontrou uma poção, mas já está com o máximo de {self.max_pocoes}.")
            return

        tipo_pocao = random.randint(1, 100)

        if tipo_pocao <= 10: # tem 10% de achar a lendaria
            self.pocoes.append("lendaria")
            print(f"{self.nome} encontrou uma 💎 poção lendária!")
        elif tipo_pocao <= 30:# tem 30% de achar a poderosa
            self.pocoes.append("poderosa")
            print(f"{self.nome} encontrou uma 🔥 poção poderosa!")
        elif tipo_pocao <= 60:# tem 60% de achar a comum
            self.pocoes.append("comum")
            print(f"{self.nome} encontrou uma 🧪 poção comum.")
        else:# excenção quando não ahcar nem comum, nem lendaria e nem poderosa
            self.pocoes.append("misteriosa")
            print(f"{self.nome} encontrou uma 🌙 poção misteriosa!")
            
        if not self.revive and random.randint(1, 100) <= 5:  #se não tiver mais a poção da fênix e procurar, mas só tem 5% de achar
            self.revive = True
            print(f"{self.nome} encontrou uma 🕊️ Poção da Fênix! Agora está protegido da morte novamente.")

            
    def encontrar_espada(self): # método que procurar uma espada
        chance = random.randint(1, 100)

        print(f"\n🔍 {self.nome} está explorando em busca de espadas...") # procurar espada 
        
        if chance <= 10: # 10 % de achar uma espada Lendária/Abençoada
            print(f"⬜ Você encontrou: Espada Negra (Lendária/Abençoada)!")
            print("Ela irradia poder... mas há algo especial nela.")
            self.dano_max += 50
            dano_vida = random.randint(10, 40)
            self.vida += dano_vida
            self.vida = max(0, self.vida)
            print(f"🌀 A benção deu {dano_vida} de vida!")
            print(f"❤️ Vida atual: {self.vida}")
        elif chance <= 20:# 20 % de achar uma espada Lendária/Maldita
            print(f"⬛ Você encontrou: Espada Negra (Lendária/Maldita)!")
            print("⚠️ Ela irradia poder... mas há algo sinistro nela.")
            self.dano_max += 40
            dano_maldicao = random.randint(10, 40)
            self.vida -= dano_maldicao
            self.vida = max(0, self.vida)
            print(f"💀 A maldição causou {dano_maldicao} de dano!")
            print(f"❤️ Vida atual: {self.vida}")

        elif chance <= 30:# 30 % de achar uma espada Épica
            print(f"🟪 Você encontrou: Espada Escura (Épica)!")
            self.dano_max += 30
            print("🗡️ Dano aumentado em +30!")

        elif chance <= 50:# 50 % de achar uma espada Rara
            print(f"🟦 Você encontrou: Espada Brilhante (Rara)!")
            self.dano_max += 20
            print("🗡️ Dano aumentado em +20!")

        elif chance <= 70:# 70 % de achar uma espada Comum
            print(f"🟫 Você encontrou: Espada Nova (Comum)!")
            self.dano_max += 10
            print("🗡️ Dano aumentado em +10!")

        else: #não encontra nenhuma
            print("🙁 Nenhuma espada foi encontrada dessa vez.")
                
    def ver_inventario(self): # método para ver o Inventário
        print(f"\n🎒 Inventário de {self.nome}:")
        
        if self.pocoes:#mostrar as poções que o user tem
            print(f"🧪 Poções disponíveis ({len(self.pocoes)}):") #mostrar as disponíveis
            for i, tipo in enumerate(self.pocoes, start=1):
                print(f"  {i}. Poção {tipo}")
        else:# se não tiver nenhuma
            print("🧪 Nenhuma poção no momento.")

        if self.revive: # se não tiver sido revivido
            print("🕊️ Poção da Fênix: DISPONÍVEL (revive o herói automaticamente)")
        else:# se tiver sido revivido
            print("🕊️ Poção da Fênix: já usada ou não encontrada")

        print("")  # linha em branco no final
    
