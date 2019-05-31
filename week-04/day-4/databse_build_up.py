import psycopg2
import get_info_functions
import json

#connect to database
con = psycopg2.connect(
    host = '127.0.0.1',
    user = 'postgres',
    password = 'Winds147963!',
    database = 'slack2'
)

cur = con.cursor()

# Create user table
user_table_query = """CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    u_id VARCHAR(128)
);
"""

cur.execute(user_table_query)
con.commit()

result = get_info_functions.get_uid_from_user('./database/random_channel_history.json')
result2 = get_info_functions.get_uid_from_user('./database/thanks_channel_history.json')
result3 = get_info_functions.get_uid_from_user('./database/thanks_channel_replies.json')
user_id = result | result2 | result3

insert_query = 'INSERT INTO users (u_id) VALUES (%s)'
for element in user_id:
    cur.execute(insert_query, (element,))
    con.commit()

# Create a message table
message_table_query = """CREATE TABLE message(
    id SERIAL PRIMARY KEY,
    u_id VARCHAR(128),
    msg VARCHAR(10000),
    channel VARCHAR(128),
    sent_at Timestamp
);
"""
cur.execute(message_table_query)
con.commit()
get_info_functions.get_and_insert_message('./database/thanks_channel_history.json', 'thanks')
get_info_functions.get_and_insert_message('./database/random_channel_history.json', 'randon')

# Create a reaction table
reaction_table_query = """CREATE TABLE reaction(
    id SERIAL PRIMARY KEY,
    u_id VARCHAR(128),
    msg_id VARCHAR(128),
    reaction VARCHAR(128)
);
"""
cur.execute(reaction_table_query)
con.commit()
get_info_functions.get_and_insert_reaction('./database/thanks_channel_history.json')
get_info_functions.get_and_insert_reaction('./database/random_channel_history.json')

# Create mention table
mention_table_query = """CREATE TABLE if not exsist mention(
    msg_id VARCHAR(128),
    u_id VARCHAR(128),
    channel VARCHAR(128)
);
"""
cur.execute(mention_table_query)
con.commit()
get_info_functions.get_and_insert_mention('./database/thanks_channel_history.json', 'thanks')
get_info_functions.get_and_insert_mention('./database/random_channel_history.json', 'random')