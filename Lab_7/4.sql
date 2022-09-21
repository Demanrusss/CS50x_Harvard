SELECT s.name
FROM songs as s
WHERE s.danceability > 0.75 AND s.energy > 0.75 AND s.valence > 0.75