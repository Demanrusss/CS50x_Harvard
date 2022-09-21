SELECT AVG(songs.energy) AS [Average Energy]
FROM songs, artists
WHERE artists.name = 'Drake'
AND songs.artist_id = artists.id