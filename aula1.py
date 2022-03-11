from flask import Flask,jsonify 

app = Flask(__name__)
@app.route('/')
def raiz():
    return 'hello world'

@app.route('/rota3')
def rota3():
    return '<H1> HOJE TEM FIFIL? EMMMMMMMMMMMM?</H1>'

@app.route('/em')
def em():
    return '<H1> EMMMMMMMM?</H1>'
@app.route('/game/<string:nome>/<string:hora>')
def games(nome,hora):
    return jsonify({'nome':nome,'hora':hora})

app.run(debug=True)
