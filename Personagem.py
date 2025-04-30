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

    def atacar(self, inimigo):
        if not self.esta_vivo():
            print(f"{self.nome} não pode atacar porque foi derrotado.")
            return

        if not inimigo.esta_vivo():
            print(f"{inimigo.nome} já está derrotado.")
            return

        dano = random.randint(1, self.dano_max)
        chance = random.randint(1, 100)

        if chance <= 60:  # 60% de chance de acertar
            inimigo.vida -= dano
            inimigo.vida = max(0, inimigo.vida)  # evita que fique negativo
            print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")
        else:
            print(f"{self.nome} errou o ataque contra {inimigo.nome}!")

        if not inimigo.esta_vivo():
            print(f"{inimigo.nome} foi derrotado!")
        else:
            print(f"{inimigo.nome} agora tem {inimigo.vida} de vida.\n")


    def tomar_pocao(self):
        if not self.pocoes:
            print(f"{self.nome} não tem mais poções!")
            return

        tipo = self.pocoes.pop(0)  # pega a primeira poção da lista

        if tipo == "lendaria":
            cura = 100
        elif tipo == "poderosa":
            cura = 50
        elif tipo == "comum":
            cura = 20
        elif tipo == "misteriosa":
            cura = self.max_vida // 2
        else:
            cura = 0

        self.vida += cura
        print(f"{self.nome} tomou uma poção {tipo} e recuperou {cura} de vida!")
        print(f"Agora tem {self.vida} de vida.")
        print(f"Poções restantes: {len(self.pocoes)}\n")

    def tentar_ganhar_pocao(self):
        chance = random.randint(1, 100)

        print(f"\n🔍 {self.nome} está explorando em busca de poções...")

        if chance <= 40:
            print(f"{self.nome} não encontrou nenhuma poção.")
            return

        if len(self.pocoes) >= self.max_pocoes:
            print(f"{self.nome} encontrou uma poção, mas já está com o máximo de {self.max_pocoes}.")
            return

        tipo_pocao = random.randint(1, 100)

        if tipo_pocao <= 10:
            self.pocoes.append("lendaria")
            print(f"{self.nome} encontrou uma 💎 poção lendária!")
        elif tipo_pocao <= 30:
            self.pocoes.append("poderosa")
            print(f"{self.nome} encontrou uma 🔥 poção poderosa!")
        elif tipo_pocao <= 80:
            self.pocoes.append("comum")
            print(f"{self.nome} encontrou uma 🧪 poção comum.")
        else:
            self.pocoes.append("misteriosa")
            print(f"{self.nome} encontrou uma 🌙 poção misteriosa!")

        if not self.revive and random.randint(1, 100) <= 5:  # 5% de chance
            self.revive = True
            print(f"{self.nome} encontrou uma 🕊️ Poção da Fênix! Agora está protegido da morte novamente.")


    def encontrar_espada(self):
        chance = random.randint(1, 100)

        print(f"\n🔍 {self.nome} está explorando em busca de espadas...")
        if chance <= 1:
            print(f"⬜ Você encontrou: Espada Branca(Lendária/Abençoada)!")
            print("Ela irradia poder... mas há algo especial nela.")
            self.dano_max += 50
            dano_vida = random.randint(10, 40)
            self.vida += dano_vida
            self.vida = max(0, self.vida)
            print("🗡️ Dano aumentado em +50!")
            print(f"🌀 A benção deu {dano_vida} de vida!")
            print(f"❤️ Vida atual: {self.vida}")

        if chance <= 10:
            print(f"🟨 Você encontrou: Espada Negra (Lendária/Maldita)!")
            print("⚠️ Ela irradia poder... mas há algo sinistro nela.")
            self.dano_max += 40
            dano_maldicao = random.randint(10, 40)
            self.vida -= dano_maldicao
            self.vida = max(0, self.vida)
            print("🗡️ Dano aumentado em +40!")
            print(f"💀 A maldição causou {dano_maldicao} de dano!")
            print(f"❤️ Vida atual: {self.vida}")

        elif chance <= 20:
            print(f"🟪 Você encontrou: Espada Escura (Épica)!")
            self.dano_max += 30
            print("🗡️ Dano aumentado em +30!")

        elif chance <= 30:
            print(f"🟦 Você encontrou: Espada Brilhante (Rara)!")
            self.dano_max += 20
            print("🗡️ Dano aumentado em +20!")

        elif chance <= 50:
            print(f"🟫 Você encontrou: Espada Nova (Comum)!")
            self.dano_max += 10
            print("🗡️ Dano aumentado em +10!")

        else:
            print("🙁 Nenhuma espada foi encontrada dessa vez.")

    def ver_inventario(self):
        print(f"\n🎒 Inventário de {self.nome}:")

        if self.pocoes:
            print(f"🧪 Poções disponíveis ({len(self.pocoes)}):")
            for i, tipo in enumerate(self.pocoes, start=1):
                print(f"  {i}. Poção {tipo}")
        else:
            print("🧪 Nenhuma poção no momento.")

        if self.revive:
            print("🕊️ Poção da Fênix: DISPONÍVEL (revive o herói automaticamente)")
        else:
            print("🕊️ Poção da Fênix: já usada ou não encontrada")

        print("")  # linha em branco no final
