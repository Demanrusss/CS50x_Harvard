SELECT DISTINCT people.name
FROM people, stars, movies
WHERE movies.id = stars.movie_id
  AND stars.person_id = people.id
  AND movies.title IN (SELECT movies.title
                       FROM movies, stars, people
                       WHERE people.name = 'Kevin Bacon'
                         AND people.birth = 1958
                         AND people.id = stars.person_id
                         AND stars.movie_id = movies.id)
  AND NOT people.name = 'Kevin Bacon'