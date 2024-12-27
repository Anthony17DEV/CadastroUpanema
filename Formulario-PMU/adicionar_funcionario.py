import xlsxwriter

def adicionar_funcionario(nome, celular, data, endereco, cep, numero, genero):
    # Cria o arquivo Excel
    workbook = xlsxwriter.Workbook('cadastro_funcionarios.xlsx')
    worksheet = workbook.add_worksheet()

    # Cabeçalhos
    headers = ['Nome', 'Celular', 'Data de nascimento', 'Endereço', 'CEP', 'Número da casa', 'Gênero']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Adiciona os dados do novo funcionário
    row = worksheet.dim_rowmax + 1  # Obtém a próxima linha disponível
    worksheet.write(row, 0, nome)
    worksheet.write(row, 1, celular)
    worksheet.write(row, 2, data)
    worksheet.write(row, 3, endereco)
    worksheet.write(row, 4, cep)
    worksheet.write(row, 5, numero)
    worksheet.write(row, 6, genero)

    # Salva e fecha o arquivo
    workbook.close()
