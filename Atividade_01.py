import csv

with open('A260930.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=";")
    for linha in leitor_csv:
        print(linha)