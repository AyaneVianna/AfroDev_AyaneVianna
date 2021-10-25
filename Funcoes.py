import pandas as pd
import matplotlib.pyplot as plt
# leitura dos dados dos arquivos
df_atletas = pd.read_excel("C:\Desenvolvedora\AfroDev_AyaneVianna\Arquivos Excel\Athletes.xlsx")
df_treinadores = pd.read_excel("C:\Desenvolvedora\AfroDev_AyaneVianna\Arquivos Excel\Coaches.xlsx")
df_genero = pd.read_excel("C:\Desenvolvedora\AfroDev_AyaneVianna\Arquivos Excel\EntriesGender.xlsx")
df_medalhas = pd.read_excel("C:\Desenvolvedora\AfroDev_AyaneVianna\Arquivos Excel\Medals.xlsx")
df_times = pd.read_excel("C:\Desenvolvedora\AfroDev_AyaneVianna\Arquivos Excel\Teams.xlsx")
#Funções estéticas
def divisao_texto():
    print('\n')
    print('*'*135)
    print('\n')

#Funções das perguntas
def total_atletas():
    num_atletas = len(df_atletas.index)
    print(f'O número total de atletas participantes das Olimpíadas de Tóquio é {num_atletas}')
def total_homens():
    atletas_homens = sum(df_genero['Male'])
    print(f'Foram {atletas_homens} atletas homens que participaram das Olimpíadas de Tóquio.')   
def total_mulheres():
    atletas_mulheres = sum(df_genero['Female'])
    print(f'Foram {atletas_mulheres} atletas mulheres que participaram das Olimpíadas de Tóquio.')
def total_atletas_esportes():
    df_genero2 = df_genero
    df_genero2['Total Athletes'] = df_genero2.sum(axis=1)
    atletas_por_esporte = df_genero2[['Discipline', 'Total Athletes']]
    print(f'O total de atletas por esporte: \n {atletas_por_esporte} ')
def total_medalhas():
    df_medalhas_total = df_medalhas
    df_medalhas_total['Total Medals'] = df_medalhas_total.sum(axis=1)
    medalhas_por_pais = df_medalhas_total[['Team/NOC', 'Total Medals']]
    print(f'O total de medalhas por país: \n {medalhas_por_pais} ')
def ranking_medalhas():
    df_medalhas_total = df_medalhas
    df_medalhas_total['Total Medals'] = df_medalhas_total.sum(axis=1)
    medalhas_por_pais = df_medalhas_total[['Team/NOC', 'Total Medals']]
    ranking_total_medalhas = medalhas_por_pais.sort_values(by=['Total Medals'], ascending=False)
    print(f'O ranking por total de medalhas é: \n {ranking_total_medalhas}')
def mais_medalha_ouro():
    num_maior_ouro = df_medalhas['Gold'].max()
    pais_mais_medalha_ouro = df_medalhas['Team/NOC'][df_medalhas['Gold'].idxmax()]
    print(f'O país com mais medalhas de ouro é {pais_mais_medalha_ouro}, tendo {num_maior_ouro} medalhas. ')
def mais_medalha_prata():
    num_maior_prata = df_medalhas['Silver'].max()
    pais_mais_medalha_prata = df_medalhas['Team/NOC'][df_medalhas['Silver'].idxmax()]
    print(f'O país com mais medalhas de prata é {pais_mais_medalha_prata}, tendo {num_maior_prata} medalhas. ')
def mais_medalha_bronze():
    num_maior_bronze = df_medalhas['Bronze'].max()
    pais_mais_medalha_bronze = df_medalhas['Team/NOC'][df_medalhas['Bronze'].idxmax()]
    print(f'O país com mais medalhas de bronze é {pais_mais_medalha_bronze}, tendo {num_maior_bronze} medalhas. ')
def menos_medalha_ouro():
    num_menor_ouro = df_medalhas['Gold'].min()
    pais_menos_medalha_ouro = df_medalhas['Team/NOC'][df_medalhas['Gold'].idxmin()]
    print(f'O país com menos medalhas de ouro é {pais_menos_medalha_ouro}, tendo {num_menor_ouro} medalhas. ')
def menos_medalha_prata():
    num_menor_prata = df_medalhas['Silver'].min()
    pais_menos_medalha_prata = df_medalhas['Team/NOC'][df_medalhas['Silver'].idxmin()]
    print(f'O país com menos medalhas de prata é {pais_menos_medalha_prata}, tendo {num_menor_prata} medalhas. ')
def menos_medalha_bronze():
    num_menor_bronze = df_medalhas['Bronze'].min()
    pais_menos_medalha_bronze = df_medalhas['Team/NOC'][df_medalhas['Bronze'].idxmin()]
    print(f'O país com menos medalhas de bronze é {pais_menos_medalha_bronze}, tendo {num_menor_bronze} medalhas. ')
def lista_esportes():
    esportes = df_genero['Discipline']
    print(f'Esportes participantes: \n{esportes} ')
def lista_esportes_mais_homens():
    esportes_mais_homens = df_genero[df_genero['Male'] > df_genero['Female']]
    print(f'Os esportes com mais homens do que mulheres participando são: \n {esportes_mais_homens} ')
def lista_esportes_mais_mulheres():
    esportes_mais_mulheres = df_genero[df_genero['Female'] > df_genero['Male']]
    print(f'Os esportes com mais mulheres do que homens participando são: \n {esportes_mais_mulheres} ')
def quantidade_treinadores_pais():
    treinadores_paises = df_treinadores['NOC'].value_counts()
    print(f'A quantidade de treinadores por país é: \n{treinadores_paises} ')
def mais_treinadores():
    df_treinadores_paises = df_treinadores['NOC'].value_counts() 
    pais_mais_treinadores =  df_treinadores_paises.idxmax()
    num_treinadores = df_treinadores_paises.max()
    print(f'O país com mais treinadores é {pais_mais_treinadores}, tendo {num_treinadores} treinadores.')
def quantidade_treinadores_esporte():
    treinadores_esporte = df_treinadores['Discipline'].value_counts()
    print(f'A quantidade de treinadores por esporte é: \n {treinadores_esporte}')
def quantidade_times_esporte_pais():
    times_esporte_pais = df_times.groupby(['NOC','Discipline']).size()
    print(f'A quantidade de times por esporte de cada país é: \n {times_esporte_pais}')
def porcentagem_generos():
    atletas_homens = sum(df_genero['Male'])
    atletas_mulheres = sum(df_genero['Female'])
    total_atletas = atletas_homens + atletas_mulheres
    porcentagem_mulheres = float((atletas_mulheres*100)/total_atletas)
    porcentagem_homens = float((atletas_homens*100)/total_atletas)
    print(f'A porcentagem de atletas mulheres participantes é {porcentagem_mulheres:.1f}%. E de homens é de {porcentagem_homens:.1f}%.')
def pais_mais_times():
    times_paises = df_times['Name'].value_counts()
    pais_max_times = times_paises.idxmax()
    num_times = times_paises.max()
    print(f'O país com mais times é {pais_max_times}, tendo {num_times} times nas olimpíadas. ')
def pais_menos_times():
    times_paises = df_times['Name'].value_counts()
    pais_min_times = times_paises.idxmin()
    num_times = times_paises.min()
    print(f'O país com menos times é {pais_min_times}, tendo {num_times} time(s) nas olimpíadas. ')
def esporte_mais_times():
    times_esporte = df_times['Discipline'].value_counts()
    esporte_max_times = times_esporte.idxmax()
    num_times = times_esporte.max()
    print(f'O esporte com mais times é {esporte_max_times}, tendo {num_times} times nas olimpíadas. ')
def esporte_menos_times():
    times_esporte = df_times['Discipline'].value_counts()
    esporte_min_times = times_esporte.idxmin()
    num_times = times_esporte.min()
    print(f'O esporte com menos times é {esporte_min_times}, tendo {num_times} time(s) nas olimpíadas. ')

#Funções de conclusão e retorno
def conclusao_retorno():
    print(f'Gostaria de ver mais informações sobre as Olimpíadas? \nSe sim, digite 1. Se não, digite 2.')
    digito = int(input())
    if (digito == 1):
        return indice_inicial()
    elif (digito == 2):
        divisao_texto()
        print(f'Espero que tenha gostado da experiência, nos vemos em uma próxima!')
        divisao_texto()
    else:
        print(f'Ops! Tem algo errado, por favor, digite novamente')
        return conclusao_retorno()
def retorno_indice():
    return indice_inicial()
#Funções dos tópicos
def atletas():
    print(f'DADOS SOBRE OS ATLETAS \n\nQue informação gostaria de saber?')
    print(f'1-Total de atletas participantes. \n2- Total de participantes homens. \n3- Total de participantes mulheres. \n4-Total de participantes por esporte. \n5-Porcentagem de atletas mulheres e homens participantes. \n0-Voltar para o índice inicial.')
    pergunta = int(input(f'\nInformação número '))
    if (pergunta == 1):
        divisao_texto()
        total_atletas()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 2):
        divisao_texto()
        total_homens()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 3):
        divisao_texto()
        total_mulheres()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 4):
        divisao_texto()
        total_atletas_esportes()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 5):
        divisao_texto()
        porcentagem_generos()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 0):
        divisao_texto()
        retorno_indice()
    else:
        divisao_texto()
        print(f'Ops, tem algo errado. Por favor, digite novamente.')
        divisao_texto()
        return atletas() 
def treinadores():
    print(f'DADOS SOBRE OS TREINADORES \n\nQue informação gostaria de saber?')
    print(f'1-Quantidade de treinadores por país. \n2-País com a maior quantidade de treinadores. \n3-Quantidade de treinadores por esporte. \n0-Voltar para o índice inicial.')
    pergunta = int(input(f'\nInformação número '))
    if (pergunta == 1):
        divisao_texto()
        quantidade_treinadores_pais()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 2):
        divisao_texto()
        mais_treinadores()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 3):
        divisao_texto()
        quantidade_treinadores_esporte()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 0):
        divisao_texto()
        retorno_indice()
    else:
        divisao_texto()
        print(f'Ops, tem algo errado. Por favor, digite novamente.')
        divisao_texto()
        return treinadores()
def esportes():
    print(f'DADOS SOBRE OS ESPORTES \n\nQue informação gostaria de saber?')
    print(f'1-Total de participantes por esporte. \n2-Lista com esportes participantes. \n3-Lista de esportes com mais homens que mulheres. \n4-Lista de esportes com mais mulheres que homens.  \n5-Quantidade de treinadores por esporte.  \n6-Quantidade de times por esporte de cada país. \n7-Esporte com mais times participantes. \n8-Esporte com menos times partipantes. \n0-Voltar para o índice inicial.')
    pergunta = int(input(f'\nInformação número '))
    if (pergunta == 1):
        divisao_texto()
        total_atletas_esportes()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 2):
        divisao_texto()
        lista_esportes()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 3):
        divisao_texto()
        lista_esportes_mais_homens()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 4):
        divisao_texto()
        lista_esportes_mais_mulheres()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 5):
        divisao_texto()
        quantidade_treinadores_esporte()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 6):
        divisao_texto()
        quantidade_times_esporte_pais()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 7):
        divisao_texto()
        esporte_mais_times()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 8):
        divisao_texto()
        esporte_menos_times()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 0):
        divisao_texto()
        retorno_indice()
    else:
        divisao_texto()
        print(f'Ops, tem algo errado. Por favor, digite novamente.')
        divisao_texto()
        return esportes()  
def paises():
    print(f'DADOS SOBRE OS PAISES \n\nQue informação gostaria de saber?')
    print(f'1-Total de medalhas por país. \n2-País com mais medalhas de ouro. \n3-País com mais medalhas de prata. \n4-País com mais medalhas de bronze.  \n5-País com menos medalhas de ouro.  \n6-País com menos medalhas de prata. \n7-País com menos medalhas de bronze.  \n8-Quantidade de treinadores por país. \n9-País com a maior quantidade de treinadores  \n10-Quantidade de times por esporte de cada país. \n11-País com mais times participantes. \n12-País com menos times participantes. \n0-Voltar para o índice inicial.')
    pergunta = int(input(f'\nInformação número '))
    if (pergunta == 1):
        divisao_texto()
        total_medalhas()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 2):
        divisao_texto()
        mais_medalha_ouro()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 3):
        divisao_texto()
        mais_medalha_prata()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 4):
        divisao_texto()
        mais_medalha_bronze()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 5):
        divisao_texto()
        menos_medalha_ouro()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 6):
        divisao_texto()
        menos_medalha_prata()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 7):
        divisao_texto()
        menos_medalha_bronze()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 8):
        divisao_texto()
        quantidade_treinadores_pais()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 9):
        divisao_texto()
        mais_treinadores()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 10):
        divisao_texto()
        quantidade_times_esporte_pais()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 11):
        divisao_texto()
        pais_mais_times()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 12):
        divisao_texto()
        pais_menos_times()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 0):
        divisao_texto()
        retorno_indice()
    else:
        divisao_texto()
        print(f'Ops, tem algo errado. Por favor, digite novamente.')
        divisao_texto()
        return paises()
def times():
    print(f'DADOS SOBRE OS TIMES \n\nQue informação gostaria de saber?')
    print(f'1-Quantidade de times por esporte de cada país. \n2-País com mais times participantes. \n3-País com menos times participantes. \n4-Esporte com mais times participantes. \n5-Esporte com menos times participantes. \n0-Voltar para o índice inicial.')
    pergunta = int(input(f'\nInformação número '))
    if (pergunta == 1):
        divisao_texto()
        quantidade_times_esporte_pais()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 2):
        divisao_texto()
        pais_mais_times()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 3):
        divisao_texto()
        pais_menos_times()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 4):
        divisao_texto()
        esporte_mais_times()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 5):
        divisao_texto()
        esporte_menos_times()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 0):
        divisao_texto()
        retorno_indice()
    else:
        divisao_texto()
        print(f'Ops, tem algo errado. Por favor, digite novamente.')
        divisao_texto()
        return times()
def medalhas():
    print(f'DADOS SOBRE AS MEDALHAS \n\nQue informação gostaria de saber?')
    print(f'1-Total de medalhas por país. \n2-País com mais medalhas de ouro. \n3-País com mais medalhas de prata. \n4-País com mais medalhas de bronze.  \n5-País com menos medalhas de ouro.  \n6-País com menos medalhas de prata. \n7-País com menos medalhas de bronze.  \n8-Ranking por medalhas totais. \n0-Voltar para o índice inicial.')
    pergunta = int(input(f'\nInformação número '))
    if (pergunta == 1):
        divisao_texto()
        total_medalhas()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 2):
        divisao_texto()
        mais_medalha_ouro()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 3):
        divisao_texto()
        mais_medalha_prata()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 4):
        divisao_texto()
        mais_medalha_bronze()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 5):
        divisao_texto()
        menos_medalha_ouro()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 6):
        divisao_texto()
        menos_medalha_prata()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 7):
        divisao_texto()
        menos_medalha_bronze()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 8):
        divisao_texto()
        ranking_medalhas()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 0):
        divisao_texto()
        retorno_indice()
    else:
        divisao_texto()
        print(f'Ops, tem algo errado. Por favor, digite novamente.')
        divisao_texto()
        return medalhas()
def genero():
    print(f'DADOS SOBRE O GÊNERO DOS ATLETAS \n\nQue informação gostaria de saber?')
    print(f'1-Total de participantes homens. \n2- Total de participantes mulheres. \n3-Lista de esportes com mais homens que mulheres. \n4-Lista de esportes com mais mulheres que homens. \n5-Porcentagem de atletas mulheres e homens participantes. \n0-Voltar para o índice inicial.')
    pergunta = int(input(f'\nInformação número '))
    if (pergunta == 1):
        divisao_texto()
        total_homens()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 2):
        divisao_texto()
        total_mulheres()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 3):
        divisao_texto()
        lista_esportes_mais_homens()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 4):
        divisao_texto()
        lista_esportes_mais_mulheres()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 5):
        divisao_texto()
        porcentagem_generos()
        divisao_texto()
        conclusao_retorno()
    elif (pergunta == 0):
        divisao_texto()
        retorno_indice()
    else:
        divisao_texto()
        print(f'Ops, tem algo errado. Por favor, digite novamente.')
        divisao_texto()
        return genero() 
#Função do indice inicial
def indice_inicial():
    print(f'ÍNDICE \n\nEscolha o tópico que deseja saber sobre e indique o número referente a ele \n1-Atletas \n2-Treinadores \n3-Esportes \n4-Países \n5-Times \n6-Medalhas \n7-Gênero \n8-Sair')
    valor_indice_inicial = int(input('Tópico:'))
    if (valor_indice_inicial == 1):
        divisao_texto()
        atletas()
    elif (valor_indice_inicial == 2):
        divisao_texto()
        treinadores()
    elif(valor_indice_inicial == 3):
        divisao_texto()
        esportes()
    elif(valor_indice_inicial == 4):
        divisao_texto()
        paises()
    elif (valor_indice_inicial == 5):
        divisao_texto()
        times()
    elif (valor_indice_inicial == 6):
        divisao_texto()
        medalhas()
    elif (valor_indice_inicial == 7):
        divisao_texto()
        genero()
    elif (valor_indice_inicial == 8):
        divisao_texto()
        print(f'Espero que tenha gostado da experiência, nos vemos em uma próxima!')
        divisao_texto()
    else:
        divisao_texto()
        print(f'Ops, tem algo errado. Por favor, digite novamente.')
        divisao_texto()
        return indice_inicial() 


