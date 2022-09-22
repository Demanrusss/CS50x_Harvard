SELECT DISTINCT people.name
FROM people, directors, ratings, movies
WHERE ratings.rating >= 9.0
  AND ratings.movie_id = movies.id
  AND people.id = directors.person_id
  AND directors.movie_id = movies.id