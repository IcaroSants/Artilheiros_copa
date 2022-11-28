from airflow import DAG
from airflow.decorators import task
from  airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.connectPostgres import Connect
from src.extract import Extract
import re


def extrai_dados()->list:
        dataset = []
        
        extract = Extract("https://www.ogol.com.br/edition_stats.php?v=jt1&id_edicao=132894")
        tbody = extract.getTag("tbody")
        artilheiros_tbody = tbody[1]

        set_data = []
        for children in artilheiros_tbody.children:
            data = []
            for ele in children.children:
                data.append(ele.text)
            data[1] = re.sub("\W"," ",data[1])
                
            set_data.append(data)

        for rec in set_data:
            info = {}
            info["nome"] = rec[1]
            info["j"] = int(rec[2])
            info["g"] = int(rec[3])
            info["pen"] = int(rec[4])
            info["ag"] = int(rec[5])
            info["mpg"]= int(rec[6])
            info["gtit"]=int(rec[7])
            info["gsup"]=int(rec[8])
            info["gpts"]=int(rec[9])
            info["gvit"] = int(rec[10])
            info["grvv"] = int(rec[11])
            info["pge"] = int(rec[12])
            info["data_rodada"] = datetime.now().strftime("%d-%m-%Y")
                
            dataset.append(info)
        
        return dataset

def insere(ti)-> None:
        dataset = ti.xcom_pull(task_ids=['extracao'])[0]
        
        connect = Connect('localhost','copa','postgres','post12345')
        connect.faz_insercao('artilheiros_copa',dataset)
    


with DAG(dag_id="COPA", schedule_interval=timedelta(days=4,hours=12),start_date=datetime.now()) as dag:
    
    
    
   
    extrai = PythonOperator(
        task_id="extracao",
        python_callable=extrai_dados,
        do_xcom_push=True
    )

    insercao = PythonOperator(
        task_id="insercao",
        python_callable=insere
    )


   
   

    extrai >> insercao
