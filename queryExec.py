import sys
import psycopg2
import messageModule as msg
import databaseConnection as dbCon

WRITE_TO_FILE = False

def writeResultToFile(query_result):
    result_file = open("first_query_result.txt", "w", encoding='UTF-8')
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
        writeResultToFile(query_result)
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
    
if __name__ == "__main__":
    main()