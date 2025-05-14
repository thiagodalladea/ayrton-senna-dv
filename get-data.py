import os
import pandas as pd
import yaml

# Caminho para a pasta que contém os dados de corrida (múltiplos anos)
base_dir = './data'

# Defina o intervalo de anos de interesse
anos = range(1970, 2025)

# Nome do piloto a ser filtrado
piloto_especifico = 'alain-prost'

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
                if file.endswith('race-results.yml'):
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

df_resultados.to_csv(f'data-csv/race-results/race-results_{piloto_especifico}.csv', index=False)





# # Função para carregar o arquivo YAML
# def carregar_resultados(arquivo):
#     with open(arquivo, 'r') as f:
#         return yaml.safe_load(f)

# # Função para converter o YAML para CSV
# def yaml_para_csv(caminho_yml, year, race):
#     # Diretório onde o CSV será salvo
#     pasta_csv = './data-csv/'
    
#     # Verifica se o diretório existe, se não, cria
#     if not os.path.exists(pasta_csv):
#         os.makedirs(pasta_csv)
    
#     # Carrega os resultados do arquivo YAML
#     resultados = carregar_resultados(caminho_yml)
    
#     # Converte a lista de resultados em um DataFrame
#     df_resultados = pd.DataFrame(resultados)
    
#     # Gera o nome do arquivo CSV a partir do nome do arquivo YAML (sem a extensão)
#     nome_arquivo = os.path.splitext(os.path.basename(caminho_yml))[0]
#     caminho_csv = os.path.join(pasta_csv, f'{ year }-{ race [3:]}.csv')
    
#     # Salva o DataFrame como um arquivo CSV
#     df_resultados.to_csv(caminho_csv, index=False)

# # Exemplo de uso:
# # Solicite o caminho do arquivo YML
# year = "1993"
# race = "03-europe"

# caminho_yml = f'./data/{ year }/races/{ race }/race-results.yml'

# # Chama a função para converter o YML em CSV
# yaml_para_csv(f'./data/{ year }/races/{ race }/race-results.yml', year, race)