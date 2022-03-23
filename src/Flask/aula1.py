import json
import json
from flask import Flask
## verbos http
#get - receber dados do resource
#post - enviar dados ou informçoes para serem processados por um resoucer
#put - atualiza um resoucer
#delete - deleta um resouce

## app.get(), app.post(), app.put(), app.delete() --> end points
app = Flask(__name__)
#abrir o arquivo json e atribuir a uma variavel

with open ("launch.json", 'r' ) as arquivo:
    clientes = json.load(arquivo)  
@app.route('/')
def raiz():
    return 'Bem vindo adicione clienta na url para obter a lista de clientes'
    
@app.route('/clientes')
def get_clientes():
    
    return print(clientes)

app.run(debug=True)
