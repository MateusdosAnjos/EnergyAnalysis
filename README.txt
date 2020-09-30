Para rodar o programa é necessário ter um banco de dados postgres
criado com as seguintes definições:

DB_HOST = "localhost"
DB_NAME = "COMERC Database"
DB_USER = "postgres"
DB_PASS = "MyDatabase"

Desta forma o programa conseguirá se conectar ao banco e criar as tabelas.
É necessário ter conexão com a internet e as bibliotecas:
os.path
requests
zipfile 
io
re
psycopg2
openpyxl

Algumas bibliotecas já vem com o python, outras devem ser instaladas utilizando:
pip install <nome_da_bilioteca>


Depois de criado o banco basta rodar:

.\manager.py <nome_do_arquivo_RAILE_baixado> file

desta forma o resultado das queries sairá em arquivos de texto

Se quiser exibir as queries no terminal use:

.\manager.py <nome_do_arquivo_RAILE_baixado>
