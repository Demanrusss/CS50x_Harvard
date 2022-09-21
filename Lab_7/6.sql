SELECT songs.name
FROM songs, artists
WHERE artists.name LIKE '%Post Malone%'
AND songs.artist_id = artists.id