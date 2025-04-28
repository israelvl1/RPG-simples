# onde vai conter todas as habilidades ativas

def manobra_estrategica(self, alvo, nova_posicao):
        
    """
    Reposiciona um aliado ou inimigo no campo de batalha.
    :param alvo: Instância de Personagem a ser reposicionada.
    :param nova_posicao: Tupla com as coordenadas para reposicionar (x, y).
    """
    print(f"{self.nome} usa Manobra Estratégica em {alvo.nome}!")
    alvo.posicao = nova_posicao
    print(f"{alvo.nome} foi movido para {nova_posicao}.")
