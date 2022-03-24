import json
from flask import Flask, render_template
## verbos http
#get - receber dados do resource
#post - enviar dados ou informçoes para serem processados por um resoucer
#put - atualiza um resoucer
#delete - deleta um resouce
## app.get(), app.post(), app.put(), app.delete() --> end points

app = Flask(__name__)

#criar a primeira  pagina da aplicação
#route -- > cria a rota www.site.com.br/cliente
#função -- > oque deseja exibir na pagina
#templates

#abrir o arquivo json e atribuir a uma variavel
with open ("launch.json", 'r' ) as arquivo:
    clientes = json.load(arquivo)  
    arquivo.close()
@app.route('/') #decorator "@" atribui uma nova função para a função seguinte
def raiz():
    return 'Bem vindo adicione clienta na url para obter a lista de clientes'
    
@app.route('/clientes')
def get_clientes():
    
    return f"{clientes}"

#return render_template(clinte.html , var_do_hmtl = <clienter>) ou .css 
#<cliente> valor passado do usuario
@app.route("/usuario/<nome_usuario>")
def usuarios(nome_usuario) :
   return render_template("usuario.html",nome_usuario=nome_usuario)

#coloca o site no ar
if __name__ == "__main__": 
    #executa as linhas abaixo caso esse arquivo seja executado na raiz apenas e nao em outro arquivo que o importe.
    app.run(debug=True)
