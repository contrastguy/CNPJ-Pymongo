import csv
from csv  import reader
import json 
from pymongo import MongoClient


client = MongoClient("localhost",27017)

db = client.Desafio
collectionEmpresas = db.Empresas
collectionSocios = db.Sócios
collectionsEstabelecimentos = db.Estabelecimentos


login = {
    "name" :"name",
}



with open("flaskr\Socios0\Socios.csv",newline="\n",encoding="utf8") as file:
    linhas = csv.reader(file)
    n = next(linhas)
    count=0
    for row in linhas:
        a = {"CNPJ_BASICOS": row[0],
             "IDENTIFICADOR_DE_SOCIO": row[1],
             "NOME_DO_SOCIO(NO CASO PF)/RAZAO_SOCIAL(NO CASO SOCIAL)":row[2],
             "CPF/CNPJ_DO_SOCIO":row[3],
             "QUALIFICACAO_DO_SOCIO":row[4],
             "DATA_DE_ENTRADA_SOCIEDADE":row[5],
             "FAIXA_ETARIA":row[6]}
        collectionSocios.insert_one(a)
    file.close()    
       
with open("flaskr\Empresas0\Empresas.csv",newline="\n",encoding="utf8") as file:
    linhas = csv.reader(file)
    n = next(linhas)
    for row in linhas:
        a = {"CNPJ_BASICOS": row[0],
             "NATUREZA_JURIDICA": row[2],
             "RAZAO_SOCIAL/NOME_EMPRESARIAL":row[1],
             "QUALIFICACAO_DO_RESPONSAVEL":row[3],
             "CAPITAL_SOCIAL_DA_EMPRESA":row[4],
             "PORTE_DA_EMPRESA":row[5],
             "ENTE_FEDERATIVO_RESPONSAVEL":row[6]}
        collectionEmpresas.insert_one(a)
    file.close()    
    
with open("flaskr\Estabelecimentos0\Estabelecimentos.csv",newline="\n",encoding="utf8") as file:
    linhas = csv.reader(file)
    n = next(linhas)
    for row in linhas:
        a = {"CNPJ_BASICOS": row[0],
             "CNPJ_ORDEM": row[1],
             "CNPJ_DV":row[2],
             "IDENTIFICADOR_MATRIZ/FILIAL":row[3],
             "NOME_FANTASIA":row[4],
             "SITUACAO_CADASTRAL":row[5],
             "DATA_SITUACAO_CADASTRAL":row[6],
             "MOTIVO_SITUACAO_CADASTRAL":row[7],
             "NOME_DA_CIDADE_NO_EXTERIOR":row[8],
             "PAIS":row[9],
             "DATA_DE_INICIO_ATIVIDADE":row[10],
             "CNAE_FISCAL_PRINCIPAL":row[11],
             "CNAE_FISCAL_SECUNDARIA":row[12],
             "TIPO_DE_LOGRADOURO":row[13],
             "LOGRADOURO":row[14],
             "NUMERO":row[15],
             "COMPLEMENTO":row[16]}
        collectionsEstabelecimentos.insert_one(a)
    file.close()    
       

  
  
  