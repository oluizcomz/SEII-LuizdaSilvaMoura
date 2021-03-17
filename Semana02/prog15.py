#work csv
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    #abrindo o csv para leitura

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']
        #abrindo o csv para escrita

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        #mudando o demarcador de dados para tablaçao(\t)
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
            #copiando linha por linha