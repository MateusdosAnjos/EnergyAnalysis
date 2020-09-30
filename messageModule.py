# MESSAGE MODULE MESSAGES #

#USED FOR COLORES PRINTS
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

################################################################################
#                             ERROR MESSAGES                                   #
################################################################################
def errorMsgCreateTable(name_table):
    print(f"{bcolors.WARNING}ALGO DEU ERRADO NA CRIAÇÃO DA TABELA:{bcolors.ENDC}", name_table)
    print("verifique seu banco de dados, se a tabela já existia provavelmente o erro estará relacionado a isso! Em muitos casos não será problema.")
    print()
    return

def msgDatabaseFailedToConnect():
    print(f"{bcolors.FAIL}FALHA NA CONEXÃO COM O BANCO DE DADOS!{bcolors.ENDC}")
    print()
    return

def noGenerator(table_name):
    print(f"{bcolors.FAIL}GERADOR DE INSERTS PARA A TABELA: " + table_name + " NÃO EXISTE!{bcolors.ENDC}")
    print()

def tableNotPopulated(table_name):
    print(f"{bcolors.WARNING}TABELA: {table_name} NÃO FOI POPULADA!{bcolors.ENDC}")
    print("verifique seu banco de dados, se a tabela já existia provavelmente o erro estará relacionado a isso!")
    print()
    return

################################################################################
#                            SUCCESS MESSAGES                                  #
################################################################################
def databaseConnected():
    print(f"{bcolors.OKGREEN}BANCO DE DADOS CONECTADO!{bcolors.ENDC}")
    print()
    return

def tableCreated(table_name):
    print(f"{bcolors.OKGREEN}TABELA DE NOME: {table_name} CRIADA COM SUCESSO!{bcolors.ENDC}")
    print()
    return

def tablePopulated(table_name):
    print(f"{bcolors.OKGREEN}TABELA DE NOME: {table_name} POPULADA COM SUCESSO!{bcolors.ENDC}")
    print()
    return

################################################################################
#               databaseCreator PROGRAM FLOW MESSAGES                          #
################################################################################
def callCheck():
    print(f"{bcolors.OKGREEN}PROGRAMA EXECUTADO CORRETAMENTE.{bcolors.ENDC}")
    print()
    return

def connectAndCreate():
    print(f"{bcolors.OKGREEN}PROGRAMA TENTANDO SE CONECTAR AO BANCO E CRIAR OS MODELOS INICIAIS DE TABELA.{bcolors.ENDC}")
    print()
    return

def readingFile():
    print(f"{bcolors.OKGREEN}PROGRAMA ESTÁ LENDO O ARQUIVO PASSADO.{bcolors.ENDC}")
    print()
    return 

def processingFile():
    print(f"{bcolors.OKGREEN}PROGRAMA ESTÁ PROCESSANDO O ARQUIVO PASSADO.{bcolors.ENDC}")
    print()
    return 

def databaseInserts():
    print(f"{bcolors.OKGREEN}PROGRAMA ESTÁ INSERINDO OS DADOS NO BANCO.{bcolors.ENDC}")
    print()
    return 

def creatingViaQuery():
    print(f"{bcolors.OKGREEN}PROGRAMA ESTÁ CRIANDO TABELAS UTILIZANDO CONSULTAS AO BANCO.{bcolors.ENDC}")
    print()
    return 

def finishExecution():
    print(f"{bcolors.OKGREEN}PROGRAMA TERMINOU SEM ERROS!{bcolors.ENDC}")
    print()
    return 

################################################################################
#                   manager PROGRAM FLOW MESSAGES                              #
################################################################################
def initDataColector():
    print(f"{bcolors.OKGREEN}INICIANDO COLETA DE DADOS!{bcolors.ENDC}")
    print()
    return 

def initDatabaseCreator():
    print(f"{bcolors.OKGREEN}INICIANDO CRIAÇÃO DO BANCO DE DADOS!{bcolors.ENDC}")
    print()
    return 
