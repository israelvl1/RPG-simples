def obter_classe_inicial(self):
    from Classes import classes
    return classes.get(self.classe, {}).get("classe_inicial", "")
    
def ameacar(self, inimigo):
    self.inimigos_ameacados.add(inimigo)
    print(f"{self.nome} está ameaçando {inimigo.nome}.")
    
def ataque_coordenado(aliado, mestre, inimigo):
    """
    Aplica bônus de ataque se o inimigo estiver sendo ameaçado por um Mestre de Batalha.
    """
    if mestre.classe_inicial == "Mestre de Batalha" and inimigo in mestre.inimigos_ameacados:
        bonus_dano = 2
        dano = random.randint(1, aliado.dano_max) + bonus_dano
        print(f"{aliado.nome} realiza um Ataque Coordenado com {mestre.nome}!")
    else:
        dano = random.randint(1, aliado.dano_max)
        print(f"{aliado.nome} ataca {inimigo.nome} normalmente.")

    inimigo.vida -= dano
    print(f"{aliado.nome} causou {dano} de dano em {inimigo.nome}!")

def liderar_ataque(self, inimigos):
    """
    Passiva: aumenta temporariamente a resistência ao liderar um ataque.
    """

    if self.obter_classe_inicial() not in ["Mestre de Batalha", "Comandante de Vanguarda"]:
        print(f"❌ {self.nome} não pode usar essa habilidade! Ela é exclusiva do Mestre de Batalha ou suas subclasses.")
        return

    print(f"\n{self.nome} está liderando o ataque!")

    # Passiva: resistência temporária durante o ataque
    self.aumentar_resistencia(self.resistencia_extra)
    print(f"Força de Vanguarda (passiva): resistência temporariamente aumentada para {self.resistencia}.")

    for inimigo in inimigos:
        self.atacar(inimigo)

    # Após o ataque, remove o bônus da passiva, mas mantém o da ativa
    self.reduzir_resistencia(self.resistencia_extra)
    print(f"Fim do ataque: resistência restaurada para {self.resistencia}.")
    
def aumentar_bonus_inspiracao(self, aliado, bonus_ataque=0, bonus_defesa=0, duracao=0):
    """
    Aplica bônus temporário a um aliado. Disponível para Mestre de Batalha e suas subclasses.
    """

    if self.obter_classe_inicial() not in ["Mestre de Batalha", "Comandante de Vanguarda"]:
        print(f"❌ {self.nome} não pode usar essa habilidade! Ela é exclusiva do Mestre de Batalha ou suas subclasses.")
        return

    if duracao > 0:
        aliado.dano_max += bonus_ataque
        aliado.defesa = getattr(aliado, "defesa", 0) + bonus_defesa
        aliado.turnos_bonus = duracao
        print(f"✅ {self.nome} inspira {aliado.nome}, concedendo +{bonus_ataque} de ataque e +{bonus_defesa} de defesa por {duracao} turnos.")
        
def lideranca_imbativel(self, aliado, dano_original):
    """
    Habilidade passiva do Mestre de Batalha e subclasses:
    Reduz o dano recebido por um aliado e o torna imune a status negativos temporariamente.
    """
    if self.obter_classe_inicial() not in ["Mestre de Batalha", "Comandante de Vanguarda"]:
        print(f"❌ {self.nome} não pode usar essa habilidade! Ela é exclusiva do Mestre de Batalha ou suas subclasses.")
        return

    resistencia = 0.4  # 40% de redução de dano
    duracao_turnos = 2

    # Reduz o dano
    dano_reduzido = dano_original * (1 - resistencia)
    aliado.vida -= dano_reduzido
    if aliado.vida < 0:
        aliado.vida = 0

    # Imunidade temporária a efeitos negativos
    aliado.imune_status = True
    aliado.turnos_imune = duracao_turnos

    print(f"🛡️ {self.nome} usa Liderança Imbatível!")
    print(f"{aliado.nome} agora ignora efeitos negativos por {duracao_turnos} turnos.")
    print(f"Dano original: {dano_original} → Dano reduzido: {dano_reduzido:.1f}")
    print(f"Vida atual de {aliado.nome}: {aliado.vida:.1f}")
