
-- Create a view where you display the reviewer's name and the amount of their review
CREATE VIEW reviewer_movieAmount AS 
SELECT name, COUNT(*)
FROM Reviewer
LEFT JOIN Rating
    ON Reviewer.rid = Rating.rid
GROUP BY name;

SELECT * FROM reviewer_movieAmount;


-- Create a view where you display the movies which have no review
CREATE VIEW movie_no_review AS
SELECT title
FROM  Movie
LEFT JOIN Rating
    ON Movie.mID = Rating.mID
WHERE stars IS NULL;

SELECT * FROM movie_no_review;


-- Create a view where you display all the directors (do not include null values)
CREATE VIEW director AS
SELECT DISTINCT director
FROM Movie
WHERE director IS NOT NULL;

SELECT * FROM  director;


-- Create a view where you display the movie title and the average rating
CREATE VIEW movie_avgRating AS
SELECT title, ROUND(AVG(stars),2) AS avg_rating
FROM Movie
LEFT JOIN Rating
    ON Movie.mid = Rating.mid
GROUP BY title;

SELECT title, COALESCE(avg_rating, 0) AS avg_rating FROM movie_avgRating;