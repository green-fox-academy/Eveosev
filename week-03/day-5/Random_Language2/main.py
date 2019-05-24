from flask import Flask
from flask import render_template
import random

app = Flask(__name__)
hello_list = ['Bonjour', 'Salut', 'Hola', '¿Qué tal? ', 'Zdravstvuyte', 'Privet', 'Nǐn hǎo', 'Nǐ hǎo', 'Salve', 'Ciao',
            'Konnichiwa', 'Anyoung haseyo', 'Olá', 'Ahlan', 'Szia']
name_list = ['John', 'Levi', 'Steven', 'Claire', 'Zilan', 'Ted', 'Changdong', 'Ke', 'Haoxiang', 'Yu', 'Sara', 'Angela',
'Santi', 'Ray', 'Yuan']

@app.route('/greet')
def greet():
    n_greet = random.randint(0, 14)
    hello = hello_list[n_greet]
    n_name = random.randint(0,14)
    name = name_list[n_name]
    return render_template('greetJohn.html', Hello = hello, Name = name)

if __name__ == '__main__':
    app.run()