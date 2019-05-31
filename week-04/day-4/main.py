import psycopg2
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import pandas
import numpy as np
import seaborn as sns

#connect to database
con = psycopg2.connect(
    host = '127.0.0.1',
    user = 'postgres',
    password = 'Winds147963!',
    database = 'slack2'
)

cur = con.cursor()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/message')
def messages():
    return render_template('messages.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/specific_user')
def single_user():
    return render_template('specific_user.html')

# @app.route('/specific_user/<u_id>', method=['GET'])
# def check_u_id(u_id):
#     u_id = request.form['u_id']
#     select_query = f'SELECT u_id, COUNT(*) FROM'
#     cur.execute(select_query)
#     select_data = cur.fetchall()


# Who sent the most messages?
q1_query = "SELECT u_id, COUNT(*) AS C FROM message GROUP BY u_id ORDER BY C DESC LIMIT 5"
cur.execute(q1_query)
q1_data = cur.fetchall()

# visualization
# plt.style.use('ggplot')
sns.set(style="darkgrid")
u_id_q1, fre_q1 = zip(*q1_data)
xs1 = np.arange(len(u_id_q1)) 
width = 0.5
plt.bar(xs1, fre_q1, width, align='center', color = 'green')
plt.xticks(xs1, u_id_q1) #Replace default x-ticks with xs, then replace xs with labels
for i in xs1:
    plt.annotate(f'{fre_q1[i]}', xy = (i, fre_q1[i]))
plt.xlabel('User ID')
plt.ylabel('Frequency')
plt.title('The top 5 person who sent most messages')
avg_post = 16
plt.axhline(y=avg_post, linewidth=1, color = 'k')
plt.savefig('post_most_message.png')
plt.clf()

# # #Who is the most mentioned person in the thanks channel?
q2_query = "SELECT u_id, COUNT(*) AS C FROM MENTION GROUP BY u_id ORDER BY C DESC LIMIT 5"
cur.execute(q2_query)
q2_data = cur.fetchall()
sns.set(style="darkgrid")
# plt.style.use('ggplot')
u_id_q2, fre_q2 = zip(*q2_data)
xs2 = np.arange(len(u_id_q2)) 
width = 0.5
plt.bar(xs2, fre_q2, width, align='center', color = 'green')
plt.xticks(xs2, u_id_q2) #Replace default x-ticks with xs, then replace xs with labels
for i in xs2:
    plt.annotate(f'{fre_q2[i]}', xy = (i, fre_q2[i]))
plt.xlabel('User ID')
plt.ylabel('Frequency')
avg_mentioned = 15
plt.axhline(y=avg_mentioned, linewidth=1, color = 'k')
plt.title('Top 5 persons who are the most mentioned')
plt.savefig('most_mentioned_person.png')
plt.clf()

# Who reacted to the most messages?
q3_query = 'SELECT u_id, COUNT(*) AS C FROM reaction GROUP BY u_id ORDER BY C DESC LIMIT 5'
cur.execute(q3_query)
q3_data = cur.fetchall()
u_id_q3, fre_q3 = zip(*q3_data)
# plt.style.use('ggplot')
sns.set(style="darkgrid")
xs3 = np.arange(len(u_id_q3)) 
width = 0.5
plt.bar(xs3, fre_q3, width, align='center', color = 'green')
plt.xticks(xs3, u_id_q3) #Replace default x-ticks with xs, then replace xs with labels
for i in xs3:
    plt.annotate(f'{fre_q3[i]}', xy = (i, fre_q3[i]))
plt.xlabel('User ID')
plt.ylabel('Frequency')
avg_reaction = 96
plt.axhline(y=avg_reaction, linewidth=1, color = 'k')
plt.title('The top 5 person who reacted most messages')
plt.savefig('reacted_most_person.png')

#further analysis
ideal_user = set(q3_data) | set(q2_data) | set(q1_data)

cur.close()
con.close()

# if __name__ == "__main__":
#     app.run()
