import requests
import time

#criar decorator calclar tempo
def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        print("vou pegar a cotacao")
        funcao()
        print("peguei a cotacao")
        tempo_final = time.time()
        print(f"tempo de operacao foi:{tempo_final - tempo_inicial} segundos")
    return wrapper


@calcular_tempo
def pegar_cotacao_dolar():
    link = f'https://economia.awesomeapi.com.br/last/USD-BRL'
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_cotacao_dolar()
