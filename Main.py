import random # importando a biblioteca random
import os # importando para o limpar tela
import time # time
from Personagem import * # puxar funções
            
def criar_personagem(): #criar personagem
    nome = input("Digite o nome do seu personagem: ").capitalize() #escolhe nome
    sexo = input("Sexo do personagem: ").capitalize() # escolhe sexo
    if sexo == "Masculino" or sexo == "Feminino":
        print("")
    else:     
        print("ERRO")
        exit()

    print("\nComo você quer definir a vida do personagem?") #Menu inicial das opções
    print("[F] Fixa (escolher entre 250, 150, 120, 80)") # 1° opção
    print("[A] Aleatória (entre 80 e 250)") # 2° opção
    print("[U] Usuário escolhe qualquer valor") # 3° opção

    modo = input("Escolha (F/A/U): ").lower() # escolha

    if modo == "f": # se escolher F
        print("\nEscolha uma vida fixa:")
        print("1 - 250 (modo guerreiro)") # 1° opção do f
        print("2 - 150 (modo equilibrado)") # 2° opção do f
        print("3 - 120 (modo padrão)") # 3° opção do f
        print("4 - 80  (modo infernal)") # 4° opção de f
        escolha = int(input("Digite 1, 2, 3 ou 4: ")) # escolha 1,2,3 ou 4

        if escolha == 1:
            vida = 250 # vai ter uma vida de 250
        elif escolha == 2:
            vida = 150 # vai ter uma vida de 150
        elif escolha == 3:
            vida = 120 # vai ter uma vida de 120
        elif escolha == 4:
            vida = 80 # vai ter uma vida de 80
        else:# se esoclher algo errado
                print("Escolha inválida. Definindo vida como 120.")
                vida = 120 # vai ter uma vida de 120

    elif modo == "a": #escolher modo a
        vida = random.randint(80, 250)

    elif modo == "u": #escolher modo u
        vida = int(input("Digite a vida desejada: "))

    else: # se escolhe algo errado
        print("Modo inválido. Usando vida padrão 120.")
        vida = 120

    personagem = Personagem(nome, vida, sexo) #criar objeto
    print(f"\nFicha criada! {personagem.nome}, {personagem.sexo}, {personagem.vida} de vida.\n") #ficha do personagem
    return personagem

def limpar_tela():#Função limpa tela
    """Limpa a tela do terminal"""
    os.system("cls" if os.name == "nt" else "clear")

def jogar():
    while True:
        limpar_tela()  # limpa a tela logo no começo
        heroi = criar_personagem()
        vida_inicial = heroi.nome 
        # Saudação personalizada baseada no sexo
        if heroi.sexo == "Feminino": # se o sexo for feminino
            print(f"Bem-vinda, {heroi.nome}!")
        else:
            print(f"Bem-vindo, {heroi.nome}!") 
        escolha = int(input(f'"vamos começar nossa aventura!"'"! Entramos na caverna, logo tinha dois caminhos Qual será nosso caminho? 1°Com som de música | 2°Com uma risada sinistra!: "))
        if escolha == 1: # caso escolha 1 
            print("Caimos num buraco")
            resposta = input(f'"Morremos de forma ridicula {heroi.nome} vamos tentar de novo? [S/N]: "').capitalize()
            if resposta == "s":
                print('"UFA! Eu não queria um final assim"')
                time.sleep(3)  # Espera 3 segundos
                continue
            elif resposta == "n":
                print("COVARDE!Valeu por jogar! Até a próxima.")
                break
            else: 
                continue # volta pro início do loop sem executar o que vem abaixo
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
            continue # volta pro início do loop sem executar o que vem abaixo
            
        # Resultado final - só aparece uma vez
        print("\nCombate encerrado.")
        if heroi.esta_vivo(): # caso o heroi ainda continua vivo
            print(f"{heroi.nome} venceu!")
            heroi.tentar_ganhar_pocao()
        else: # se o heroi estiver morto
            print(f"{goblin.nome} venceu!")
            if vida_inicial == 80 and modo == "f":
                escolha = input('"Sei que escolheu o modo infernal, mas não é ridículo morrer para um simples goblin? Esquecendo quer continuar? Talvez seja melhor diminuir a dificuldade [S/N]: "').capitalize()
                if escolha == "s":
                    print('"Valeu e um conselho. Não morrer para um goblin"')  
                    time.sleep(3)  # Espera 3 segundos
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Sério...Parece que você era uma fracote desde o início"')
                        break
                    else:
                        print('"Sério...Parece que você era um fracote desde o início"')
                        break
                else:
                    continue
            elif vida_inicial == 120 and modo == "f":
                escolha = input('"Sei que escolheu o modo padrão, mas não é ridículo morrer para um simples goblin? Tipo você tinha capacidade de durar mais...Vamos tentar de novo! [S/N]: "').capitalize()
                if escolha == "s":
                    print('"Valeu e um conselho. Tomar poção se necessário"')  
                    time.sleep(3)  # Espera 3 segundos
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Parece que você era uma convarde desde o início"')
                        break
                    else:
                        print('"Parece que você era um convarde desde o início"')
                        break
                else:
                    continue
            elif vida_inicial == 150 and modo == "f":
                escolha = input('"Sei que escolheu o modo equilibrado, mas não é era necessário ser equilibrado também no dano e na cura? Todo mundo falhar...Porém vamos continuar! [S/N]: "').capitalize()
                if escolha == "s":
                    print('"Legal... vamos tentar de novo. Só que, da próxima vez, seria bom se não precisássemos começar tudo do zero."')  
                    time.sleep(3)  # Espera 3 segundos
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print("Ele apenas virou o rosto para o lado, sem dizer uma palavra, deixando claro que não se importava com sua decisão. Apenas seguiu com o seu caminho, como se nada tivesse acontecido.") 
                        break
                    else:
                        print("Ele apenas virou o rosto para o lado, sem dizer uma palavra, deixando claro que não se importava com sua decisão. Apenas seguiu com o seu caminho, como se nada tivesse acontecido.") 
                        break
                else:
                    continue
            elif vida_inicial == 250 and modo == "f":
                escolha = input('"Você escolheu o modo guerreiro, mas não! Tinha que ser morto por um goblin! Um goblin, sério? Vamos começar de novo logo, antes que eu perca mais tempo. [S/N]: "').capitalize()
                if escolha == "s":
                    if heroi.sexo == "Feminino":
                        print('"Agora, dessa vez, tenta ficar viva, heroína... não quero ter que te aguentar de novo."') 
                        time.sleep(3)  # Espera 3 segundos
                        continue
                    else:
                        print('"Agora, dessa vez, tenta ficar vivo, heroizinho... não quero ter que ficar aguentando você de novo."')  
                        time.sleep(3)  # Espera 3 segundos
                        continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Sua inútil, eu estava quase chegando no meu objetivo, era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"') 
                        break
                    else:
                        print('"Seu inútil, eu estava quase chegando no meu objetivo e era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"') 
                        break
                else:
                    continue
            elif modo == U:
                escolha = input('"Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: "').capitalize()
                if escolha == "s":
                    print("Legal dessa vez vai dar certo!")
                    time.sleep(3)  # Espera 3 segundos
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print("Entendi...Valeu por jogar...perdedora")
                        break
                    else:
                        print("Entendi...Valeu por jogar...perdedor")
                        break
                else: 
                    continue
            else:
                escolha = input('"Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: "').capitalize()
                if escolha == "s":
                    print(f"Legal, vamos voltar {heroi.nome}")
                    time.sleep(3)  # Espera 3 segundos
                    continue
                elif escolha == "n":
                    print("Que decepção...")
                    break
                else:
                    continue
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
            if vida_inicial == 80 and modo == "f":
                escolha = input('"Sei que escolheu o modo infernal, mas não é ridículo morrer para um simples slime? Esquecendo quer continuar? Talvez seja melhor diminuir a dificuldade [S/N]: "').capitalize()
                if escolha == "s":
                    print('"Valeu e um conselho. Não morrer para um slime"')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Sério...Parece que você era uma fracote desde o início"')
                        break
                    else:
                        print('"Sério...Parece que você era um fracote desde o início"')
                        break
                else:
                    continue
            elif vida_inicial == 120 and modo == "f":
                escolha = input('"Sei que escolheu o modo padrão, mas não é ridículo morrer para um simples slime? Tipo você tinha capacidade de durar mais...Vamos tentar de novo! [S/N]: "').capitalize()
                if escolha == "s":
                    print('"Valeu e um conselho. Tomar poção se necessário"')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Parece que você era uma convarde desde o início"')
                        break
                    else:
                        print('"Parece que você era um convarde desde o início"')
                        break
                else:
                    continue
            elif vida_inicial == 150 and modo == "f":
                escolha = input('"Sei que escolheu o modo equilibrado, mas não é era necessário ser equilibrado também no dano e na cura? Todo mundo falhar...Porém vamos continuar! [S/N]: "').capitalize()
                if escolha == "s":
                    print('"Legal... vamos tentar de novo. Só que, da próxima vez, seria bom se não precisássemos começar tudo do zero."')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print("Ele apenas virou o rosto para o lado, sem dizer uma palavra, deixando claro que não se importava com sua decisão. Apenas seguiu com o seu caminho, como se nada tivesse acontecido.") 
                        break
                    else:
                        print("Ele apenas virou o rosto para o lado, sem dizer uma palavra, deixando claro que não se importava com sua decisão. Apenas seguiu com o seu caminho, como se nada tivesse acontecido.") 
                        break
                else:
                    continue
            elif vida_inicial == 250 and modo == "f":
                escolha = input('"Você escolheu o modo guerreiro, mas não! Tinha que ser morto por um slime! Um slime, sério? Vamos começar de novo logo, antes que eu perca mais tempo. [S/N]: "').capitalize()
                if escolha == "s":
                    if heroi.sexo == "Feminino":
                        print('"Agora, dessa vez, tenta ficar viva, heroína... não quero ter que te aguentar de novo."') 
                    else:
                        print('"Agora, dessa vez, tenta ficar vivo, heroizinho... não quero ter que ficar aguentando você de novo."')  
                        continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Sua inútil, eu estava quase chegando no meu objetivo, era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"') 
                        break
                    else:
                        print('"Seu inútil, eu estava quase chegando no meu objetivo e era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"') 
                        break
                else:
                    continue
            elif modo == U:
                escolha = input('"Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: "').capitalize()
                if escolha == "s":
                    print("Legal dessa vez vai dar certo!")
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print("Entendi...Valeu por jogar...perdedora")
                        break
                    else:
                        print("Entendi...Valeu por jogar...perdedor")
                        break
                else: 
                    continue
            else:
                escolha = input('"Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: "').capitalize()
                if escolha == "s":
                    print(f"Legal, vamos voltar {heroi.nome}")
                    continue
                elif escolha == "n":
                    print("Que decepção...")
                    break
                else:
                    continue
            
        escolha = 0
        while escolha != 1:
            escolha = int(input(f'"Parabéns {heroi.nome} por limpar nosso caminho para o tesouro e agora o que desejar fazer? 1° Continuar a aprofundar na caverna| 2° procurar poção| 3° sentar e afiar espada: "'))
                
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
            if vida_inicial == 80 and modo == "f":
                escolha = input("Mestre: Sei que escolheu o modo infernal, mas você sabia que teria de matar um Orc? Esquecendo disso quer continuar? Talvez seja melhor diminuir a dificuldade [S/N]: ").capitalize()
                if escolha == "s":
                    print('"Valeu e um conselho. Observe o Orc bem"')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Sério...Parece que você era uma fracote desde o início"')
                        break
                    else:
                        print('"Sério...Parece que você era um fracote desde o início"')
                        break
                else:
                    continue
            elif vida_inicial == 120 and modo == "f":
                escolha = input("Mestre: Sei que escolheu o modo padrão, mas não deveria ter tentando melhor contrar o Orc? Tipo você tinha capacidade de durar mais...Vamos tentar de novo! [S/N]: ").capitalize()
                if escolha == "s":
                    print('"Valeu e um conselho. Tomar poção se necessário"')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Parece que você era uma convarde desde o início"')
                        break
                    else:
                        print('"Parece que você era um convarde desde o início"')
                        break
                else:
                    continue
            elif vida_inicial == 150 and modo == "f":
                escolha = input(" Mestre: Sei que escolheu o modo equilibrado, mas não é era necessário ser equilibrado também no dano e na cura? Todo mundo falhar...Porém vamos continuar! [S/N]: ").capitalize()
                if escolha == "s":
                    print('"Legal... vamos tentar de novo. Só que, da próxima vez, seria bom se não precisássemos começar tudo do zero."')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print("Ele apenas virou o rosto para o lado, sem dizer uma palavra, deixando claro que não se importava com sua decisão. Apenas seguiu com o seu caminho, como se nada tivesse acontecido.") 
                        break
                    else:
                        print("Ele apenas virou o rosto para o lado, sem dizer uma palavra, deixando claro que não se importava com sua decisão. Apenas seguiu com o seu caminho, como se nada tivesse acontecido.") 
                        break
                else:
                    continue
            elif vida_inicial == 250 and modo == "f":
                escolha = input(" Mestre: Você escolheu o modo guerreiro, mas não! Tinha que ser morto por um Orc! Vamos começar de novo logo, antes que eu perca mais tempo. [S/N]: ").capitalize()
                if escolha == "s":
                    if heroi.sexo == "Feminino":
                        print('"Agora, dessa vez, tenta ficar viva, heroína... não quero ter que te aguentar de novo."') 
                    else:
                        print('"Agora, dessa vez, tenta ficar vivo, heroizinho... não quero ter que ficar aguentando você de novo."')  
                        continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Sua inútil, eu estava quase chegando no meu objetivo, era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"') 
                        break
                    else:
                        print('"Seu inútil, eu estava quase chegando no meu objetivo e era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"') 
                        break
                else:
                    continue
            elif modo == U:
                escolha = input(" Mestre: Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: ").capitalize()
                if escolha == "s":
                    print("Legal dessa vez vai dar certo!")
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print("Entendi...Valeu por jogar...perdedora")
                        break
                    else:
                        print("Entendi...Valeu por jogar...perdedor")
                        break
                else: 
                    continue
            else:
                escolha = input("Mestre: Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: ").capitalize()
                if escolha == "s":
                    print(f"Legal, vamos voltar {heroi.nome}")
                    continue
                elif escolha == "n":
                    print("Que decepção...")
                    break
                else:
                    continue
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
                                print(f"Esqueleto atacou {heroi.nome} e causou {dano} de dano!")
                                print(f'{heroi.nome} agora tem {heroi.vida} de vida.\n')
                        
                        turno1 += 1
                    if heroi.esta_vivo():
                        print('"Agora o necromante"')
                    else:
                        print(f"{esqueleto.nome} venceu!")
                            
                elif tentativa1 <= chance_ataque:
                    chance_esquiva = 20  # 20% de chance de desviar
                    tentativa = random.randint(1, 100)
                    if tentativa <= chance_esquiva:
                        print(f"{heroi.nome} desviou do ataque de {necromante.nome}!")
                    else:
                        print(f'"É tola tentativa de tentar me derrotar"')
                        dano = random.randint(1, 20)
                        heroi.vida -= dano
                        print(f"Necromante atacou {heroi.nome} e causou {dano} de dano!")
                        print(f'{heroi.nome} agora tem {heroi.vida} de vida.\n')    
                    
            turno += 1
        if heroi.esta_vivo():
            if heroi.sexo == "Feminino": # se o sexo for feminino
                print(f'"Você fez algo incrivel, grande {heroi.nome}"')
            else:
                print(f"Você fez algo incrivel, grandioso {heroi.nome}!")
            heroi.tentar_ganhar_pocao()
        else:
            print(f"{necromante.nome} venceu!") 
            if vida_inicial == 80 and modo == "f":
                escolha = input("Mestre: Sei que escolheu o modo infernal, mas você sabia que teria de matar um Necromante né? Esquecendo disso quer continuar? Talvez seja melhor diminuir a dificuldade [S/N]: ").capitalize()
                if escolha == "s":
                    print('"Valeu e um conselho. Tome cuidado com seus poderes"')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Sério...Parece que você era uma fracote desde o início"')
                        break
                    else:
                        print('"Sério...Parece que você era um fracote desde o início"')
                        break
                else:
                    continue
            elif vida_inicial == 120 and modo == "f":
                escolha = input("Mestre: Sei que escolheu o modo padrão, mas não deveria ter tentando melhor contrar o Necromante? Tipo você tinha capacidade de durar mais..., também ele era mais fraco de dano diferente do orc e ok vamos tentar de novo! [S/N]: ").capitalize()
                if escolha == "s":
                    print('"Valeu e um conselho. Tomar poção se necessário"')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Parece que você era uma convarde desde o início"')
                        break
                    else:
                        print('"Parece que você era um convarde desde o início"')
                        break
                else:
                    continue
            elif vida_inicial == 150 and modo == "f":
                escolha = input(" Mestre: Sei que escolheu o modo equilibrado, mas não é era necessário ser equilibrado também no dano e na cura? Todo mundo falhar...Porém vamos continuar! [S/N]: ").capitalize()
                if escolha == "s":
                    print('"Legal... vamos tentar de novo. Só que, da próxima vez, seria bom se não precisássemos começar tudo do zero."')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print("Ele apenas virou o rosto para o lado, sem dizer uma palavra, deixando claro que não se importava com sua decisão. Apenas seguiu com o seu caminho, como se nada tivesse acontecido.") 
                        break
                    else:
                        print("Ele apenas virou o rosto para o lado, sem dizer uma palavra, deixando claro que não se importava com sua decisão. Apenas seguiu com o seu caminho, como se nada tivesse acontecido.") 
                        break
                else:
                    continue
            elif vida_inicial == 250 and modo == "f":
                escolha = input(" Mestre: Você escolheu o modo guerreiro, mas não! Tinha que ser morto por um Necromante! Vamos começar de novo logo, antes que eu perca mais tempo. [S/N]: ").capitalize()
                if escolha == "s":
                    if heroi.sexo == "Feminino":
                        print('"Agora, dessa vez, tenta ficar viva, heroína... não quero ter que te aguentar de novo."') 
                    else:
                        print('"Agora, dessa vez, tenta ficar vivo, heroizinho... não quero ter que ficar aguentando você de novo."')  
                        continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Sua inútil, eu estava quase chegando no meu objetivo, era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"') 
                        break
                    else:
                        print('"Seu inútil, eu estava quase chegando no meu objetivo e era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"') 
                        break
                else:
                    continue
            elif modo == U:
                escolha = input(" Mestre: Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: ").capitalize()
                if escolha == "s":
                    print("Legal dessa vez vai dar certo!")
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print("Entendi...Valeu por jogar...perdedora")
                        break
                    else:
                        print("Entendi...Valeu por jogar...perdedor")
                        break
                else: 
                    continue
            else:
                escolha = input("Mestre: Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: ").capitalize()
                if escolha == "s":
                    print(f"Legal, vamos voltar {heroi.nome}")
                    continue
                elif escolha == "n":
                    print("Que decepção...")
                    break
                else:
                    continue
        
        heroi.tentar_ganhar_pocao()
        print(f'"Mas finalmente estamos chegando no nosso destino!"')
        print("Continuamos nos aprofundando na caverna até que finalmente nos aproximávamos de um grande portão feito de ouro.")
        print(f'"Finalmente chegamos no nosso destino!"'"O meu companheiro transparencia um sorriso grande.")
        print(f"{heroi.nome} firmou as mãos sobre a porta e empurrava as portas e no mesmo momento abria o portão.")
        print("Entravamos dentro da sala do tesouro, enquanto entrava dava para ver montes de dinheiro.")
        dragao = Personagem("Dragão",600,"monstro")
        dragao_dormindo = 0
        print('"Olha ali!"'"Ele se escondia atrás de uma pilastra e olhava para o dragão que estava adormecido."'"O que você quer fazer antes dele acordar?"')
        while dragao_dormindo < 100:
            escolha = int(input("1° Procurar uma nova espada| 2° Procurar poção| 3° Atacar o dragão | 4° Afiar a espada | 5° Treinar agilidade| 6° Desistir"))
            
            if escolha == 1:
                heroi.encontrar_espada()
                dragao_dormindo += 10
                
            elif escolha ==2: 
                heroi.tentar_ganhar_pocao()
                dragao_dormindo += 5
                
            elif escolha == 3:
                print('"O QUE VOCÊ FEZ?"')
                dragao_dormindo += 100
                dragao_vida -= heroi.dano_max
                print(f"{heroi.nome} atacou {dragao.nome} e causou {dano} de dano!")
                
            elif escolha == 4:
                print(f"{heroi.nome} se sentar é começar a afiar a espada")
                heroi.dano_max += 2
                dragao_dormindo += 2
                
            elif escolha == 5:
                print(f"{heroi.nome} começar a treinar")
                chance_esquiva += 5
                dragao_dormindo += 5
                
            elif escolha == 6:
                print("Meu companheiro parava na minha frente com os braços estendidos"'"VOCÊ NÃO VAI FUGIR!"')
                dragao_dormindo += 20
        print("De repente, um rugido profundo e estrondoso ecoou pela caverna, como um trovão que se aproximava. As paredes tremiam, e o ar ao nosso redor parecia vibrar com a força do som. Com um enorme estalo, as asas do dragão bateram, criando um vento tão forte que quase fomos derrubados. O monstro estava acordando.")
        print(f'O dragão abriu seus olhos, e sua voz, como o eco de uma montanha, preencheu a caverna.')
        print(f'"Quem ousa invadir meu domínio?!" Sua voz ressoava como um trovão distante, carregada de raiva e poder.Logo {heroi.nome} erguia a sua espada. "Vocês realmente acreditam que podem me enfrentar?"')
        print(f'Com um movimento lento, ele se levantou, suas escamas brilhando de forma ameaçadora, e olhou diretamente para nós, seu olhar cortante como fogo.')
        print(f'"Vocês estão no meu território agora. Não haverá misericórdia."')
        turno = 1
        while heroi.esta_vivo() and dragao.esta_vivo():
            acao = int(input("Deseja atacar (1) ou tomar poção (2)? "))
            if acao == 1: # atacar o dragão
                print(f"\n--- Turno {turno} ---")
                heroi.atacar(dragao)
        
            elif acao == 2: # beber poção
                heroi.tomar_pocao()
                
                 # orc ataca, se estiver vivo
            if dragao.esta_vivo():
                dano = random.randint(1, 100)
                tentativa = random.randint(1, 100)
                if tentativa <= chance_esquiva:
                    print(f"{heroi.nome} desviou do ataque de {dragao.nome}!")
                else:
                    heroi.vida -= dano
                    print(f"Dragão atacou {heroi.nome} e causou {dano} de dano!")
                    print(f'{heroi.nome} agora tem {heroi.vida} de vida.\n')    
            turno += 1
            
        if heroi.esta_vivo():
            print(f'"{heroi.nome} você...ganhou... de um Dragão!!!!!!"')
            
        else:
            print(f"{dragao.nome} venceu!")        
            if vida_inicial == 80 and modo == "f":
                escolha = input("Mestre: Sei que escolheu o modo infernal, mas você sabia que teria de matar um Dragão ancião!? Esquecendo disso quer continuar? Talvez seja melhor diminuir a dificuldade [S/N]: ").capitalize()
                if escolha == "s":
                    print('"Valeu e um conselho. Você tinha que ser mais forte"')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Sério...Parece que você era uma fracote desde o início"')
                        break
                    else:
                        print('"Sério...Parece que você era um fracote desde o início"')
                        break
                else:
                    continue
            elif vida_inicial == 120 and modo == "f":
                escolha = input("Mestre: Sei que escolheu o modo padrão, mas não deveria ter como você fica mais forte? Tipo você tinha capacidade de durar mais...Vamos tentar de novo! [S/N]: ").capitalize()
                if escolha == "s":
                    print('"Valeu e um conselho. Tomar poção se necessário"')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Parece que você era uma convarde desde o início"')
                        break
                    else:
                        print('"Parece que você era um convarde desde o início"')
                        break
                else:
                    continue
            elif vida_inicial == 150 and modo == "f":
                escolha = input(" Mestre: Sei que escolheu o modo equilibrado, mas não é era necessário ser equilibrado também no dano e na cura? Todo mundo falhar...Porém vamos continuar! [S/N]: ").capitalize()
                if escolha == "s":
                    print('"Legal... vamos tentar de novo. Só que, da próxima vez, seria bom se não precisássemos começar tudo do zero."')  
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print("Ele apenas virou o rosto para o lado, sem dizer uma palavra, deixando claro que não se importava com sua decisão. Apenas seguiu com o seu caminho, como se nada tivesse acontecido.") 
                        break
                    else:
                        print("Ele apenas virou o rosto para o lado, sem dizer uma palavra, deixando claro que não se importava com sua decisão. Apenas seguiu com o seu caminho, como se nada tivesse acontecido.") 
                        break
                else:
                    continue
            elif vida_inicial == 250 and modo == "f":
                escolha = input(" Mestre: Você escolheu o modo guerreiro, mas não! Tinha que ser morto por um Dragão! Vamos começar de novo logo, antes que eu perca mais tempo. [S/N]: ").capitalize()
                if escolha == "s":
                    if heroi.sexo == "Feminino":
                        print('"Agora, dessa vez, tenta ficar viva, heroína... não quero ter que te aguentar de novo."') 
                    else:
                        print('"Agora, dessa vez, tenta ficar vivo, heroizinho... não quero ter que ficar aguentando você de novo."')  
                        continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print('"Sua inútil, eu estava quase chegando no meu objetivo, era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"') 
                        break
                    else:
                        print('"Seu inútil, eu estava quase chegando no meu objetivo e era só você abrir o caminho e depois eu te mataria para ter meu tesouro, mas você falhou!"') 
                        break
                else:
                    continue
            elif modo == U:
                escolha = input(" Mestre: Que pena...Mas você deveria ter escolhido uma vida maior. Esquecendo isso..Quer continuar? [S/N]: ").capitalize()
                if escolha == "s":
                    print("Legal dessa vez vai dar certo!")
                    continue
                elif escolha == "n":
                    if heroi.sexo == "Feminino":
                        print("Entendi...Valeu por jogar...perdedora")
                        break
                    else:
                        print("Entendi...Valeu por jogar...perdedor")
                        break
                else: 
                    continue
            else:
                escolha = input("Mestre: Valeu por tentar jogar, mas agora quer tentar de novo? [S/N]: ").capitalize()
                if escolha == "s":
                    print(f"Legal, vamos voltar {heroi.nome}")
                    continue
                elif escolha == "n":
                    print("Que decepção...")
                    break
                else:
                    continue

jogar()
