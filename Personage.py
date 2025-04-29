import random
from Xp import *
from Classes import *

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
        if self.classe_inicial in ["Guerreiro", "Arqueiro", "Assassino"]:
            self.max_arma = 2  # Pode equipar 2 armas!
        else:
            self.max_arma = 1  # Padrão: 1 arma
        if self.classe_inicial == "Monge":
            self.ki = self.defini_ki()
        if self.classe_inicial in ["Mago", "Feiticeiro", "Bruxo", "Bardo", "Druida"]:
            self.mana = self.defini_mana()
        if self.classe_inicial in ["Guerreiro", "Berserker", "Arqueiro", "Assassino"]:  
            self.aura = self.defini_aura()
        if self.classe_inicial == "Clérigo":
            self.energia_divina = self.defini_energia_divina()
        if self.classe == "Mestre de Batalha" or self.classe_inicial == "Mestre de Batalha":
            self.posicao = self.definir_posicao()
            self.zona_ativa = False
            self.resistencia_extra = 5
            self.passiva_forca_de_vanguarda_ativa = False
            self.ativada = False
        self.dinheiro = self.definir_dinheiro()
        self.nivel = 1
        self.xp_atual = xp_atual
        self.moral = []  # Lista que mantém as ações de moral (pode ser positiva ou negativa)
        self.max_moral = 10  # O máximo que a moral pode atingir
        self.pontos_positivos = 0  # Quantidade de pontos positivos acumulados
        self.pontos_negativos = 0  # Quantidade de pontos negativos acumulados
        self.corrompido = False  # Se o personagem está corrompido ou não
        self.iluminado = False
        self.resistencia = 5
        self.faltando_para_proximo_nivel = calcular_faltando(self.nivel, self.xp_atual)
        self.quantidade_max_xp = calcular_xp_max(self.nivel)
        self.dano_max =  self.definir_dano() # dano base maximo 
        self.revive = self.definir_revive() #não começa com a poção da fênix
        self.max_vida = vida
        self.envenenado = False
        self.tipo_veneno = None
        self.turnos_veneno = 0
        self.em_chamas = False
        self.bonus_dano = 0 
        self.tipo_fogo = None
        self.turnos_fogo = 0
        self.corrosivo = False
        self.adormecido = False
        self.atordoado = False
        self.turnos_atordoado = 0
        self.sangramento = False  # Estado de sangramento
        self.turnos_sangramento = 0  # Número de turnos de sangramento
        self.turnos_sono = 0
        self.tipo_sono = None
        self.visao = 100
        self.habilidades_ativas = []  # herdadas da classe
        self.habilidades_passivas = []  # herdadas da classe
        self.habilidades_extra = []   # ganhas por quests, magias, etc
        self.inimigos_ameacados = set()
        if self.classe_inicial in ["Guerreiro", "Monge", "Berserker"]:
            self.defesa = 10
        elif self.classe_inicial in ["Arqueiro", "Assassino", "Monge"]:
            self.defesa = 7
        elif self.classe_inicial in ["Mago", "Feiticeiro", "Bruxo", "Bardo", "Druida"]:
            self.defesa = 4
        elif self.classe_inicial == "Clérigo":
            self.defesa = 6
        else:
            self.defesa = 5  # valor padrão
        
        def tentar_multiclassificar(self, nova_classe):
            if nova_classe not in classes:
                print(f"❌ Classe '{nova_classe}' não existe.")
                return
        
            classe_atual_info = classes[self.classe]
            classe_nova_info = classes[nova_classe]
        
            # Verifica se a classe inicial é a mesma
            if classe_nova_info["classe_inicial"] != self.classe_inicial:
                print(f"❌ {self.nome} não pode mudar para {nova_classe}, pois pertence a outra árvore de classe (inicial: {self.classe_inicial}).")
                return
        
            # Verifica se a nova classe está na lista de evolução permitida
            if nova_classe not in classe_atual_info.get("pode_evoluir", []):
                print(f"❌ {self.nome} não pode evoluir de {self.classe} para {nova_classe}.")
                return
        
            # Verifica o nível de evolução (se estiver definido nas duas classes)
            nivel_atual = classe_atual_info.get("nivel_evolucao")
            nivel_novo = classe_nova_info.get("nivel_evolucao")
        
            if nivel_atual is not None and nivel_novo is not None:
                if nivel_novo != nivel_atual + 1:
                    print(f"❌ {nova_classe} requer um nível de evolução superior. ({nivel_novo} vs {nivel_atual + 1})")
                    return
        
            # Tudo certo: evolução liberada
            self.classe = nova_classe
            self.classe_inicial = classe_nova_info["classe_inicial"]  # Atualiza a raiz da árvore
            print(f"✅ {self.nome} evoluiu para {self.classe}!")
            
        def aumentar_resistencia(self, valor):
            self.resistencia += valor

        def reduzir_resistencia(self, valor):
            self.resistencia -= valor
            
            
        def poder_habilidade(self, usar_habilidade):
            # Verifica se a habilidade existe no dicionário geral
            if usar_habilidade not in habilidades_ativas:
                print(f"❌ A habilidade '{usar_habilidade}' não existe.")
                return
        
            # Verifica se a habilidade é do personagem
            habilidades_totais = self.habilidades_ativas + self.habilidades_extra  # Somando habilidades adquiridas de outras fontes
        
            if usar_habilidade not in habilidades_totais:
                print(f"❌ {self.nome} não possui a habilidade '{usar_habilidade}'!")
                return
        
            # Se passou pelas duas verificações, ativa a habilidade
            print(f"✨ {self.nome} usou a habilidade {usar_habilidade}!")
            habilidades_ativas[usar_habilidade](self)  # Chama a função da habilidade
        
            
        def verificar_passivas(self, ambiente):
            """
            Verifica e aplica habilidades passivas automaticamente dependendo do ambiente.
            """
        
            if ambiente == "noite":
                if "Visão Noturna" in self.habilidades_passivas or "Visão Noturna" in self.habilidades_extras:
                    self.visao = 100
                    print(f"🌙 {self.nome} ativa a Visão Noturna! Visão total no escuro.")
                else:
                    self.visao = 50
                    print(f"🌑 {self.nome} tem visão reduzida ({self.visao}%) por ser noite.")
            else:
                self.visao = 100
                print(f"☀️ {self.nome} tem visão normal ({self.visao}%) durante o dia.")
        
        
        def ganhar_habilidade(self, nova_habilidade):
            if nova_habilidade not in habilidades_ativas:
                print(f"❌ A habilidade '{nova_habilidade}' não existe e não pode ser aprendida.")
                return
        
            if nova_habilidade in self.habilidades_ativas or nova_habilidade in self.habilidades_extra:
                print(f"⚡ {self.nome} já possui a habilidade '{nova_habilidade}'.")
                return
        
            self.habilidades_extra.append(nova_habilidade)
            print(f"🎉 {self.nome} aprendeu a habilidade extra: {nova_habilidade}!")
            
    
        def status(self):# mostrar os status do personagem 
            print(f"{self.nome} está no nível {self.nivel} e é {self.classe}.")
        
        def esta_vivo(self):
            self.vida = max(0, self.vida)  # Garante que a vida nunca fique negativa
            return self.vida > 0
            
        def atacar(self, inimigo):
            # Verifica se o personagem está adormecido antes de agir
            self.verificar_sono()
            if self.adormecido:
                if self.tipo_sono == "Sono leve":
                    print(f"{self.nome} está em sono leve... está meio desorientado e pode atacar, mas a chance de erro é maior.")
                    # A chance de erro pode aumentar um pouco por estar desorientado
                    chance_erro = random.randint(1, 100)
                    if chance_erro > 80:  # Caso erre o ataque
                        print(f"{self.nome} errou o ataque contra {inimigo.nome}!")
                        return
                elif self.tipo_sono == "Sono mágico":
                    print(f"{self.nome} está em sono mágico! Só magias podem acordá-lo e ele não pode atacar.")
                    return
                elif self.tipo_sono == "Sono profundo":
                    print(f"{self.nome} está em sono profundo... não pode atacar.")
                    return
                elif self.tipo_sono == "Sono eterno":
                    print(f"{self.nome} está em sono eterno... não pode atacar.")
                    return
                elif self.tipo_sono == "Sono de desorientação":
                    print(f"{self.nome} está desorientado devido ao sono... a chance de erro no ataque está aumentada.")
                    # A chance de erro do ataque é aumentada devido à desorientação
                    chance_erro = random.randint(1, 100)
                    if chance_erro > 60:  # Caso erre o ataque (a chance de erro é maior)
                        print(f"{self.nome} errou o ataque contra {inimigo.nome}!")
                        return
                elif self.tipo_sono == "Sono espiritual":
                    print(f"{self.nome} está em sono espiritual... não pode atacar fisicamente, apenas com magias.")
                    return  # O personagem não pode atacar fisicamente
                elif self.tipo_sono == "Sono criogênico":
                    print(f"{self.nome} está em sono criogênico... está imune a danos, mas não pode atacar.")
                    return          
            
            # Se o personagem está atordoado, ele pode acordar ou agir após o dano
            if self.atordoado:
                print(f"{self.nome} está atordoado e não pode atacar! 😵")
                self.turnos_atordoado -= 1  # Decrementa o número de turnos de atordoamento
                if self.turnos_atordoado <= 0:
                    self.atordoado = False  # Se o contador de turnos chegar a zero, o personagem não está mais atordoado
                    print(f"{self.nome} deixou de estar atordoado e pode agir novamente! 🎯")
                return
                    
            if not self.esta_vivo(): # não atacar se o inimigo estiver morto
                print(f"{self.nome} não pode atacar porque foi derrotado.")
                return

            if not inimigo.esta_vivo():# não atacar se o inimigo tive sido derrotado
                print(f"{inimigo.nome} já está derrotado.")
                return

            dano = random.randint(1, self.dano_max)  # Calcular dano aleatório
            
            if chance <= 80:  # 80% de chance de acertar
                inimigo.vida -= dano  # Reduz a vida do inimigo
                inimigo.vida = max(0, inimigo.vida)  # Garante que a vida não fique negativa
                print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")
                inimigo.sofrer_dano(dano)  # Chama o método sofrer_dano para efeitos adicionais
            else:  # Caso erre o ataque
                print(f"{self.nome} errou o ataque contra {inimigo.nome}!")
            
        def sofrer_dano(self, dano):
            dano_final = max(dano - self.resistencia, 0)  # Dano não pode ser negativo
            self.vida -= dano_final
            print(f"{self.nome} recebeu {dano_final} de dano! Vida restante: {self.vida}.")
            
            # Verifica se o personagem está adormecido
            if self.adormecido:
                if self.tipo_sono == "Sono leve":
                    self.adormecido = False  # Acorda o personagem
                    print(f"{self.nome} acordou após sofrer dano! 😲")
                
                elif self.tipo_sono == "Sono mágico":
                    print(f"{self.nome} está em sono mágico... O dano não foi suficiente para acordá-lo!")
                
                elif self.tipo_sono == "Sono profundo":
                    print(f"{self.nome} está em sono profundo... O dano não é suficiente para acordá-lo. Ele dorme até o fim do turno.")
                
                elif self.tipo_sono == "Sono eterno":
                    print(f"{self.nome} está em sono eterno... O dano não tem efeito sobre ele.")
                
                elif self.tipo_sono == "Sono de desorientação":
                    print(f"{self.nome} está desorientado... Mesmo com o dano, ele permanece adormecido, mas a chance de erro de ataque aumenta.")
                
                elif self.tipo_sono == "Sono espiritual":
                    print(f"{self.nome} está em sono espiritual... O dano não tem efeito físico sobre ele.")
                
                elif self.tipo_sono == "Sono criogênico":
                    print(f"{self.nome} está em sono criogênico... O dano não tem efeito, ele está congelado.")
            
            # Verifica se a vida do personagem chegou a zero ou menos
            if self.vida <= 0:
                self.vida = 0
                print(f"{self.nome} foi derrotado! 💀")     
                
        def ser_atordoado(self, turnos=3):
            # Método que coloca o personagem no estado atordoado por um número de turnos
            self.atordoado = True
            self.turnos_atordoado = turnos  # Define o número de turnos que o personagem ficará atordoado
            print(f"{self.nome} foi atordoado e ficará atordoado por {turnos} turnos! 😵")
                
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
            
        def aplicar_veneno(self, tipo_veneno, turnos=None):
            self.envenenado = True
            self.tipo_veneno = tipo_veneno
            self.turnos_veneno = turnos
            if turnos is None:
                self.turnos_veneno = None  # Permanente
                print(f"{self.nome} O veneno '{self.tipo_veneno}'corre eternamente pelas veias! 😵 Sofrerá dano contínuo até a morte.")
            else:
                self.turnos_veneno = turnos
                print(f"{self.nome} O veneno corre eternamente pelas veias! 😵")

        def aplicar_queimadura(self,tipo_fogo, turnos=None):
            self.em_chamas = True
            self.tipo_fogo = tipo_fogo
            self.turnos_fogo = turnos
            if turnos is None:
                self.turnos_fogo = None  # Permanente
                print(f"{self.nome} as chamas do '{self.tipo_fogo}' ardem eternamente! 🔥 Sofrerá dano contínuo até a morte.")
            else:
                self.turnos_fogo = turnos
                print(f"{self.nome} está em chamas! 🔥 Sofrerá dano por {turnos} turnos.")
        
        def aplicar_sono(self,tipo_sono, turnos):
            self.adormecido = True
            self.tipo_sono = tipo_sono
            self.turnos_sono = turnos
            if turnos:
                print(f"{self.nome} foi afetado por {tipo_sono}! 😴 Dormirá por {turnos} turnos.")
            else:
                print(f"{self.nome} caiu em {tipo_sono} permanente! 😴")
        
        def verificar_sono(self):
            if self.adormecido:
                if self.tipo_sono == "Sono leve":
                    print(f"{self.nome} está em sono leve... pode acordar com dano.")
                
                elif self.tipo_sono == "Sono mágico" and self.classe_inicial != "Mago":
                    print(f"{self.nome} está em sono mágico! Apenas magia pode despertá-lo.")
                
                elif self.tipo_sono == "Sono profundo":
                    print(f"{self.nome} está em sono profundo...")
                
                elif self.tipo_sono == "Sono eterno":
                    print(f"{self.nome} está em sono eterno... não acordará por nada!")
                    
                elif self.tipo_sono == "Sono mortal":
                    print(f"{self.nome} está em sono eterno...só poe acordar com 1 de vida!")
                    
                elif self.tipo_sono == "Sono de desorientação":
                    print(f"{self.nome} está desorientado, dormindo profundamente, mas sua precisão de ataque está reduzida.")
                
                elif self.tipo_sono == "Sono espiritual":
                    print(f"{self.nome} está em sono espiritual... imune a danos físicos, mas vulnerável a ataques mágicos.")
                
                elif self.tipo_sono == "Sono criogênico":
                    print(f"{self.nome} está em sono criogênico... imune a danos, e só pode ser acordado com magia ou dispositivo especial.")
                
                if self.turnos_sono is not None:
                    self.turnos_sono -= 1
                    print(f"{self.nome} está dormindo... ({self.turnos_sono} turnos restantes)")
                    if self.turnos_sono <= 0:
                        self.adormecido = False
                        print(f"{self.nome} acordou de seu sono.")
              
        def aplicar_acido(self):
            self.corrosivo = True
            print(f"{self.nome} bebeu Ácido! 💀")
            
        def sofrer_efeitos_acido(self,):
            if self.corrosivo:
                dano = -self.max_vida
                print(f"{self.nome} bebeu ácido e morreu sendo corroído por dentro, o corpo se desfazendo em agonia!")
                
        def sofrer_efeitos_f(self):
            if self.em_chamas:
                if self.tipo_fogo == "Fogo arcano":
                    dano = 15
                else:
                    dano = 5
        
                self.vida -= dano
                print(f"{self.nome} sofre {dano} de dano por fogo! 🔥")
        
                if self.turnos_fogo is not None:
                    self.turnos_fogo -= 1
        
                    if self.turnos_fogo <= 0:
                        if self.tomar_pocao or self.classe_inicial == "Clérigo":
                            self.em_chamas = False
                            print(f"{self.nome} apagou as chamas e não está mais queimando.")
                        elif self.tipo_fogo == "Fogo arcano" and self.classe_inicial != "Clérigo":
                            print(f"A poção não tem efeito em {self.nome}! Apenas um Clérigo pode extinguir esse fogo arcano.")
                else:
                    print(f"{self.nome} está em chamas PERMANENTES! 💀")
                    if self.tomar_pocao:
                        self.em_chamas = False
                        print(f"{self.nome} conseguiu apagar as chamas com uma poção.")
        
        def sofrer_efeitos_f(self, inimigo):
            # Efeito de fogo no personagem
            if self.em_chamas:
                if self.tipo_fogo == "Fogo arcano":
                    dano = 15
                else:
                    dano = 5
                print(f"{self.nome} sofre {dano} de dano por fogo! 🔥 (restam {self.turnos_fogo} turnos)")
                self.vida -= dano
        
                if self.turnos_fogo is not None:
                    self.turnos_fogo -= 1
                    if self.turnos_fogo <= 0:
                        if self.tomar_pocao or self.classe_inicial == "Clérigo":
                            self.em_chamas = False
                            print(f"{self.nome} não está mais em chamas.")
                        elif self.tipo_fogo == "Fogo arcano" and self.classe_inicial != "Clérigo":
                            print(f"A poção não surte efeito! Apenas um Clérigo pode apagar o fogo arcano em {self.nome}.")
                else:
                    print(f"{self.nome} queima com fogo PERMANENTE! 💀")
                    if self.tomar_pocao:
                        self.em_chamas = False
                        print(f"{self.nome} usou uma poção e apagou as chamas.")
        
            # Efeito de fogo no inimigo
            if hasattr(inimigo, 'em_chamas') and inimigo.em_chamas:
                if inimigo.tipo_fogo == "Fogo arcano":
                    dano = 15
                else:
                    dano = 5
                inimigo.vida -= dano
                print(f"{inimigo.nome} sofre {dano} de dano por fogo! 🔥 (restam {inimigo.turnos_fogo} turnos)")
        
                if inimigo.turnos_fogo is not None:
                    inimigo.turnos_fogo -= 1
                    if inimigo.turnos_fogo <= 0:
                        inimigo.em_chamas = False
                        print(f"{inimigo.nome} não está mais em chamas.")
                        
        def sofrer_efeitos_s(self):
            # Aplica dano de sangramento a cada turno
            if self.sangramento:
                dano_sangramento = 9  # Dano fixo de sangramento por turno (você pode ajustar esse valor)
                self.vida -= dano_sangramento
                self.vida = max(0, self.vida)  # Evita que a vida do personagem fique negativa
                print(f"{self.nome} sofre {dano_sangramento} de dano devido ao sangramento! Vida restante: {self.vida}")
                
                self.turnos_sangramento -= 1
                if self.turnos_sangramento <= 0:
                    self.sangramento = False
                    print(f"{self.nome} parou de sangrar.")
                    
        def sofrer_efeitos_s(self, inimigo):
            # Efeito de sangramento no personagem
            if self.sangramento:
                dano_sangramento = 9
                self.vida -= dano_sangramento
                self.vida = max(0, self.vida)
                print(f"{self.nome} sofre {dano_sangramento} de dano por sangramento! 🩸 (restam {self.turnos_sangramento} turnos) Vida: {self.vida}")
        
                self.turnos_sangramento -= 1
                if self.turnos_sangramento <= 0:
                    self.sangramento = False
                    print(f"{self.nome} parou de sangrar.")
        
            # Efeito de sangramento no inimigo
            if hasattr(inimigo, 'sangramento') and inimigo.sangramento:
                dano_sangramento = 9
                inimigo.vida -= dano_sangramento
                inimigo.vida = max(0, inimigo.vida)
                print(f"{inimigo.nome} sofre {dano_sangramento} de dano por sangramento! 🩸 (restam {inimigo.turnos_sangramento} turnos) Vida: {inimigo.vida}")
        
                inimigo.turnos_sangramento -= 1
                if inimigo.turnos_sangramento <= 0:
                    inimigo.sangramento = False
                    print(f"{inimigo.nome} parou de sangrar.")
        
            
        def sofrer_efeitos_v(self):
            if self.envenenado:
                if self.tipo_veneno == "Veneno da aranha vermelha":
                    dano = 15
                else:
                    dano = 5
        
                self.vida -= dano
                print(f"{self.nome} sofre {dano} de dano por veneno!")
        
                if self.turnos_veneno is not None:
                    self.turnos_veneno -= 1
        
                    if self.turnos_veneno <= 0:
                        if self.tomar_pocao or self.classe_inicial == "Clérigo":
                            self.envenenado = False
                            print(f"{self.nome} não está mais sofrendo efeitos do veneno.")
                        elif self.tipo_veneno == "Veneno da aranha vermelha":
                            print(f"A poção não tem efeito no {self.nome}! Apenas um Clérigo pode curá-te deste veneno.")
                else:
                    print(f"{self.nome} sofre dano de veneno PERMANENTE! 💀")
                    if self.tomar_pocao:
                        self.envenenado = False
                        print(f"{self.nome} não está mais sofrendo efeitos do veneno.")
                        
        def sofrer_efeitos_v(self, inimigo):
            # Efeito de veneno no personagem
            if self.envenenado:
                if self.tipo_veneno == "Veneno da aranha vermelha":
                    dano = 15
                else:
                    dano = 5
                print(f"{self.nome} sofre {dano} de dano por veneno! (restam {self.turnos_veneno} turnos)")
                self.vida -= dano
        
                if self.turnos_veneno is not None:
                    self.turnos_veneno -= 1
                    if self.turnos_veneno <= 0:
                        if self.tomar_pocao or self.classe_inicial == "Clérigo":
                            self.envenenado = False
                            print(f"{self.nome} não está mais sofrendo efeitos do veneno.")
                        elif self.tipo_veneno == "Veneno da aranha vermelha":
                            print(f"A poção não tem efeito em {self.nome}! Apenas um Clérigo pode curá-lo deste veneno.")
                else:  # veneno permanente
                    print(f"{self.nome} sofre dano por veneno PERMANENTE! 💀")
                    if self.tomar_pocao:
                        self.envenenado = False
                        print(f"{self.nome} não está mais envenenado.")
        
            # Efeito de veneno no inimigo (caso ele também possa ser envenenado)
            if hasattr(inimigo, 'envenenado') and inimigo.envenenado:
                if inimigo.tipo_veneno == "Veneno da aranha vermelha":
                    dano = 15
                else:
                    dano = 5
                inimigo.vida -= dano
                print(f"{inimigo.nome} sofre {dano} de dano por veneno! (restam {inimigo.turnos_veneno} turnos)")
        
                if inimigo.turnos_veneno is not None:
                    inimigo.turnos_veneno -= 1
                    if inimigo.turnos_veneno <= 0:
                        inimigo.envenenado = False
                        print(f"{inimigo.nome} não está mais envenenado.")
        
        def ser_atordoado(self):
            # Método que coloca o personagem no estado atordoado
            self.atordoado = True
            print(f"{self.nome} foi atordoado! 😵") 
        
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
            self.verificar_iluminar() # Verificar se a moral do personagem causou iluminação

        def verificar_corrupta(self):
            """
            Verifica se a moral do personagem foi corrompida.
            A moral se corrompe quando os pontos negativos superam os positivos.
            """
            if len(self.moral) >= self.max_moral:
                if self.pontos_negativos > self.pontos_positivos:
                    self.corrompido = True
                    print(f"{self.nome} a corrupção tomou conta de seu ser!")
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
                    print(f"{self.nome} a iluminação tomou conta de seu ser!")
                else:
                    print(f"{self.nome} manteve sua moral positiva.")
            else:
                print(f"{self.nome} ainda tem espaço para novas ações.")
                
        def aplicar _sangramento(self, turnos=3):
            # Método que coloca o inimigo ou personagem em sangramento por um número de turnos
            self.sangramento = True
            self.turnos_sangramento = turnos  # Define o número de turnos que o inimigo/ personagem ficará sangrando
            print(f"{self.nome} está sangrando e sofrerá dano por {turnos} turnos! 🩸")
    
