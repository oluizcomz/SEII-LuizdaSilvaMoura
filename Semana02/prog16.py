import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    #abrindo os dados no arquivo patrons.csv para leitura como dicionario 
    # onde tem uma chave para cada dado correspondente ao cabeçalho
    csv_data = csv.DictReader(data_file)
    #pulando as linhas que nao deseja ler
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        #para de ler novas linhas assim q le uma nao correspondente
        names.append(f"{line['FirstName']} {line['LastName']}")
        #addcionando no final do vetor o primeiro e o ultimo nome

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)