import random # importando a biblioteca random
# Definição da classe Personagem
class Personagem: 
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
            self.dano_max += 40
            dano_maldicao = random.randint(10, 40)
            self.vida -= dano_maldicao
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


nome = input("Nome do seu personagem: ").strip().lower() # adicionar o nome do heroi
vida = int(input("Digite o tamanho da sua vida: ")) # adicionar o tamanho da vida
sexo = input("Seu sexo: ").capitalize() # adicionar o sexo do heroi
# Criando um personagem para teste
heroi = Personagem(nome, vida, sexo) #criar o objeto

# Exibindo as informações
print("=== Ficha do Personagem ===") # ficha do Personagem
print(f"Nome: {heroi.nome}")
print(f"Vida: {heroi.vida}")
print(f"Sexo: {heroi.sexo}")

# Saudação personalizada baseada no sexo
if heroi.sexo == "Feminino": # se o sexo for feminino
    print(f"Bem-vinda, {heroi.nome}!")
elif heroi.sexo == "Masculino":
    print(f"Bem-vindo, {heroi.nome}!") 
else: #caso digitar algo errado
    exit()
escolha = int(input(f'"vamos começar nossa aventura!"'"! Entramos na caverna, logo tinha dois caminhos Qual será nosso caminho? 1°Com som de música | 2°Com uma risada sinistra!: "))
if escolha == 1: # caso escolha 1 
    print("Caimos num buraco")
    exit() # acabar o programa
elif escolha ==2: #caso escolha 2
    print(f"O caminho parecia tranquilo até que, de repente, ouvimos novamente aquela risada macabra. Viramos rapidamente e, para nosso terror, vimos um goblin correndo em nossa direção, brandindo uma adaga afiada.. Logo {heroi.nome} puxar uma espada")
    goblin = Personagem("Goblin", 50, "Monstro") # objeto criado para ser o inimigo
    turno = 1
    while heroi.esta_vivo() and goblin.esta_vivo(): # continua enquanto o heroi ou o goblin estiver vivo
        acao = int(input("Deseja atacar (1) ou tomar poção (2)? ")) 
        if acao == 1: # atacar o goblin
            print(f"\n--- Turno {turno} ---")
            heroi.atacar(goblin)
            

        elif acao == 2: # tomar poção 
            heroi.tomar_pocao()
        
        if goblin.esta_vivo(): # se o goblin estiver vivo, então ele atacar
            dano = random.randint(1, 10) # de 1 a 10 de dano
            chance_esquiva = 20  # 20% de chance de desviar
            tentativa = random.randint(1, 100)
            if tentativa <= chance_esquiva:
                print(f"{heroi.nome} desviou do ataque de {goblin.nome}!")
            else:
                heroi.vida -= dano # diminuir  a vida do heroi 
                print(f"Goblin atacou {heroi.nome} e causou {dano} de dano!")
                print(f'{heroi.nome} agora tem {heroi.vida} de vida.\n')
            
        turno += 1

else: # caso escolha uma opção invalida
    print("ERRO")
    exit()
    
# Resultado final - só aparece uma vez
print("\nCombate encerrado.")
if heroi.esta_vivo(): # caso o heroi ainda continua vivo
    print(f"{heroi.nome} venceu!")
    heroi.tentar_ganhar_pocao()
    
else: # se o heroi estiver morto
    print(f"{goblin.nome} venceu!")        
    exit()    

print(f"Depois de {heroi.nome} matar o Goblin voltamos a andar em buscar do tesouro. Até que aparece um slime na nossa frente")
slime = Personagem("slime", 20, "Monstro") # objeto criado para ser o inimigo
turno = 1
while heroi.esta_vivo() and slime.esta_vivo():
    acao = int(input("Deseja atacar (1) ou tomar poção (2)? "))
    if acao == 1: # atacar o slime
        print(f"\n--- Turno {turno} ---")
        heroi.atacar(slime)

    elif acao == 2: # beber poção
        heroi.tomar_pocao()
                
    # Slime ataca, se estiver vivo
    if slime.esta_vivo():
        dano = random.randint(1, 6)
        chance_esquiva = 20  # 20% de chance de desviar
        tentativa = random.randint(1, 100)
        if tentativa <= chance_esquiva:
            print(f"{heroi.nome} desviou do ataque de {slime.nome}!")
        else:
            heroi.vida -= dano
            print(f"Slime atacou {heroi.nome} e causou {dano} de dano!")
            print(f'{heroi.nome} agora tem {heroi.vida} de vida.\n')    
    turno += 1
        
print("\nCombate encerrado.")
if heroi.esta_vivo():
    print(f"{heroi.nome} venceu!")
    heroi.tentar_ganhar_pocao()
    
else:
    print(f"{slime.nome} venceu!")        
    exit()
    
escolha = 0
while escolha != 1:
    escolha = int(input('"Parabéns {heroi.nome} por limpar nosso caminho para o tesouro e agora o que desejar fazer? 1° Continuar a aprofundar na caverna| 2° procurar poção| 3° sentar e afiar espada"'))
        
    if escolha == 2:
        heroi.tentar_ganhar_pocao()
    elif escolha == 3:
        print(f"{heroi.nome} se sentar é começar a afiar a espada")
        heroi.dano_max += 1
        print("A sua espada fica mais afiada")
    elif escolha != 1:
        print("Opção inválida ou ainda não é hora de continuar.\n")
        
print('"Entendi, vem {heroi.nome} vamos achar esse tesouro!"')
print("Estávamos andado até que dava para ouvir um grunhido estranho e logo aparecia um orc verde que estava sorrindo")
print("ORC:"'"Que grande sorte dois humanos para devorar!"')
orc = Personagem("Orc", 70, "Monstro") # objeto criado para ser o inimigo
turno = 1
while heroi.esta_vivo() and orc.esta_vivo():
    acao = int(input("Deseja atacar (1) ou tomar poção (2)? "))
    if acao == 1: # atacar o orc
        print(f"\n--- Turno {turno} ---")
        heroi.atacar(orc)

    elif acao == 2: # beber poção
        heroi.tomar_pocao()
                
    # orc ataca, se estiver vivo
    if orc.esta_vivo():
        dano = random.randint(1, 30)
        chance_esquiva = 20  # 20% de chance de desviar
        tentativa = random.randint(1, 100)
        if tentativa <= chance_esquiva:
            print(f"{heroi.nome} desviou do ataque de {orc.nome}!")
        else:
            heroi.vida -= dano
            print(f"Orc atacou {heroi.nome} e causou {dano} de dano!")
            print(f'{heroi.nome} agora tem {heroi.vida} de vida.\n')    
    turno += 1
    
print("\nCombate encerrado.")
if heroi.esta_vivo():
    print(f"{heroi.nome} venceu!")
    heroi.tentar_ganhar_pocao()
else:
    print(f"{orc.nome} venceu!")        
    exit()    
print(f'"Uau {heroi.nome} parabéns por matar esse orc sujo, mas agora vamos continuar porque estamos quase chegando no nosso destino"')
print("Enquanto andavamos surgir uma pessoa com um um cajado com uma bola de cristal roxa e quando apontava para nós percebiamos o que era")
print(f'"Cuidado {heroi.nome} ele é um necromante!"')
necromante = Personagem("Necromante", 110, "Monstro") # objeto criado para ser o Necromante
turno = 1
while heroi.esta_vivo() and necromante.esta_vivo():
    acao = int(input("Deseja atacar (1) ou tomar poção (2)? "))
    if acao == 1: # atacar o necromante
        print(f"\n--- Turno {turno} ---")
        heroi.atacar(necromante)

    elif acao == 2: # beber poção
        heroi.tomar_pocao()
                
    # necromante ataca, se estiver vivo
    if necromante.esta_vivo():
        print(f'"É tola tentativa de tentar me derrotar"')
        chance_ataque = 50  # 50% de chance de ataque
        tentativa1 = random.randint(1, 100)
        if tentativa1 <= 20:  # 20% de chance de se curar
            cura = random.randint(5, 25)
            necromante.vida += cura
            print(f"{necromante.nome} se recuperou e ganhou {cura} de vida!")
            print(f"Vida atual de {necromante.nome}: {necromante.vida}")
        elif tentativa1 <= 30:
            print(F'"Não lutarei contra você, mas meu soldado sim!"')
            esqueleto = Personagem("Esqueleto", 40, "Monstro")
            turno1 = 1
            while heroi.esta_vivo() and esqueleto.esta_vivo():
                acao1 = int(input("Deseja atacar (1) ou tomar poção (2)? "))
                if acao1 == 1: # atacar o esqueleto
                    print(f"\n--- Turno {turno} ---")
                    heroi.atacar(esqueleto)
    
                elif acao1 == 2: # beber poção
                    heroi.tomar_pocao() 
                    
                if esqueleto.esta_vivo(): # se o goblin estiver vivo, então ele atacar
                    dano = random.randint(1, 10) # de 1 a 10 de dano
                    chance_esquiva = 20  # 20% de chance de desviar
                    tentativa = random.randint(1, 100)
                    if tentativa <= chance_esquiva:
                        print(f"{heroi.nome} desviou do ataque de {esqueleto.nome}!")
                    else:
                        heroi.vida -= dano # diminuir  a vida do heroi 
                        print(f"Goblin atacou {heroi.nome} e causou {dano} de dano!")
                        print(f'{heroi.nome} agora tem {heroi.vida} de vida.\n')
                    
                turno1 += 1
                    
                    
        elif tentativa1 <= chance_ataque:
            chance_esquiva = 20  # 20% de chance de desviar
            tentativa = random.randint(1, 100)
            if tentativa <= chance_esquiva:
                print(f"{heroi.nome} desviou do ataque de {necromante.nome}!")
            else:
                dano = random.randint(1, 26)
                heroi.vida -= dano
                print(f"Orc atacou {heroi.nome} e causou {dano} de dano!")
                print(f'{heroi.nome} agora tem {heroi.vida} de vida.\n')    
            
    turno += 1
    
if heroi.sexo == "Feminino": # se o sexo for feminino
    print(f'"Você fez algo incrivel, grande {heroi.nome}"')
elif heroi.sexo == "Masculino":
    print(f"Você fez algo incrivel, grandioso {heroi.nome}!")
heroi.tentar_ganhar_pocao()
print(f'"Mas finalmente estamos chegando no nosso destino!"')
