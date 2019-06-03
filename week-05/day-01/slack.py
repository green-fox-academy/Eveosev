# Slack
# Try to parse the Slack Project's data with functional programming principles in mind. Write unit tests as well. 
# You don't need to store it in the database.
import json
from pprint import pprint
import re

with open('thanks_channel_history.json') as f:
    data_of_thanks = json.load(f)


"""
Extract user_id
"""
#by functions

result = tuple(filter(lambda x: 'user' in x, data_of_thanks))

users = set(map(lambda x: x['user'], result))


#by for loop
users = set(i['user'] for i in data_of_thanks if 'user' in i)


"""
Extract msg_id
"""
result = tuple(filter(lambda x: 'user' in x and 'text' in x, data_of_thanks))

messages = tuple(map(lambda x: [x['user'], x['text'], x['ts']], result))

#pprint(messages)


"""
Extract reactions
"""
result = tuple(filter(lambda x: 'user' in x and 'client_msg_id' in x and 'reactions' in x, data_of_thanks))

reactions = tuple(map(lambda x: [x['client_msg_id'], x['reactions']], result))


"""
Extract mentions
"""

regex = r"\@([A-Z0-9]{9})"
p = re.compile(regex)

result1 = tuple(filter(lambda x: 'text' in x and'user' in x, data_of_thanks))

result2 = tuple(filter(lambda x: p.findall(x['text']) is not None, result1))

mentions = tuple(map(lambda x: [x['user'], p.findall(x['text'])], result2))

