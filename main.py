from flask import Flask, render_template, request
import sqlite3
import logging



logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('log.log')
logger.addHandler(handler) 

app = Flask(__name__)

@app.route("/home")
def screen_home():
    return render_template('index.html')

@app.route("/login")
def screen_login():
    return render_template('login.html')

@app.route("/register")
def screen_register():
    logger.info("Here's some Info")
    return render_template('register.html')

@app.route("/help")
def screen_help():
    return render_template("help.html")

@app.route("/about")
def screen_about():
    return render_template("about.html")

@app.route("/compras")
def screen_compras():
    

    return render_template("compras.html")

@app.route("/compras/carrinho")
def screen_carrinho():
    return render_template("carrinho.html")

@app.route('/login', methods= ['POST'])
def login():
    if request.method == 'POST':
        banco = sqlite3.connect('users.db')
        cursor = banco.cursor()
        email = request.form['email']
        password = request.form['password']
        usuarios = [email, password]
        try:
            cursor.execute(f"SELECT senha FROM usuarios WHERE nome = '{email}'")
            senha_banco = cursor.fetchall()
            try:
                if password == senha_banco[0][0]:
                    print('Login Efetuado')
                    @app.route('/home', methods=['POST'])
                    def screen():
                        return render_template('index.html')
                else:
                    print('senha incorreta')
            except Exception as error:
                print(error)
        except sqlite3.Error as error:

            print('Erro no Banco: ', error)


        return "Email: " + email + " <br> " + "Password: " + password



@app.route('/register', methods= ['POST'])
def register():
    if request.method == 'POST':
        banco = sqlite3.connect("users.db")
        cursor = banco.cursor()
        cursor.execute("SELECT id FROM usuarios")
        dado_lido = cursor.fetchall()

        nome = request.form['nome']
        if nome == '':
            nome = 'None'

        email: str = request.form['email']
        if email == '':
            email = 'None'

        password = request.form['password']
        if password == '':
            password = 'None'

        numero = request.form['numero']
        if numero == '':
            numero = 'None'
        
        id_existente = len(dado_lido) + 1
        usuarios = [('email =' + email), ('nome = ' + nome) ,("Senha = " + str(password)), ("numero = " + str(numero)), ("id = " + str(id_existente))]
        #print(usuarios[1][7:])
        
        
        try:
            cursor.execute("INSERT INTO usuarios VALUES('"+str(id_existente)+"', '"+str(email)+"', '"+str(password)+"', '"+str(numero)+"')")
            render_template('index.html')

            with open('usuarios.txt', 'a') as logs:
                logs.write(f"\n{str(usuarios)}\n")

        except sqlite3.Error as error:
            print("error no banco", error)
        finally:
            banco.commit()
        return ("Nome: " + nome + "Email: " + email + " <br> " + "Password: " + password + "<br>" + "Numero: " + numero)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(405)
def not_found(error):
    return render_template('405.html'), 405
@app.errorhandler(500)
def not_found(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
