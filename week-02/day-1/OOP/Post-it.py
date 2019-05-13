"""
Create a PostIt class that has
  a background_color
  a text on it
  a text_color
Create a few example post-it objects:
  an orange with blue text: "Idea 1"
  a pink with black text: "Awesome"
  a yellow with green text: "Superb!
"""
class PostIt(object):
    backgrounp_color = ""
    text_on_it = ""
    text_color = ""
    
post1 = PostIt()
post2 = PostIt()
post3 = PostIt()

post1.backgrounp_color = "orange"
post1.text_color = "blue"
post1.text_on_it = "Idea 1"
post2.backgrounp_color = "pink"
post2.text_color = "black"
post2.text_on_it = "Awesome"
post3.backgrounp_color = "yellow"
post3.text_color = "green"
post3.text_on_it = "Superb!"

print("Backgroud color: " + post1.backgrounp_color + " Text: " + post1.text_on_it
      + " Text color: " + post1.text_color)
print("Backgroud color: " + post2.backgrounp_color + " Text: " + post2.text_on_it
      + " Text color: " + post2.text_color)
print("Backgroud color: " + post3.backgrounp_color + " Text: " + post3.text_on_it
      + " Text color: " + post3.text_color)
  