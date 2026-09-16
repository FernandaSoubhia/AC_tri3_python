#Aplicar os conceitos de Funções em Python (def, parâmetros e return) para construir uma
#ferramenta de gestão interativa para RH/Departamento Pessoal em terminal.
#O objetivo é modularizar os cálculos trabalhistas e de avaliação de desempenho da
#empresa em funções reutilizáveis, integrando tudo em um menu contínuo de navegação.

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
    elif pontuacao <= 69:
        return "Regular"
    elif pontuacao <= 89:
        return "Bom"
    else:
        return "Excelente"
 
def calcular_score_gerencial(experiencia_anos, projetos_entregues, pontuacao_desempenho):
    score = (experiencia_anos * 2) + projetos_entregues + pontuacao_desempenho
    return score
























