import os
import pandas as pd
import yaml

# Caminho para a pasta que contém os dados de corrida (múltiplos anos)
base_dir = './data'

# Defina o intervalo de anos de interesse
anos = range(1970, 2025)

# Nome do piloto a ser filtrado
piloto_especifico = 'elio-de-angelis'

# Lista para armazenar os dados de cada corrida
resultados_corridas = []

# Função para carregar o arquivo YAML
def carregar_resultados(arquivo):
    with open(arquivo, 'r') as f:
        return yaml.safe_load(f)

# Iterando pelos anos e corridas dentro do intervalo especificado
for ano in anos:
    ano_dir = os.path.join(base_dir, str(ano))
    
    # Verificando se a pasta do ano existe
    if os.path.exists(ano_dir):
        for root, dirs, files in os.walk(ano_dir):
            for file in files:
                if file.endswith('qualifying-results.yml'):
                    caminho_arquivo = os.path.join(root, file)
                    resultados = carregar_resultados(caminho_arquivo)
                    
                    # Nome da corrida (nome da pasta contendo 'race-results.yml')
                    nome_corrida = os.path.basename(root)
                    
                    # Assumindo que o arquivo contém uma lista de resultados de pilotos
                    for resultado in resultados:
                        if resultado['driverId'] == piloto_especifico:
                            # Adiciona o ano e o nome da corrida ao resultado
                            resultado['year'] = ano
                            resultado['race'] = nome_corrida[3:]
                            resultados_corridas.append(resultado)

# Convertendo os resultados em um DataFrame
df_resultados = pd.DataFrame(resultados_corridas)

df_resultados.to_csv(f'data-csv/qualifying-results_{piloto_especifico}.csv', index=False)