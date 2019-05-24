from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

hello_list = ['Bonjour', 'Salut', 'Hola', '¿Qué tal? ', 'Zdravstvuyte', 'Privet', 'Nǐn hǎo', 'Nǐ hǎo', 'Salve', 'Ciao',
            'Konnichiwa', 'Anyoung haseyo', 'Olá', 'Ahlan', 'Szia']

name_list = ['John', 'Levi', 'Steven', 'Claire', 'Zilan', 'Ted', 'Changdong', 'Ke', 'Haoxiang', 'Yu', 'Sara', 'Angela',
'Santi', 'Ray', 'Yuan']

products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)
]

authors = [
    {
        "id": 100,
        "name": "John",
        "likes": [
            202,
            200
        ]
    },
    {
        "id": 101,
        "name": "Jane",
        "likes" : [
            200
        ]
    }
]

posts = [
    {
        "id": 200,
        "author": 100,
        "content": "Difficulty on insensible reasonable in. From as went he they."
    },
    {
        "id": 201,
        "author": 100,
        "content": "Preference themselves me as thoroughly partiality considered on in estimating."
    },
    {
        "id": 202,
        "author": 101,
        "content": "In as name to here them deny wise this. As rapid woody my he me which."
    }
]


articles = [
    {
        "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
        "seen": ["John", "Jane", "Bob"]
    },
    {
        "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
        "seen": ["John", "Jane"]
    },
    {
        "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
        "seen": ["John"]
    },
    {
        "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
        "seen": []
    }
]

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route("/posts")
def list_posts():
    transformed_posts = [authors, posts]
    return render_template("posts.html", post=transformed_posts)

@app.route('/greet')
def greet():
    n = random.randint(0, 14)
    hello = hello_list[n]
    return render_template('greetJohn.html', Hello = hello)

@app.route('/greet2')
def greet2():
    n_greet = random.randint(0, 14)
    hello = hello_list[n_greet]
    n_name = random.randint(0,14)
    name = name_list[n_name]
    return render_template('greetJohn2.html', Hello = hello, Name = name)

@app.route('/product')
def display_products():
    return render_template('product.html', p = products)

@app.route("/articles")
def list_articles():
    return render_template("articles.html", articles=articles)

if __name__ == '__main__':
    app.run()