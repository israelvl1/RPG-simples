from Personagem import *  # Importando a classe base

class Aliado(Personagem):
    def __init__(self, nome, vida, sexo, classe, nivel=1, xp_atual=0):
        super().__init__(nome, vida, sexo, classe, nivel, xp_atual)
        self.moral = 0          # Pode variar de -10 a +10, por exemplo
        self.afeto = 0          # Pode variar de -10 a +10 também
        self.fugiu = False
        self.traidor = False
        self.ativo = True

    def receber_bonus_temporario(self, moral_bonus=0, ataque_bonus=0, dano_bonus=0, defesa_bonus=0, duracao=1):
        if self.turnos_bonus == 0 and duracao > 0:
            if moral_bonus:
                self.moral += moral_bonus
            if ataque_bonus or dano_bonus:
                self.bonus_ataque += ataque_bonus + dano_bonus
            if defesa_bonus:
                self.bonus_defesa += defesa_bonus
            self.turnos_bonus = duracao
            print(f"{self.nome} recebeu bônus por {duracao} turno(s)!")
    
        elif self.turnos_bonus > 0:
        self.turnos_bonus -= 1
            print(f"{self.nome} ainda tem bônus por {self.turnos_bonus} turno(s).")
            if self.turnos_bonus == 0:
                print(f"⏳ Os bônus de {self.nome} acabaram!")
                self.bonus_ataque = 0
                self.bonus_defesa = 0
            
        
    def atualizar_imunidade(self):
        if hasattr(self, "turnos_imune") and self.turnos_imune > 0:
            self.turnos_imune -= 1
            if self.turnos_imune == 0:
                self.imune_status = False
                print(f"{self.nome} não está mais imune a status negativos.")
