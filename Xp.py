# Função que retorna o XP máximo necessário para o nível específico
def calcular_xp_max(nivel):
    tabela_xp = [
        0,      # Nível 1
        300,    # Nível 2
        900,    # Nível 3
        2700,   # Nível 4
        6500,   # Nível 5
        14000,  # Nível 6
        23000,  # Nível 7
        34000,  # Nível 8
        48000,  # Nível 9
        64000,  # Nível 10
        85000,  # Nível 11
        100000, # Nível 12
        120000, # Nível 13
        140000, # Nível 14
        165000, # Nível 15
        195000, # Nível 16
        225000, # Nível 17
        265000, # Nível 18
        305000, # Nível 19
        355000  # Nível 20
    ]

    if nivel <= 20:
        return tabela_xp[nivel - 1]
    
    # Extrapolação para níveis acima de 20
    xp_max = int(355000 * (1.1 ** (nivel - 20)))  # Aumento de 10% por nível após o nível 20
    return xp_max

# Função para calcular o XP faltando para o próximo nível
def calcular_faltando(nivel, xp_atual):
    xp_max_atual = calcular_xp_max(nivel)
    xp_max_proximo = calcular_xp_max(nivel + 1)

    faltando = xp_max_proximo - xp_atual
    
    if xp_atual >= xp_max_atual:
        return 0
    
    if faltando < 0:
        return 0
    
    return faltando
