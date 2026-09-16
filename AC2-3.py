#calcular_horas_extras(valor_hora, horas_realizadas)
#Recebe o valor da hora normal e a quantidade de horas extras executadas.
#Retorna o valor total a ser pago pelas horas extras (considerando um acréscimo/adicional de 50% sobre o valor da hora).
#calcular_desconto_falta(salario_base, dias_falta)
#Recebe o salário base mensal e a quantidade de faltas não justificadas.
#Retorna o valor total a ser descontado do salário (considerando o mês comercial de 30dias).
#calcular_salario_liquido(salario_base, bonus, descontos)
#Recebe o salário base, valor de bônus e total de descontos, retornando o salário líquidofinal do funcionário.
#classificar_desempenho(pontuacao)
#Recebe uma pontuação de avaliação de desempenho (0 a 100) e retorna o nível de
#classificação do colaborador:
#- Abaixo de 50 pontos -> Insuficiente
#- 50 a 69 pontos -> Regular
#- 70 a 89 pontos -> Bom
#- 90 ou mais pontos -> Excelente
#calcular_score_gerencial(experiencia_anos, projetos_entregues, pontuacao_desempenho)
#Recebe o tempo de casa (em anos), número de projetos finalizados e a nota de
#desempenho.
#Retorna o score gerencial calculado pela fórmula:
#score = (experiência * 2) + projetos + pontuação

def calcular_horas_extras(valor_hora, horas_realizadas):
    return valor_hora * horas_realizadas * 1.5

def calcular_desconto_falta(salario_base, dias_falta):
    valor_dia = salario_base / 30
    return valor_dia * dias_falta

def calcular_salario_liquido(salario_base, bonus, descontos):
    return salario_base + bonus - descontos

def classificar_desempenho(pontuacao):
    if pontuacao >= 90:
        return "Excelente"
    elif pontuacao >= 70:
        return "Bom"
    elif pontuacao >= 50:
        return "Regular"
    else:
        return "Insuficiente"

def calcular_score_gerencial(experiencia_anos, projetos_entregues, pontuacao_desempenho):
    score = (experiencia_anos * 2) + projetos_entregues + pontuacao_desempenho
    return score


while True:
    print("\n=== PAINEL DE GESTÃO DE RECURSOS HUMANOS ===")
    print("1. Calcular Score Gerencial do Colaborador")
    print("2. Simular Salário Líquido (Horas Extras / Descontos)")
    print("3. Avaliar Nível de Desempenho")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exp = int(input("Anos de experiência: "))
        proj = int(input("Quantidade de projetos entregues: "))
        nota = float(input("Pontuação de desempenho: "))

        score_final = calcular_score_gerencial(exp, proj, nota)
        print(f"\n> Score Gerencial do Colaborador: {score_final:.2f}")

    elif opcao == "2":
        salario = float(input("Salário base (R$): "))
        v_hora = float(input("Valor da hora normal (R$): "))
        h_extras = float(input("Quantidade de horas extras feitas: "))
        faltas = int(input("Quantidade de faltas não justificadas: "))

        total_extras = calcular_horas_extras(v_hora, h_extras)
        total_descontos = calcular_desconto_falta(salario, faltas)
        salario_final = calcular_salario_liquido(
            salario,
            total_extras,
            total_descontos
        )

        print("\n--- Resumo Salarial ---")
        print(f"(+) Horas Extras: R$ {total_extras:.2f}")
        print(f"(-) Desconto Faltas: R$ {total_descontos:.2f}")
        print(f"(=) Salário Líquido: R$ {salario_final:.2f}")

    elif opcao == "3":
        nota = float(input("Digite a pontuação de desempenho (0 a 100): "))
        classificacao = classificar_desempenho(nota)

        print(f"\n> Classificação do Colaborador: {classificacao}")

    elif opcao == "4":
        print("\nEncerrando o sistema. Até logo!")
        break

    else:
        print("\n[Erro] Opção inválida! Escolha um número de 1 a 4.")