-- 13. Number of shows by genre
SELECT tv_genres.name AS 'genre', COUNT(tv_genres.name) AS 'number_of_shows' FROM tv_genres, tv_show_genres WHERE tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY `number_of_shows` DESC;
