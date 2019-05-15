"""
    You can find some posts and their comments in this file. 
    Now you need to find the post which got the most popular comments. 
    Most popular comments mean the sum of the likes on the comments.
"""
import json
#Read file.json by using json
#with open(filename, 'rb') as f
#jsondata = json.loads(f.read())

def findpopularpost(filename):
    try:
        with open(filename, 'rb') as f_post:
            jsondata = json.loads(f_post.read())
        sumlike_list = []
        for i in range(len(jsondata)):
            temp = 0
            if jsondata[i]['comments'] == None:
                sumlike_list.append(temp)
            else: 
                for j in range(len(jsondata[i]['comments'])):
                    temp = temp + jsondata[i]['comments'][j]['like_count']
                sumlike_list.append(temp)
        popindex = sumlike_list.index(max(sumlike_list))
        print(f"The most popular posts with maximum {max(sumlike_list)} like is ")
        return jsondata[popindex]
    except:
        print("Please enter a correct filename")

findpopularpost('posts.json')
