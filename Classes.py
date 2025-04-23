classes = {
    "Guerreiro": {
        "nivel_evolucao": 1,
        "desc": "O guerreiro é uma classe de combatente versátil, mestre das armas e da tática. Ele se destaca em combate físico, seja em combate corpo a corpo ou à distância, sendo capaz de usar uma variedade de armas e armaduras.",
        "pode_evoluir": ["Mestre de Batalha", "Campeão", "Cavaleiro Eldritch", "Guerreiro Psíquico", "Arqueiro Arcano", "Cavaleiro", "Samurai", "Banneret", "Rune Knight", "Echo Knight"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Força": 2, "Constituição": 2}
    },
    "Mestre de Batalha": {
        "nivel_evolucao": 3,
        "desc": "Um guerreiro tático que usa manobras especiais para controlar o campo de batalha.",
        "pode_evoluir": ["Comandante de Vanguarda","Tático das Sombras","Mestre do Cerco","Veterano da Arena","Estrategista Elemental","Condutor de Falange","Arquiteto da Guerra","Executor Implacável","Marionetista de Guerra"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Força": 2, "Destreza": 1}
    },
    "Comandante de Vanguarda": {
        "nivel_evolucao": 7,
        "desc": "Especialista em liderar o ataque, esse mestre inspira aliados com gritos de guerra e toma a frente da batalha com táticas ofensivas agressivas.",
        "classe_inicial": "Mestre de Batalha",
        "bonus": {"Força": 2, "Carisma": 1},
        "pode_evoluir": ["Comandante Supremo", "Tornado de Guerra"],
        "habilidades": [
            "Grito de Guerra: Aumenta o moral e a força de ataque dos aliados próximos, inspirando-os a lutar com mais ferocidade.",
            "Impulso de Ataque: Fornece um bônus temporário de dano a todos os aliados dentro de um raio específico, incentivando-os a atacar com mais intensidade.",
            "Força de Vanguarda: Garante que o comandante seja mais resistente ao dano enquanto lidera o ataque, funcionando como um 'tanque' que absorve danos para proteger seus aliados."
        ]
    },
    "Comandante Supremo": {
        "nivel_evolucao": 13,
        "desc": "Evolução para um líder ainda mais inspirador e formidável, com a capacidade de melhorar ainda mais os bônus que ele dá aos aliados.",
        "classe_inicial": "Comandante de Vanguarda",
        "bonus": {"Carisma": 2, "Inteligência": 1},
        "pode_evoluir": [null],
        "habilidades": [
                "Aumentar Bônus de Inspiração: Aumenta os efeitos das habilidades que inspiram e fortalecem os aliados, melhorando o bônus de ataque e defesa em combate.",
                "Liderança Imbatível: Dá aos aliados próximos uma resistência significativa ao dano, além de permitir que eles ignorem status negativos por um tempo limitado."
        ]
    },
    "Tornado de Guerra": {
        "desc": "A evolução torna o comandante mais agressivo, liderando ataques devastadores que afetam o campo de batalha.",
        "classe_inicial": "Comandante de Vanguarda",
        "bonus": {"Força": 2, "Destreza": 1},
        "pode_evoluir": [null],
        "habilidades": [
                 "Ataque Devastador: Permite ao comandante realizar ataques massivos em área, causando grande dano a todos os inimigos ao redor.",
                 "Grito de Guerra Aprimorado: Aumenta a eficácia do Grito de Guerra, proporcionando mais força de ataque e aumentando a moral dos aliados por mais tempo."
        ]
    },
    "Tático das Sombras": {
        "nivel_evolucao": 7,
        "desc": "Um estrategista que usa o campo de batalha a seu favor com furtividade e manipulação. Mestre em emboscadas e movimentos táticos sorrateiros.",
        "classe_inicial": "Mestre de Batalha",
        "bonus": {"Destreza": 2, "Inteligência": 1},
        "pode_evoluir": ["Sombra Mortal", "Lâmina Silenciosa"],
        "habilidades": [
            "Furtividade Avançada: Permite ao Tático se mover sem ser detectado, tornando-o invisível por curtos períodos, o que lhe permite escapar de perigos ou se posicionar para um ataque surpresa.",
            "Emboscada Mortal: Garante dano extra ao atacar inimigos desprevenidos, aproveitando a falta de defesa do oponente.",
            "Manipulação de Terreno: Cria áreas de sombra que dificultam a visão inimiga e confundem o campo de batalha, permitindo emboscadas e evasão."
        ]
    },
    "Sombra Mortal": {
        "desc": "O Tático das Sombras se torna uma sombra ambulante, capaz de causar grandes danos enquanto permanece invisível ou difícil de ser detectado.",
        "classe_inicial": "Tático das Sombras",
        "bonus": {"Destreza": 2, "Inteligência": 1},
        "pode_evoluir": [null],
        "habilidades": [
                "Invisibilidade Avançada: Aumenta a duração da invisibilidade e reduz a chance de detecção, permitindo movimentos furtivos com maior liberdade.",
                "Ataque Fatal: Aumenta o dano de ataques furtivos contra inimigos desprevenidos, causando danos massivos ao atingir pontos fracos."
        ]
    },
    "Lâmina Silenciosa": {
        "desc": "Evolução que torna o Tático das Sombras mais letal em ataques furtivos, além de ganhar habilidades de manipulação mental em combate.",
        "classe_inicial": "Tático das Sombras",
        "bonus": {"Destreza": 2, "Carisma": 1},
        "pode_evoluir": [null],
        "habilidades": [
                "Manipulação Psíquica: Permite ao Tático manipular as mentes dos inimigos próximos, confundindo-os e forçando-os a agir de maneira errada.",
                "Ataque Silencioso Aprimorado: Melhora a habilidade de ataques furtivos, causando dano extra e debilitando os inimigos afetados, reduzindo sua capacidade de defesa."
        ]
    },
    "Mestre do Cerco": {
        "nivel_evolucao": 7,
        "desc": "Um guerreiro treinado para combates em larga escala e destruição de estruturas. Especialista em táticas de guerra de cerco e uso de armamento pesado.",
        "classe_inicial": "Mestre de Batalha",
        "bonus": {"Força": 2, "Constituição": 1},
        "pode_evoluir": ["Destruidor Imparável", "Mestre das Máquinas"],
        "habilidades": [
            "Aríete Imortal: Um ataque de cerco que destrói as defesas inimigas e causa dano massivo a estruturas e unidades inimigas.",
            "Catapulta de Fogo: Lança projéteis incendiários em áreas grandes, causando dano em área e queimando inimigos e estruturas ao redor.",
            "Resistência de Cerco: Aumenta a resistência a ataques de longo alcance e danos físicos, permitindo ao Mestre do Cerco resistir a embates prolongados durante a batalha."
        ]
    },
    "Destruidor Imparável": {
        "desc": "Foco em aumentar a destruição e a resistência em combate, permitindo ao Mestre do Cerco destruir fortificações e esmagar inimigos com força bruta.",
        "classe_inicial": "Mestre do Cerco",
        "bonus": {"Força": 3, "Constituição": 1},
        "pode_evoluir": [null],
        "habilidades": [
                "Destruição Total: Permite ao Mestre do Cerco causar dano massivo em estruturas inimigas, derrubando defesas e deixando o campo de batalha aberto para ataques subsequentes.",
                "Invulnerabilidade Temporária: Concede uma camada de invulnerabilidade temporária ao Mestre do Cerco, permitindo que ele absorva danos sem ser afetado por um curto período."
        ]
    },
    "Mestre das Máquinas": {
        "desc": "Focado em utilizar ferramentas de cerco, como catapultas e aríetes, e até mesmo em comandar máquinas de guerra.",
        "classe_inicial": "Mestre do Cerco",
        "bonus": {"Inteligência": 2, "Força": 1},
        "pode_evoluir": [null],
        "habilidades": [
                "Controle de Máquinas: Permite ao Mestre do Cerco controlar máquinas de guerra com precisão, como catapultas, aríetes e balistas, causando dano em larga escala.",
                "Mestre das Armas de Cerco: Aumenta a eficácia das armas de cerco, reduzindo o tempo de recarga e aumentando o dano causado a estruturas e unidades inimigas."
        ]
    },
    "Veterano da Arena": {
        "nivel_evolucao": 7,
        "desc": "Forjado em combate individual e em batalhas públicas, esse mestre é um duelista brutal e imprevisível.",
        "classe_inicial": "Mestre de Batalha",
        "bonus": {"Força": 2, "Sabedoria": 1},
        "pode_evoluir": ["Gladiador Supremo", "Ferro e Fogo"],
        "habilidades": [
            "Golpe Preciso: Aumenta a chance de acertos críticos e o dano em duelos, tornando o Veterano da Arena uma força devastadora em combate individual.",
            "Desvio Impecável: Permite ao veterano evitar um ataque com maestria, utilizando sua experiência de combate para desviar com facilidade.",
            "Ataque Frenético: Aumenta a velocidade de ataque por um curto período, permitindo combos rápidos e ataques contínuos."
        ]
    },
    "Gladiador Supremo": {
        "desc": "O Veterano da Arena se torna um mestre imbatível em combates 1x1, invencível e com ataques que exploram fraquezas dos oponentes.",
        "classe_inicial": "Veterano da Arena",
        "bonus": {"Força": 3, "Sabedoria": 1},
        "pode_evoluir": [null],
        "habilidades": [
                "Exploitar Fraquezas: Permite ao Gladiador identificar e explorar as fraquezas do inimigo, causando danos adicionais e quebrando defesas inimigas.",
                "Ataques Imparáveis: Dá ao Gladiador a capacidade de realizar ataques imbatíveis, ignorando armaduras e resistências de inimigos por um período curto."
        ]
    },
    "Ferro e Fogo": {
        "desc": "Especializa-se em usar armas e habilidades de combate em uma combinação brutal de ataque físico e mágico.",
        "classe_inicial": "Veterano da Arena",
        "bonus": {"Força": 2, "Inteligência": 1},
        "pode_evoluir": [null],
        "habilidades": [
                "Golpes Elementais: Permite ao Veterano usar ataques elementais junto com suas habilidades físicas, causando dano adicional baseado em fogo, gelo ou eletricidade.",
                "Combate Mágico Aprimorado: Aprimora o uso de magia no combate, permitindo conjurações rápidas e eficazes, mesmo durante ataques físicos."
        ]
    },
    "Estrategista Elemental": {
        "desc": "Um mestre de batalha que estudou como manipular elementos naturais em suas táticas. Mistura combate físico com efeitos mágicos sutis e estratégicos.",
        "classe_inicial": "Mestre de Batalha",
        "bonus": {"Inteligência": 2, "Força": 1},
        "pode_evoluir": ["Mestre Elemental", "Chamado da Tempestade"],
        "habilidades": [
            "Magia de Combate: Mistura feitiços elementares com ataques físicos, aumentando o dano e causando efeitos adicionais baseados nos elementos (fogo, água, vento, terra).",
            "Campo Elemental: Cria um campo ao redor do comandante que altera o terreno e afeta os inimigos com um dos quatro elementos, podendo causar dano ou aplicar debuffs.",
            "Escudo Elemental: Protege aliados próximos com uma barreira de energia elemental, aumentando sua resistência a danos e controlando os efeitos do campo."
        ]
    },
    "Mestre Elemental": {
        "desc": "O Estrategista Elemental alcança domínio absoluto sobre os elementos, podendo invocar e manipular os elementos de forma mais poderosa.",
        "classe_inicial": "Estrategista Elemental",
        "bonus": {"Inteligência": 3, "Força": 1},
        "pode_evoluir": [null],
        "habilidades": [
                "Invocação Elemental Avançada: Permite ao Estrategista invocar criaturas elementares poderosas para lutar ao seu lado e controlar os elementos de maneira mais efetiva.",
                "Controle Elemental: Aumenta o controle sobre os elementos naturais, podendo manipular o fogo, a água, a terra e o vento para criar barreiras, causar dano e controlar o campo de batalha."
        ]
    },
    "Chamado da Tempestade": {
        "desc": "Habilidade de conjurar tempestades elementais e usar os poderes da natureza para desferir ataques devastadores.",
        "classe_inicial": "Estrategista Elemental",
        "bonus": {"Sabedoria": 2, "Inteligência": 1},
        "pode_evoluir": [null],
        "habilidades": [
                "Tempestade de Raios: Invoca uma tempestade que descarrega raios nos inimigos, causando dano massivo em área e deixando-os atordoados.",
                "Fúria dos Elementos: Desencadeia uma série de ataques elementares que arrasam as fileiras inimigas, causando dano e criando condições desfavoráveis para os oponentes."
        ]
    },
    "Condutor de Falange": {
        "desc": "Especializado em combate em grupo e formação defensiva, lidera aliados como uma unidade só, transformando um grupo em uma muralha viva.",
        "classe_inicial": "Mestre de Batalha",
        "bonus": {"Constituição": 2, "Carisma": 1},
        "pode_evoluir": ["Falange Imbatível", "Guardião da Legião"],
        "habilidades": [
            "Formação Blindada: Cria uma formação defensiva onde os aliados recebem redução de dano, tornando-se mais difíceis de serem derrotados.",
            "Comando de Falange: Ordena um ataque coordenado que causa dano em área aos inimigos dentro do alcance, com todos os aliados agindo em uníssono.",
            "Defesa Inquebrável: Aumenta a resistência a danos de todos os aliados próximos quando em formação, criando uma linha de defesa impenetrável."
        ]
    },
    "Falange Imbatível": {
    "desc": "A evolução definitiva do Condutor de Falange. Transforma o grupo em uma fortaleza ambulante, com sinergia defensiva extrema.",
    "classe_inicial": "Condutor de Falange",
    "bonus": { "Constituição": 2, "Sabedoria": 1 },
    "pode_evoluir": [null],
    "habilidades": [
      "Muralha Viva: Torna aliados praticamente imunes a ataques frontais enquanto estiverem em formação.",
      "Barreira Inquebrável: Cria um escudo coletivo que reduz dano mágico e bloqueia controle por um tempo limitado."
        ]
    },
    "Guardião da Legião": {
    "desc": "Focado em proteger aliados com táticas defensivas avançadas e inspirar resistência mesmo nas piores situações.",
    "classe_inicial": "Condutor de Falange",
    "bonus": { "Carisma": 2, "Constituição": 1 },
    "pode_evoluir": [null],
    "habilidades": [
      "Proteção Coletiva: Parte do dano de aliados é transferida para o Guardião, que o absorve com resistência aumentada.",
      "Juramento de Ferro: Torna aliados vulneráveis temporariamente imunes a dano fatal."
       ]
     },
    "Arquiteto da Guerra": {
        "desc": "Um planejador nato que transforma o campo de batalha em um tabuleiro. Capaz de alterar o terreno, criar armadilhas e manipular posicionamento.",
        "classe_inicial": "Mestre de Batalha",
        "bonus": {"Inteligência": 2, "Sabedoria": 1},
        "pode_evoluir": ["Construtor de Caos", "Mestre das Armadilhas"],
        "habilidades": [
            "Terreno Manipulado: Muda o terreno, criando obstáculos ou zonas de vantagem para a própria equipe, alterando o campo de batalha para controlar o fluxo do combate.",
            "Armadilha Explosiva: Coloca armadilhas que detonam quando inimigos passam por elas, causando dano em área e desorganizando as fileiras inimigas.",
            "Posicionamento Estratégico: Aumenta o poder de ataque e defesa de aliados em uma área ao redor de pontos-chave, otimizando as posições para maximizar a eficácia do time."
        ]
    },
    "Construtor de Caos": {
    "desc": "Transcende o papel de arquiteto e se torna um controlador absoluto do campo, usando o ambiente para causar destruição e desordem total.",
    "classe_inicial": "Arquiteto da Guerra",
    "bonus": { "Inteligência": 2, "Carisma": 1 },
    "pode_evoluir": [null],
    "habilidades": [
      "Colapso Programado: Detona zonas manipuladas do terreno, causando dano em área e desorientando inimigos.",
      "Campo Caótico: Cria um ambiente instável onde habilidades e movimentações inimigas têm chance de falhar."
      ]
     },
    "Mestre das Armadilhas": {
    "desc": "Aprofunda-se na arte das armadilhas, tornando o campo de batalha um labirinto letal para os desavisados.",
    "classe_inicial": "Arquiteto da Guerra",
    "bonus": { "Inteligência": 2, "Destreza": 1 },
    "pode_evoluir": [null],
    "habilidades": [
      "Rede de Armadilhas: Instala múltiplas armadilhas ocultas que se ativam por proximidade ou comando.",
      "Engenharia de Batalha: Reduz o tempo de preparo e aumenta o alcance e eficácia das armadilhas."
      ]
    },
    "Executor Implacável": {
        "desc": "Um mestre que se especializou em eliminar alvos prioritários rapidamente e com precisão cirúrgica.",
        "classe_inicial": "Mestre de Batalha",
        "bonus": {"Destreza": 2, "Força": 1},
        "pode_evoluir": ["Assassino Imparável", "Sentença Final"],
        "habilidades": [
            "Golpe Mortal: Aumenta significativamente o dano contra um único alvo, focando no inimigo mais importante ou vulnerável.",
            "Execução Rápida: Permite eliminar um inimigo crítico em um golpe de precisão, oferecendo uma maneira de eliminar rapidamente alvos prioritários.",
            "Foco Letal: Concentra a mente para garantir um acerto fatal em inimigos com pouca vida, tornando-os alvos fáceis para o Executor."
        ]
    },
    "Assassino Imparável": {
    "desc": "Um especialista em eliminação que executa alvos com velocidade e brutalidade, quase impossível de deter quando em ação.",
    "classe_inicial": "Executor Implacável",
    "bonus": { "Destreza": 2, "Força": 1 },
    "pode_evoluir": [null],
    "habilidades": [
      "Cadência Letal: Permite múltiplas execuções em sequência se os inimigos forem eliminados rapidamente.",
      "Sombras Velozes: Aumenta drasticamente a mobilidade após uma execução, permitindo reposicionamento imediato."
      ]
    },
    "Sentença Final": {
    "desc": "Transforma o Executor em um juiz do campo de batalha, cuja presença impõe medo e cuja lâmina traz o fim inevitável.",
    "classe_inicial": "Executor Implacável",
    "bonus": { "Carisma": 2, "Destreza": 1 },
    "pode_evoluir": [null],
    "habilidades": [
      "Veredito Imediato: Executa automaticamente inimigos com menos de certa porcentagem de vida.",
      "Golpe Final: Um ataque devastador que ignora armadura e causa dano crítico absoluto."
      ]
    },
    "Marionetista de Guerra": {
        "desc": "Um mestre de batalha que manipula o inimigo como peças em um tabuleiro, forçando movimentos, trocando posições e desorientando.",
        "classe_inicial": "Mestre de Batalha",
        "bonus": {"Inteligência": 2, "Carisma": 1},
        "pode_evoluir": ["Domínio Psíquico", "Teatro da Guerra"],
        "habilidades": [
            "Controle Mental: Controla a mente de um inimigo, forçando-o a agir em seu favor por um curto período, transformando-o em uma ferramenta contra seus próprios aliados.",
            "Troca de Posições: Troca de lugar com um inimigo ou aliado, causando confusão nas linhas inimigas e alterando o posicionamento no campo de batalha.",
            "Desorientação Psíquica: Faz com que os inimigos próximos percam a capacidade de coordenar ataques corretamente, gerando caos e ineficiência nas fileiras inimigas."
        ]
    },
    "Domínio Psíquico": {
    "desc": "Aprofunda-se no controle mental e manipulação, tornando-se um mestre do caos psíquico no campo de batalha.",
    "classe_inicial": "Marionetista de Guerra",
    "bonus": { "Inteligência": 3 },
    "pode_evoluir": [null],
    "habilidades": [
      "Controle Total: Prolonga o controle mental e permite forçar inimigos a usar habilidades contra seus aliados.",
      "Corrupção Psíquica: Envenena a mente do inimigo, causando dano contínuo e bloqueando habilidades."
        ]
    },
    "Teatro da Guerra": {
    "desc": "Transcende a manipulação individual e passa a coordenar o caos como um diretor de uma peça sangrenta no campo de batalha.",
    "classe_inicial": "Marionetista de Guerra",
    "bonus": { "Carisma": 2, "Inteligência": 1 },
    "pode_evoluir": [null],
    "habilidades": [
      "Cenário Ilusório: Cria ilusões em larga escala que enganam os inimigos e alteram suas rotas.",
      "Direção Oculta: Dá comandos secretos aos aliados, permitindo ações sincronizadas fora da percepção inimiga."
        ]
    },
    "Campeão": {
        "desc": "Um guerreiro resiliente com habilidades aprimoradas em combate físico.",
        "pode_evoluir": ["Cavaleiro", "Guerreiro Psíquico", "Samurai"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Força": 2, "Constituição": 1}
    },
    "Cavaleiro Eldritch": {
        "desc": "Um guerreiro que combina combate físico com magia arcana.",
        "pode_evoluir": ["Arqueiro Arcano", "Guerreiro Psíquico", "Campeão"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Força": 2, "Inteligência": 1}
    },
    "Guerreiro Psíquico": {
        "desc": "Um guerreiro que usa poderes psíquicos para aumentar suas capacidades em combate.",
        "pode_evoluir": ["Campeão", "Mestre de Batalha", "Cavaleiro Eldritch"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Força": 2, "Sabedoria": 1}
    },
    "Arqueiro Arcano": {
        "desc": "Um guerreiro especializado no uso de arcos e flechas mágicas.",
        "pode_evoluir": ["Cavaleiro Eldritch", "Mestre de Batalha"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Destreza": 2, "Inteligência": 1}
    },
    "Cavaleiro": {
        "desc": "Um guerreiro montado que se destaca na proteção de aliados e controle do campo de batalha.",
        "pode_evoluir": ["Samurai", "Cavaleiro Eldritch", "Guerreiro Psíquico"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Força": 2, "Constituição": 1}
    },
    "Samurai": {
        "desc": "Um guerreiro disciplinado que se especializa em combates ferozes e resistir ao dano.",
        "pode_evoluir": ["Cavaleiro", "Campeão", "Mestre de Batalha"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Força": 2, "Carisma": 1}
    },
    "Banneret": {
        "desc": "Um guerreiro líder, inspirando e protegendo seus aliados em combate.",
        "pode_evoluir": ["Cavaleiro", "Guerreiro Psíquico", "Cavaleiro Eldritch"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Força": 2, "Carisma": 1}
    },
    "Rune Knight": {
        "desc": "Um guerreiro que canaliza o poder das runas para aumentar suas habilidades.",
        "pode_evoluir": ["Cavaleiro", "Mestre de Batalha", "Guerreiro Psíquico"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Força": 2, "Inteligência": 1}
    },
    "Echo Knight": {
        "desc": "Um guerreiro que manipula ecos temporais para realizar ataques adicionais e distorcer o espaço.",
        "pode_evoluir": ["Mestre de Batalha", "Guerreiro Psíquico", "Cavaleiro Eldritch"],
        "classe_inicial": "Guerreiro",
        "bonus": {"Força": 2, "Destreza": 1}
    },

    "Paladino": {
        "desc": "Um cavaleiro sagrado, mestre da espada e da cura divina.",
        "pode_evoluir": [],
        "classe_inicial": "Cavaleiro",
        "bonus": {"Força": 1, "Sabedoria": 2, "Carisma": 1}
    },

    "Mago": {
        "desc": "Especialista em magias arcanas. Frágil, mas poderoso à distância.",
        "pode_evoluir": ["Arquimago", "Feiticeiro"],
        "classe_inicial": "Mago",
        "bonus": {"Inteligência": 3}
    },

    "Arquimago": {
        "desc": "Um mestre absoluto da magia. Conhecimento e destruição.",
        "pode_evoluir": [],
        "classe_inicial": "Mago",
        "bonus": {"Inteligência": 4, "Constituição": -1}
    },

    "Feiticeiro": {
        "desc": "Canaliza magia bruta vinda do sangue ou pacto.",
        "pode_evoluir": [],
        "classe_inicial": "Mago",
        "bonus": {"Carisma": 2, "Inteligência": 1}
    },

    "Arqueiro": {
        "desc": "Perito em ataques à distância. Rápido e preciso.",
        "pode_evoluir": ["Atirador Sombrio", "Rastreador"],
        "classe_inicial": "Arqueiro",
        "bonus": {"Destreza": 3}
    },

    "Atirador Sombrio": {
        "desc": "Um arqueiro que domina o silêncio e a escuridão.",
        "pode_evoluir": [],
        "classe_inicial": "Arqueiro",
        "bonus": {"Destreza": 2, "Sabedoria": 1}
    },

    "Rastreador": {
        "desc": "Caçador nato, conectado à natureza e ao faro de combate.",
        "pode_evoluir": [],
        "classe_inicial": "Arqueiro",
        "bonus": {"Destreza": 1, "Sabedoria": 2}
    }
}
