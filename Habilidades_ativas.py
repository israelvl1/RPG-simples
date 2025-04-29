def obter_classe_inicial(self):
    from Classes import classes
    return classes.get(self.classe, {}).get("classe_inicial", "")
    
def Manobra_estrategica(self, alvo, nova_posicao):
    """Reposiciona um aliado ou inimigo no campo de batalha."""
    if not isinstance(self, MestreDeBatalha):  # Verifica se é Mestre de Batalha ou subclasse
        print(f"{self.nome} não pode usar essa habilidade, ela é exclusiva do Mestre de Batalha ou suas subclasses!")
        return
        
    print(f"{self.nome} usa Manobra Estratégica em {alvo.nome}!")
    alvo.posicao = nova_posicao
    print(f"{alvo.nome} foi movido para {nova_posicao}.")
    
def Controle_da_zona(self, inimigos):
    """Ativa Controle da Zona, afetando inimigos ao redor."""
    if not isinstance(self, MestreDeBatalha):  # Verifica se é Mestre de Batalha ou subclasse
        print(f"{self.nome} não pode usar essa habilidade, ela é exclusiva do Mestre de Batalha ou suas subclasses!")
        return

    print(f"{self.nome} ativa Controle da Zona!")
    self.zona_ativa = True
    for inimigo in inimigos:
        inimigo.reduzir_mobilidade()
        inimigo.reduzir_precisao()
        
def grito_de_guerra(self, aliados, duracao_turnos=2):
    """Ativa o Grito de Guerra, dando bônus aos aliados."""
    if self.obter_classe_inicial() not in ["Mestre de Batalha", "Comandante de Vanguarda"]:
        print(f"{self.nome} não pode usar essa habilidade, ela é exclusiva do Mestre de Batalha ou suas subclasses!")
        return
    
    print(f"{self.nome} usa Grito de Guerra!")
    for aliado in aliados:
        aliado.receber_bonus_temporario(moral_bonus=5, ataque_bonus=3, duracao=duracao_turnos)

def impulso_de_ataque(self, aliados, raio, duracao_turnos):
    """Ativa Impulso de Ataque, aumentando o dano dos aliados ao redor."""
    if self.obter_classe_inicial() not in ["Mestre de Batalha", "Comandante de Vanguarda"]:
        print(f"{self.nome} não pode usar essa habilidade, ela é exclusiva do Mestre de Batalha ou suas subclasses!")
        return

    print(f"{self.nome} usa Impulso de Ataque!")
    for aliado in aliados:
        aliado.receber_bonus_temporario(dano_bonus=5, duracao=duracao_turnos)
        
def ativar_forca_de_vanguarda(self):
    """
    Habilidade ativa: aumenta a resistência enquanto estiver ativa.
    """
    if self.obter_classe_inicial() not in ["Mestre de Batalha", "Comandante de Vanguarda"]:
        print(f"{self.nome} não pode usar essa habilidade.")
        return
    if not self.forca_de_vanguarda_ativa:
        self.aumentar_resistencia(self.resistencia_extra)
        self.forca_de_vanguarda_ativa = True
        print(f"{self.nome} ativou Força de Vanguarda! Resistência aumentada para {self.resistencia}.")
    else:
        print(f"{self.nome} já está com Força de Vanguarda ativa.")
        
def ataque_devastador(self, inimigos):
    """
    Habilidade ativa do Comandante de Vanguarda:
    Causa grande dano a todos os inimigos ao redor.
    """
    if self.obter_classe_inicial() not in ["Mestre de Batalha", "Comandante de Vanguarda"]:
        print(f"❌ {self.nome} não pode usar 'Ataque Devastador'. Habilidade exclusiva do Comandante de Vanguarda!")
        return

    print(f"\n🔥 {self.nome} usa ATAQUE DEVASTADOR!")

    for inimigo in inimigos:
        dano = random.randint(int(self.dano_max * 0.8), self.dano_max + 10)
        inimigo.vida -= dano
        if inimigo.vida < 0:
            inimigo.vida = 0
        print(f"💥 {inimigo.nome} sofreu {dano} de dano! Vida restante: {inimigo.vida}")
