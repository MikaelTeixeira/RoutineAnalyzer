import pandas as pd

def mostrar_porcentagem_de_tarefas(dataframe, dias_da_semana: list ):

    print(f"\nTOTAL DE ATIVIDADES NO DIA")

    total_atividades_semana = 0

    contagem_semanal = {}

    df = dataframe

    for dia in dias_da_semana:


        total_atividades = df[f"{dia}"].count()
        
        total_atividades_semana += total_atividades

        contagem = df[f"{dia}"].value_counts()

        print(f"\n{dia.upper()}")

        for atividade, numero_atividade in contagem.items():
            
            if atividade in contagem_semanal:
                contagem_semanal[atividade] += numero_atividade
            else:
                contagem_semanal[atividade] = numero_atividade

            percentual = (numero_atividade/total_atividades) * 100

            print(f"\n{atividade.title()} = {numero_atividade} horas ({percentual:.2f}%)")

    print(f"\n{"=" * 32}")
    print(f"RELATÓRIO SEMANAL DAS ATIVIDADES")
    print(f"{"=" * 32}")

    for nome_atividade, quantidade_atividade in contagem_semanal.items():

        percentual = (quantidade_atividade/total_atividades_semana) * 100

        print(f"\n'{nome_atividade.title()}' representa {percentual:.2f}% das atividades da semana.")

df_name = "RoutineAnalyzer Week days structure.csv"
df = pd.read_csv(df_name)

df.to_csv(df_name, index=False)

df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

''' 
df.map percorre cada célula de forma individual do meu dataframe, quando coloco .strip() ele remove os espaços em branco de cada célula.

Lambda é uma função anônima, em resumo: Você não precisa criar uma função específica para isso. É interessante usar o Lambda quando não vai reutilizar uma função,

é mais rápido e prático. Se eu precisasse limpar mais de um csv, seria melhor criar uma função dedicada.

Nesse exemplo ele vai retirar espaços duplos se a célula for uma string. Se não for, ele retorna a própria célula

OBS.: É melhor criar uma função dedicada se quiser fazer uma limpeza completa. Dá pra encaixar muitas validações pessoais numa função dedicada sem ficar confuso.
'''

dias_semana = ["SEGUNDA", "TERÇA", "QUARTA", "QUINTA", "SEXTA", "SÁBADO", "DOMINGO"]

mostrar_porcentagem_de_tarefas(df, dias_semana)