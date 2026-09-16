#O programa deve rodar em um loop (while) oferecendo o menu interativo abaixo até que o
#usuário escolha encerrá-lo:
#=== PAINEL DE GESTÃO DE RECURSOS HUMANOS ===
#1. Calcular Score Gerencial do Colaborador
#2. Simular Salário Líquido (Horas Extras / Descontos)
#3. Avaliar Nível de Desempenho
#4. Sair

def calcular_horas_extras(valor_hora, horas_realizadas):
    return horas_realizadas * valor_hora * 1.5
 
 
def calcular_desconto_falta(salario_base, dias_falta):
    valor_dia = salario_base / 30
    return valor_dia * dias_falta
 
 
def calcular_salario_liquido(salario_base, bonus, descontos):
    return salario_base + bonus - descontos
 
 
def classificar_desempenho(pontuacao):
    if pontuacao < 50:
        return "Insuficiente"
    elif 50 <= pontuacao <= 69:
        return "Regular"
    elif 70 <= pontuacao <= 89:
        return "Bom"
    else:  
        return "Excelente"
 
 
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
        print("\n--- Cálculo de Score Gerencial ---")
        exp = int(input("Anos de experiência (tempo de casa): "))
        proj = int(input("Quantidade de projetos entregues: "))
        nota = float(input("Nota da avaliação de desempenho: "))
        score_final = calcular_score_gerencial(exp, proj, nota)
        print(f"\n> Score Gerencial do Colaborador: {score_final:.2f}")
    elif opcao == "2":
        print("\n--- Simulação de Salário Líquido ---")
        salario = float(input("Salário base mensal (R$): "))
        v_hora = float(input("Valor da hora normal (R$): "))
        h_extras = float(input("Quantidade de horas extras executadas: "))
        faltas = int(input("Quantidade de faltas não justificadas: "))
        total_extras = calcular_horas_extras(v_hora, h_extras)
        total_descontos = calcular_desconto_falta(salario, faltas)
        salario_final = calcular_salario_liquido(salario, total_extras, total_descontos)
        print(f"\n--- Resumo Trabalhista ---")
        print(f"  (+) Horas Extras Adicionadas: R$ {total_extras:.2f}")
        print(f"  (-) Desconto de Faltas:       R$ {total_descontos:.2f}")
        print(f"  (=) Salário Líquido Final:    R$ {salario_final:.2f}")
    elif opcao == "3":
        print("\n--- Avaliação de Desempenho ---")
        nota = float(input("Digite a pontuação do colaborador (0 a 100): "))
        classificacao = classificar_desempenho(nota)
        print(f"\n> Nível de Classificação: {classificacao}")
    elif opcao == "4":
        print("\nEncerrando o Sistema de Gestão. Até mais!")
        break
    else:
        print("\n[Erro] Opção inválida! Por favor, escolha um número de 1 a 4.")