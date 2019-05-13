"""
Create a BlogPost class that has
   an author_name
   a title
   a text
   a publication_date
Create a few blog post objects:
   "Lorem Ipsum" titled by John Doe posted at "2000.05.04."
    Lorem ipsum dolor sit amet.
   "Wait but why" titled by Tim Urban posted at "2010.10.10."
    A popular long-form, stick-figure-illustrated blog about almost everything.
   "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
    Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.
"""

class BlogPost():
    author_name = ""
    title = ""
    text = ""
    publication_date = ""

bp1 = BlogPost()
bp2 = BlogPost()
bp3 = BlogPost()

bp1.author_name = "John Doe"
bp1.publication_date = "2000.05.04"
bp1.title = "John Doe"
bp1.text = "Lorem ipsum dolor sit amet."
bp2.author_name = "Tim Urban"
bp2.publication_date = "2010.10.10"
bp2.title = "Wait but why"
bp2.text = "A popular long-form, stick-figure-illustrated blog about almost everything."
bp3.author_name = "William Turton"
bp3.publication_date = "2017.03.28"
bp3.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
bp3.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."