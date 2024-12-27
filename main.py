import xlsxwriter

def adicionar_funcionario(nome, telefone, datanascimento, endereco, cep, ncasa, genero):
    # Cria o arquivo Excel
    workbook = xlsxwriter.Workbook('cadastro_funcionarios.xlsx')
    worksheet = workbook.add_worksheet()

    # Cabeçalhos
    headers = ['Nome', 'Telefone', 'Data de nascimento', 'Endereço', 'CEP', 'Número da casa', 'Gênero']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Adiciona os dados do novo funcionário
    row = worksheet.dim_rowmax + 1  # Obtém a próxima linha disponível
    worksheet.write(row, 0, nome)
    worksheet.write(row, 1, telefone)
    worksheet.write(row, 2, datanascimento)
    worksheet.write(row, 3, endereco)
    worksheet.write(row, 4, cep)
    worksheet.write(row, 5, ncasa)
    worksheet.write(row, 6, genero)

    # Salva e fecha o arquivo
    workbook.close()

# Exemplo de uso
nome_funcionario = 'João Pedro'
telefone_funcionario = '22 98121-5654'
nascimento_funcionario = '22/05/2004'
endereco_funcionario = 'Rua Alfredo Backer'
cep_funcionario = '27910-190'
ncasa_funcionario = '405'
genero_funcionario = 'Masculino'

adicionar_funcionario(nome_funcionario, telefone_funcionario, nascimento_funcionario, endereco_funcionario, cep_funcionario, ncasa_funcionario, genero_funcionario)
