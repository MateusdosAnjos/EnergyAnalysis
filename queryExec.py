import sys
import psycopg2
import messageModule as msg
import databaseConnection as dbCon

WRITE_TO_FILE = False

def writeResultToFile(query_result, file_name: str):
    result_file = open(file_name, "w", encoding='UTF-8')
    for result_line in query_result:
        for element in result_line:
            result_file.write(str(element))
            result_file.write(", ")
        result_file.write("\n")
    result_file.close()

def firstQuery(DATABASE_CONNECTION):
    global WRITE_TO_FILE
    cur = DATABASE_CONNECTION.cursor()
    cur.execute('''
        SELECT previsao, sum(potencia_ug) as soma_de_potencia_ug, submercado, uf, situacao_das_obras
        FROM ralie, cad_estado_submercado
        WHERE ((situacao_das_obras != 'Atrasada') and (ralie.uf = cad_estado_submercado.sigla))
        GROUP BY combustivel, previsao, submercado, uf, situacao_das_obras
        ORDER BY(submercado, previsao);''')
    if WRITE_TO_FILE:
        query_result = cur.fetchall()
        writeResultToFile(query_result, "first_query_result.txt")
    else:
        print(cur.fetchall())

def secondQuery(DATABASE_CONNECTION):
    global WRITE_TO_FILE
    cur = DATABASE_CONNECTION.cursor()
    cur.execute('''
        SELECT  round(avg((previsao_operacao - inicio_das_obras)/30), 2), tipo_geracao, situacao_das_obras FROM ralie
        WHERE 
        (combustivel = 'Eólica' or combustivel = 'Solar')
        and
        (inicio_das_obras is not null)
        and
        (previsao_operacao <= '2021-09-30' and previsao_operacao >= '2020-10-01')
        GROUP BY tipo_geracao, situacao_das_obras;''')
    if WRITE_TO_FILE:
        query_result = cur.fetchall()
        writeResultToFile(query_result, "second_query_result.txt")
    else:
        print(cur.fetchall())

def main():
    global WRITE_TO_FILE
    if len(sys.argv) > 1 and sys.argv[1] == 'file':
        WRITE_TO_FILE = True
    DATABASE_CONNECTION = dbCon.connectToDatabase()
    if DATABASE_CONNECTION == None:
        return
    firstQuery(DATABASE_CONNECTION)
    secondQuery(DATABASE_CONNECTION)
    
if __name__ == "__main__":
    main()