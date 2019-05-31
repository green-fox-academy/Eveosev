import json
import re
from datetime import datetime
import psycopg2

con = psycopg2.connect(
    host = '127.0.0.1',
    user = 'postgres',
    password = 'Winds147963!',
    database = 'slack2'
)

cur = con.cursor()

def openfile(filename):
    with open(filename) as r_file:
        file = json.load(r_file)
    return file

def get_uid_from_user(filename):
    u_id = set()
    error = []
    data = openfile(filename)
    for subdict in data:
        for key in subdict:
            if key == 'text':
                regex = r'[\@\<\"]([A-Z0-9]{9})[\>\"]'
                p = re.compile(regex)
                result = p.findall(subdict[key])
                for element in result:
                    u_id.add(element)
            elif key == 'user':
                try:
                    u_id.add(subdict[key])
                except:
                    error.append(subdict)
            elif key == 'reply_users':
                for element in subdict[key]:
                    u_id.add(element)
            elif key == 'reactions':
                for i in range(len(subdict['reactions'])):
                    for element in subdict[key][i]['users']:
                        u_id.add(element)
            elif key == 'edited':
                u_id.add(subdict[key]['user']) 
    return u_id

    
def get_and_insert_mention(filename, channel):
    file = openfile(filename)
    insert_mention_query = 'INSERT INTO mention (msg_id, u_id, channel) VALUES (%s, %s, %s)'
    regex = r'\@([A-Z0-9]{9})'
    p = re.compile(regex)
    for subdict in file:
        try:
            if 'client_msg_id' in subdict and 'text' in subdict:
                result = p.findall(subdict['text'])
                for element in result:
                    cur.execute(insert_mention_query, (subdict['client_msg_id'], element, channel,))
                    con.commit()
        except Exception as e:
            print(e)


def get_and_insert_message(filename, channel):
    file = openfile(filename)
    insert_message_query = 'INSERT INTO message (u_id, msg, channel, sent_at) VALUES (%s, %s, %s, %s)'
    for subdict in file:
        try:
            if 'client_msg_id' in subdict and 'user' in subdict:
                temp_time = datetime.fromtimestamp(float(subdict['ts'])).strftime('%Y-%m-%d %H:%M:%S')
                cur.execute(insert_message_query, (subdict['user'], subdict['text'], channel, temp_time))
                con.commit()
        except Exception as e:
            print(f'Error in message: {e}')
        

def get_and_insert_reaction(filename):
    file = openfile(filename)
    insert_reaction_query = 'INSERT INTO reaction (u_id, msg_id, reaction) VALUES (%s, %s, %s)'
    for subdict in file:
        try:
            temp_msg_id = subdict['client_msg_id']
            for item in subdict['reactions']:
                temp_name = item['name']
                for i in range(len(item['users'])):
                    cur.execute(insert_reaction_query, (item['users'][i], temp_msg_id, temp_name))
                    con.commit()
        except Exception as e:
            print(e)
