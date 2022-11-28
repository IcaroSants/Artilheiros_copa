import psycopg2

class Connect(object):
    def __init__(self, host,database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
    
    def get_connection(self):
        conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conn.cursor()
        return conn, cursor
    
    def retorna_insercao(self,tabela,registros):
        for coluna, valor in registros.items():
            if type(valor) == str:
                registros[coluna]='\''+valor+'\''
        sql = "INSERT INTO "+tabela+"("+",".join(str(coluna) for coluna in registros.keys())+")"+" VALUES"+" ("+",".join(str(value) for value in registros.values())+")"
        return sql 

    def faz_insercao(self,tabela,registros):
        conn, cursor = self.get_connection()

        for registro in registros:
            sql = self.retorna_insercao(tabela,registro)
            cursor.execute(sql)
        
        conn.commit()

        conn.close()

    def get_registers(self,tabela):
        conn, cursor = self.get_connection()
        sql = "select * from "+tabela

        cursor.execute(sql)
        register = cursor.fetchall()

        conn.commit()
        conn.close()

        return register

