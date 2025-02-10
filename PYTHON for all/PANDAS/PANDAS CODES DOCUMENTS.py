import pandas as pd
# ??? Como add valor em cada célula com o data frame ????
try:
    df = pd.read_excel('TesteBrasilmadVBA.xlsx')
    '''PGAR LINHAS E COLUNAS'''
    df.iloc[:, 4]                # ''' : significa todas as linhas O 4 significa "quinta coluna" (começamos contando do 0) '''
    df.loc['linha por nome do índice']
    df[df.iloc[:, 4] == 'valor_filtro']       #  '''Guarda só as linhas que correspondem ao que queremos'''
    colunas = df.iloc[:, [0, 2]]  # Pega a primeira e a terceira coluna
    colunas = df.iloc[:, 1:3]  # Pega da segunda até a terceira coluna
    
    '''Ver_os_Dados''' 
    display(df)  #  usa no lugar do print para organizar o dataframe
    print(df)  # mostra o df  5 linhas iniciais e 5 linhas finais
    print(df.shape) # mostra DF com as linhas e colunas ao final do DF
    df.head()    # Ver as primeiras 5 linhas
    # Ver as últimas 5 linhas
    df.tail()
    # Ver informações sobre os dados
    df.info()
    ''' Filtragem:'''
    # Pegar linhas onde idade > 10
    df[df['idade'] > 10]
    # Pegar linhas onde nome é 'João'
    df[df['nome'] == 'João']
    '''Ordenação'''
    # Ordenar por idade
    df.sort_values('idade')
    # Ordenar por idade de forma decrescente
    df.sort_values('idade', ascending=False)

    '''Cálculos:'''
    # Média de uma coluna
    df['idade'].mean()
    # Soma de uma coluna
    df['valor'].sum()
    # Contar valores únicos
    df['cor'].value_counts()

    '''Agrupamento:'''
    # Agrupar por cor e calcular média de idade
    df.groupby('cor')['idade'].mean()
    '''Criando novas colunas:'''
    # Criar coluna de dobro da idade
    df['idade_dobro'] = df['idade'] * 2

    '''Limpeza de dados:'''
    # Remover linhas com valores faltantes
    df.dropna()
    # Preencher valores faltantes com 0
    df.fillna(0)


    '''Copiando Dados   _ excel v'''
    # Copiar só algumas colunas que você quer
    colunas_importantes = df[['nome', 'idade', 'cor']]
    # Copiar sem repetir valores
    valores_unicos = df['nome'].unique()

    '''Transformando Dados:'''
    # Trocar todos os valores de uma coluna
    df['idade'] = df['idade'].replace(10, 11)  # Troca todos 10 por 11
    # Aplicar uma mudança em toda coluna
    df['nome'] = df['nome'].str.upper()  # Deixa tudo maiúsculo

    '''Juntando Planilhas '''
    # Juntar lado a lado (merge)
    novo_df = pd.merge('df1', 'df2', on='nome')
    # Empilhar uma em cima da outra (concat)
    df_grandao = pd.concat(['df1', 'df2'])

    '''Trabalhando com Datas'''
    # Transformar texto em data
    df['data'] = pd.to_datetime(df['data'])
    # Pegar só o mês ou ano
    df['mes'] = df['data'].dt.month
    df['ano'] = df['data'].dt.year

    '''Salvando de Formas Diferentes:'''
    # Salvar em Excel bonitinho
    df.to_excel('arquivo_novo.xlsx', index=False)
    # Salvar em CSV
    df.to_csv('arquivo.csv', sep=';')








    ''' codes: inserir e substituir valores na planílha'''
    # 🔹 Inserir os novos dados diretamente no DataFrame
    linha_inicio = 16  # C17 no Excel (zero-indexado)
    colunas = list(range(2, 12))  # C até L (coluna 2 até 11 no zero-indexado)

    df_excel.iloc[linha_inicio:linha_inicio+len(df_novos_dados), colunas] = df_novos_dados.values

    # 🔹 Salvar de volta no Excel
    df_excel.to_excel(file_path, sheet_name=sheet_name, index=False, engine="openpyxl")

except:
    pass