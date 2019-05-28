--SQL Movie-Rating Exercise Extra

--Q1
SELECT DISTINCT name
FROM  Reviewer
INNER JOIN Rating
    ON Reviewer.rID = Rating.rID
INNER JOIN Movie
    ON Rating.mID = Movie.mID
WHERE title = 'Gone with the Wind';


--Q2
SELECT DISTINCT name, title, stars
FROM Reviewer
INNER JOIN Movie
    ON Reviewer.name = Movie.director
INNER JOIN Rating
    ON Movie.mID = Rating.mID AND Reviewer.rid = Rating.rid;


--Q3
SELECT name, title
FROM Reviewer
LEFT JOIN Rating
    ON Reviewer.rID = Rating.rID
LEFT JOIN Movie
    ON Rating.mID = Movie.mID;


