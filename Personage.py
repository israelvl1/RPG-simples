import random
from Xp import *

class Personagem: # Definição da classe Personagem
    def __init__(self, nome, vida, sexo, classe,nivel=1, xp_atual=0):
        self.nome = nome        # Nome do personagem
        self.vida = vida        # Vida atual
        self.sexo = sexo        # Sexo do personagem
        self.classe = classe    # classe do personagem 
        self.classe_inicial = self.definir_classe_inicial()
        self.pocoes = []  # lista que guarda tipos de poções
        self.max_pocoes = 8
        self.arma = []
        # 🎯 Definindo quantas armas pode carregar com base na classe
        if self.classe_inicial == "Assassino" or self.classe_inicial == "Arqueiro" or self.classe_inicial == "Cavaleiro":
            self.max_arma = 2  # Pode equipar 2 armas!
        else:
            self.max_arma = 1  # Padrão: 1 arma
        if self.classe_inicial == "Monge":
            self.ki = self.defini_ki()
        if self.classe_inicial == "Mago" or self.classe_inicial == "Feiticeiro" or self.classe_inicial == "Bruxo" or self.classe_inicial == "Bardo" self.classe_inicial == "Druida":
            self.mana = self.defini_mana()
        if self.classe_inicial == "Cavaleiro" or self.classe_inicial == "Berserker" or self.classe_inicial == "Arqueiro" or self.classe_inicial == "Assassino":  
            self.aura = self.defini_aura()
        if self.classe_inicial == "Clérigo":
            self.energia_divina == self.defini_energia_divina()
        self.dinheiro = self.definir_dinheiro()
        self.nivel = 1
        self.xp_atual = xp_atual
        self.moral = []  # Lista que mantém as ações de moral (pode ser positiva ou negativa)
        self.max_moral = 10  # O máximo que a moral pode atingir
        self.pontos_positivos = 0  # Quantidade de pontos positivos acumulados
        self.pontos_negativos = 0  # Quantidade de pontos negativos acumulados
        self.corrompido = False  # Se o personagem está corrompido ou não
        self.iluminado = False
        self.faltando_para_proximo_nivel = calcular_faltando(self.nivel, self.xp_atual)
        self.quantidade_max_xp = calcular_xp_max(self.nivel)
        self.dano_max =  self.definir_dano() # dano base
        self.revive = self.definir_revive() #não começa com a poção da fênix
        self.max_vida = vida
        self.envenenado = False
        self.queimado = False
        self.corrosivo = False
        self.visao_noturna = False
        self.classe_incompativeis = {
            "Cavaleiro": ["Arqueiro", "Mago", "Berserker", "Bruxo", "Feiticeiro", "Monge", "Bardo", "Druida", "Engenheiro", "Clérigo", "Assassino"],
            "Mago": ["Arqueiro", "Cavaleiro", "Berserker", "Bruxo", "Feiticeiro", "Monge", "Bardo", "Druida", "Engenheiro", "Clérigo", "Assassino"],
            "Arqueiro": ["Cavaleiro", "Mago", "Berserker", "Bruxo", "Feiticeiro", "Monge", "Bardo", "Druida", "Engenheiro", "Clérigo", "Assassino"],
            "Monge": ["Arqueiro", "Mago", "Berserker", "Bruxo", "Feiticeiro", "Cavaleiro", "Bardo", "Druida", "Engenheiro", "Clérigo", "Assassino"],
            "Feiticeiro": ["Arqueiro", "Mago", "Berserker", "Bruxo", "Cavaleiro", "Monge", "Bardo", "Druida", "Engenheiro", "Clérigo", "Assassino"],       
            "Berserker": ["Arqueiro", "Mago", "Cavaleiro", "Bruxo", "Feiticeiro", "Monge", "Bardo", "Druida", "Engenheiro", "Clérigo", "Assassino"],
            "Bardo": ["Arqueiro", "Mago", "Berserker", "Bruxo", "Feiticeiro", "Monge", "Cavaleiro", "Druida", "Engenheiro", "Clérigo", "Assassino"],
            "Druida": ["Arqueiro", "Mago", "Berserker", "Bruxo", "Feiticeiro", "Monge", "Bardo", "Cavaleiro", "Engenheiro", "Clérigo", "Assassino"],
            "Assassino": ["Arqueiro", "Mago", "Berserker", "Bruxo", "Feiticeiro", "Monge", "Bardo", "Druida", "Engenheiro", "Clérigo", "Cavaleiro"],
            "Clérigo": ["Arqueiro", "Mago", "Berserker", "Bruxo", "Feiticeiro", "Monge", "Bardo", "Druida", "Engenheiro", "Cavaleiro", "Assassino"],
            "Bruxo": ["Arqueiro", "Mago", "Berserker", "Cavaleiro", "Feiticeiro", "Monge", "Bardo", "Druida", "Engenheiro", "Clérigo", "Assassino"],
            "Engenheiro": ["Arqueiro", "Mago", "Berserker", "Bruxo", "Feiticeiro", "Monge", "Bardo", "Druida", "Cavaleiro", "Clérigo", "Assassino"]
        }
        self.

        def tentar_multiclassificar(self, nova_classe):
            """
            Tenta mudar a classe do personagem, mas com caminhos limitados por sua classe inicial.
            """
            if nova_classe in self.classe_incompativeis.get(self.classe_inicial, []):
                print(f"Você não pode mudar porque a classe inicial é {self.classe_inicial} diferente da classe inicial da sua nova classe {nova_classe}!")
            else:
                self.classe = nova_classe
                print(f"{self.nome} agora é {self.classe}!")
    
        def status(self):
            print(f"{self.nome} está no nível {self.nivel} e é {self.classe}.")
        
        
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
            elif tipo == "estranha":
                chance = random.randint(1, 100)
                if chance <= 20:
                    print(f"{self.nome} tomou uma poção mais sentiu um gosto ácido ✳️")
                    self.aplicar_acido
                elif chance <= 50:
                    print(f"{self.nome} tomou veneno sem saber")
                    self.aplicar_veneno
                else: 
                    print(f"{self.nome} tomou um poção de força 💪")
                    self.dano_max += 10
            else: # se não tiver for nenhum desses tipos, não dá vida de volta
                cura = 0

            self.vida += cura # dar mais vidade dependendo da poção
            print(f"{self.nome} tomou uma poção {tipo} e recuperou {cura} de vida!")
            print(f"Agora tem {self.vida} de vida.")
            print(f"Poções restantes: {len(self.pocoes)}\n")
            
        def aplicar_veneno(self, turnos=None):
            self.envenenado = True
            if turnos is None:
                self.turnos_veneno = None  # Permanente
                print(f"{self.nome} foi envenenado PERMANENTEMENTE! 😵 Sofrerá dano contínuo.")
            else:
                self.turnos_veneno = turnos
                print(f"{self.nome} foi envenenado! 😵")
        
        def aplicar_queimadura
        def aplicar_acido(self):
            self.corrosivo = True
            print(f"{self.nome} bebeu Ácido! 💀")
            
        def sofrer_efeitos_acido(self,):
            if self.corrosivo:
                dano = -self.max_vida
                print(f"{self.nome} bebeu ácido e morreu sendo corroido pelo ácido de dentro para fora!")
            
        def sofrer_efeitos(self):
            if self.envenenado:
                dano = 5
                self.vida -= dano
                print(f"{self.nome} sofre {dano} de dano por veneno!")
                if self.turnos_veneno is not None:
                    self.turnos_veneno -= 1
                    if self.tomar_pocao:
                        self.envenenado = False
                        print(f"{self.nome} não está mais envenenado.")
                else: 
                     print(f"{self.nome} sofre {dano} de dano por veneno PERMANENTE! 💀")
                     if self.tomar_pocao:
                        self.envenenado = False
                        print(f"{self.nome} não está mais envenenado.")
                        
        def sofrer_efeitos(self, inimigo):
            # Efeito de veneno no personagem
            if self.envenenado:
                dano = 5
                self.vida -= dano
                print(f"{self.nome} sofre {dano} de dano por veneno! (restam {self.turnos_veneno} turnos)")
                if self.turnos_veneno is not None:
                    self.turnos_veneno -= 1
                    if self.tomar_pocao:
                        self.envenenado = False
                        print(f"{self.nome} não está mais envenenado.")
                else: 
                     print(f"{self.nome} sofre {dano} de dano por veneno PERMANENTE! 💀")
                     if self.tomar_pocao:
                        self.envenenado = False
                        print(f"{self.nome} não está mais envenenado.")

            # Efeito de veneno no inimigo (caso ele também possa ser envenenado)
            if hasattr(inimigo, 'envenenado') and inimigo.envenenado:
                dano = 5
                inimigo.vida -= dano
                inimigo.turnos_veneno -= 1
                print(f"{inimigo.nome} sofre {dano} de dano por veneno! (restam {inimigo.turnos_veneno} turnos)")
                if inimigo.turnos_veneno <= 0:
                    inimigo.envenenado = False
                    print(f"{inimigo.nome} não está mais envenenado.")      
        
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
                self.pocoes.append("estranha")
                print(f"{self.nome} encontrou uma 🧿 poção estranha!")
            elif tipo_pocao <= 30: # tem 30% de achar a lendaria
                self.pocoes.append("lendaria")
                print(f"{self.nome} encontrou uma 💎 poção lendária!")
            elif tipo_pocao <= 60:# tem 60% de achar a poderosa
                self.pocoes.append("poderosa")
                print(f"{self.nome} encontrou uma 🔥 poção poderosa!")
            elif tipo_pocao <= 80:# tem 80% de achar a comum
                self.pocoes.append("comum")
                print(f"{self.nome} encontrou uma 🧪 poção comum.")
            else:# excenção quando não ahcar nem comum, nem lendaria e nem poderosa
                self.pocoes.append("misteriosa")
                print(f"{self.nome} encontrou uma 🌙 poção misteriosa!")
                
            if not self.revive and random.randint(1, 100) <= 5:  #se não tiver mais a poção da fênix e procurar, mas só tem 5% de achar
                self.revive = True
                print(f"{self.nome} encontrou uma 🕊️ Poção da Fênix! Agora está protegido da morte novamente."                
                        
        def encontrar_arma(self): # método que procurar uma espada
            chance = random.randint(1, 100)
            if chance <= 1 and (self.classe == "Cavaleiro" or self.classe_inicial== "Cavaleiro"):
                self.arma.append("lunar")
                print(f"️🌙 Você encontrou: Espada Lunar (Lendária/Linhagem dos céus)!")
                print("Ela irradia poder... mas há algo especial nela. Que apenas pode ser despertada na hora certa")
                self.dano_max += 20
                print("🗡️ Dano aumentado em +20!")
            elif chance <= 2 and self.classe == "Cavaleiro":
                self.arma.append("solar")
                print(f"☀️ Você encontrou: Espada Solar (Lendária/Linhagem dos céus)!")
                print("Ela irradia poder... mas há algo especial nela. Que apenas pode ser despertada na hora certa")
                self.dano_max += 20
                print("🗡️ Dano aumentado em +20!"
            elif chance <= 10 and self.classe == "Cavaleiro": # 10 % de achar uma espada Lendária/Abençoada
                self.arma.append("branca")
                print(f"⬜ Você encontrou: Espada Branca(Lendária/Abençoada)!")
                print("Ela irradia poder... mas há algo especial nela.")
                self.dano_max += 50
                dano_vida = random.randint(10, 40)
                self.vida += dano_vida
                self.vida = max(0, self.vida)
                print(f"🌀 A benção deu {dano_vida} de vida!")
                print(f"❤️ Vida atual: {self.vida}")
            elif chance <= 20 and self.classe == "Cavaleiro":# 20 % de achar uma espada Lendária/Maldita
                self.arma.append("negra")
                print(f"⬛ Você encontrou: Espada Negra (Lendária/Maldita)!")
                print("⚠️ Ela irradia poder... mas há algo sinistro nela.")
                self.dano_max += 40
                dano_maldicao = random.randint(10, 40)
                self.vida -= dano_maldicao
                self.vida = max(0, self.vida)
                print(f"💀 A maldição causou {dano_maldicao} de dano!")
                print(f"❤️ Vida atual: {self.vida}")
            elif chance <= 30 and self.classe == "Cavaleiro":# 30 % de achar uma espada Épica
                self.arma.append("escura")
                print(f"🟪 Você encontrou: Espada Escura (Épica)!")
                self.dano_max += 30
                print("🗡️ Dano aumentado em +30!")
            elif chance <= 50 and self.classe == "Cavaleiro":# 50 % de achar uma espada Rara
                self.arma.append("brilhante")
                print(f"🟦 Você encontrou: Espada Brilhante (Rara)!")
                self.dano_max += 20
                print("🗡️ Dano aumentado em +20!")
            elif chance <= 70 and self.classe == "Cavaleiro":# 70 % de achar uma espada Comum
                self.arma.append("nova")
                print(f"🟫 Você encontrou: Espada Nova (Comum)!")
                self.dano_max += 10
                print("🗡️ Dano aumentado em +10!")
            elif chance <= 1 and self.classe == "Arqueiro":
                self.arma.append("lunar")
                print(f"️🌙 Você encontro: Arco Lunar (Lendário/Linhagem dos céus)!")
                print("Ele irradia poder... mas há algo especial nele. Que apenas pode ser despertado na hora certa")
                self.dano_max += 20
                print("🗡️ Dano aumentado em +20!")
            elif chance <= 2 and self.classe == "Arqueiro":
                self.arma.append("solar")
                print(f"☀️ Você encontrou: Arco Solar (Lendário/Linhagem dos céus)!")
                print("Ela irradia poder... mas há algo especial nela. Que apenas pode ser despertada na hora certa")
                self.dano_max += 20
                print("🗡️ Dano aumentado em +20!"
            elif chance <= 10 and self.classe == "Arqueiro": # 10 % de achar um arco Lendário/Abençoado
                self.arma.append("branca")
                print(f"⬜ Você encontrou: Arco Branco(Lendário/Abençoado)!")
                print("Ele irradia poder... mas há algo especial nele.")
                self.dano_max += 50
                dano_vida = random.randint(10, 40)
                self.vida += dano_vida
                self.vida = max(0, self.vida)
                print(f"🌀 A benção deu {dano_vida} de vida!")
                print(f"❤️ Vida atual: {self.vida}")
            elif chance <= 20 and self.classe == "Arqueiro":# 20 % de achar um arco Lendário/Maldito
                self.arma.append("negra")
                print(f"⬛ Você encontrou: Arco Negro (Lendário/Maldito)!")
                print("⚠️ Ele irradia poder... mas há algo sinistro nele.")
                self.dano_max += 40
                dano_maldicao = random.randint(10, 40)
                self.vida -= dano_maldicao
                self.vida = max(0, self.vida)
                print(f"💀 A maldição causou {dano_maldicao} de dano!")
                print(f"❤️ Vida atual: {self.vida}")
            elif chance <= 30 and self.classe == "Arqueiro":# 30 % de achar um Arco Épic
                self.arma.append("escura")
                print(f"🟪 Você encontrou: Arco Escuro (Épico)!")
                self.dano_max += 30
                print("🗡️ Dano aumentado em +30!")
            elif chance <= 50 and self.classe == "Arqueiro":# 50 % de achar uma espada Rara
                self.arma.append("brilhante")
                print(f"🟦 Você encontrou: Arco Brilhante (Raro)!")
                self.dano_max += 20
                print("🗡️ Dano aumentado em +20!")
            elif chance <= 70 and self.classe == "Arqueiro":# 70 % de achar uma espada Comum
                self.arma.append("nova")
                print(f"🟫 Você encontrou: Arco Novo (Comum)!")
                self.dano_max += 10
                print("🗡️ Dano aumentado em +10!")
                
            
            if len(self.arma) >= self.max_arma: # se encontrar, mas o loot estiver cheio
                    print(f"{self.nome} encontrou uma arma, mas já está com o máximo de {self.arma}.")
                    return
            
        def atualizar_visao(self, periodo):
            if periodo == "noite" and self.visao_noturna == False:
                self.visao = 50
                print(f"{self.nome} agora tem visão reduzida{self.visao}.")
            else:
                self.visao = 100
                print(f"{self.nome} agora tem visão normal{self.visao}.")
                
        def desbloquear_visao_noturna(self):
            classes_aptas = ["Ladino", "Arqueiro", "Bruxo", "Druida", "Vampiro"]
            if self.classe in classes_aptas:
                self.visao_noturna = True
                print(f"{self.nome} desenvolveu visão noturna! 👁️🌑")
            else:
                print(f"{self.nome} não conseguiu desenvolver visão noturna! 👁️🌑")
                            
        def verificar_nivel(self):
            print(f"Nível: {self.nivel}, XP máximo para o nível: {self.quantidade_max_xp} XP")
            print(f"Faltando para o próximo nível: {self.faltando_para_proximo_nivel} XP")
                    
        def adicionar_acao(self, acao, tipo):
            """
            Adiciona uma ação à moral do personagem. As ações podem ser 'positiva' ou 'negativa'.
            """
            if tipo == 'positiva':
                self.pontos_positivos += 1
            print(f"Ação positiva! Moral positiva aumentada para {self.pontos_positivos}.")
            elif tipo == 'negativa':
                self.pontos_negativos += 1
                print(f"Ação negativa! Moral negativa aumentada para {self.pontos_negativos}.")
        
            self.moral.append((acao, tipo))  # Armazena a ação na lista de moral
            self.verificar_corrupta()  # Verifica se a moral do personagem causou corrupção

        def verificar_corrupta(self):
            """
            Verifica se a moral do personagem foi corrompida.
            A moral se corrompe quando os pontos negativos superam os positivos.
            """
            if len(self.moral) >= self.max_moral:
                if self.pontos_negativos > self.pontos_positivos:
                    self.corrompido = True
                    print(f"{self.nome} está corrompido pela moral negativa!")
                else:
                    print(f"{self.nome} manteve sua moral positiva.")
            else:
                print(f"{self.nome} ainda tem espaço para novas ações.")
                    
        def verificar_iluminar(self):
            """
            Verifica se a moral do personagem foi corrompida.
            A moral se corrompe quando os pontos negativos superam os positivos.
            """
            if len(self.moral) >= self.max_moral:
                if self.pontos_positivos > self.pontos_negativos:
                    self.iluminado = True
                    print(f"{self.nome} está iluminado pela moral negativa!")
                else:
                    print(f"{self.nome} manteve sua moral positiva.")
            else:
                print(f"{self.nome} ainda tem espaço para novas ações.")
