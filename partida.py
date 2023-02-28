import random
import json

# Carregar informações dos clubes no arquivo .JSON
with open('clubes.json', 'r', encoding='utf-8') as f:
    clubes = json.load(f)["clubes"]

# Buscar clubes no arquivo .JSON
corinthians = clubes[0]
flamengo = clubes[1]

# Tipos de gols
tipos_gols = ['gol de cabeça', 'golaço de falta', 'pênalti muito bem cobrado', 'chutaço de fora da área', 'chute colado dentro da área']

# Simular partida
def simular_partida(casa, fora):
  casa_gols = 0
  fora_gols = 0
  
  # Simular os 90 minutos da partida
  minuto = 0
  for minute in range(90):
    minuto += 1
    if random.random() < 0.05: # 5% de chance de gol
      if random.random() < 0.5: # 50% de chances de gol em casa
        casa_gols += 1
        gol_autor = random.choice(casa["jogadores"])
        gol_tipo = random.choice(tipos_gols)
        print(f'Gol do time da casa marcado por {gol_autor["nome_jogador"]} aos {minuto} minutos, com um {gol_tipo}.')

      else:
        fora_gols += 1
        gol_autor = random.choice(fora["jogadores"])
        gol_tipo = random.choice(tipos_gols)
        print(f'Gol do time visitante marcado por {gol_autor["nome_jogador"]} aos {minuto} minutos, com um {gol_tipo}.')
  
  print(f'{casa["nome_time"]} {casa_gols} x {fora_gols} {fora["nome_time"]}')

# Jogar partida
simular_partida(corinthians, flamengo)
