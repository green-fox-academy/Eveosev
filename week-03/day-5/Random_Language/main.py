from flask import Flask
from flask import render_template
import random

app = Flask(__name__)
hello_list = ['Bonjour', 'Salut', 'Hola', '¿Qué tal? ', 'Zdravstvuyte', 'Privet', 'Nǐn hǎo', 'Nǐ hǎo', 'Salve', 'Ciao',
            'Konnichiwa', 'Anyoung haseyo', 'Olá', 'Ahlan', 'Szia']

@app.route('/greet')
def greet():
    n = random.randint(0, 14)
    hello = hello_list[n]
    return render_template('greetJohn.html', Hello = hello)

if __name__ == '__main__':
    app.run()