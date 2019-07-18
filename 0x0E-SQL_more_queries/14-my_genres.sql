-- 14. My genres
SELECT tv_genres.name FROM tv_genres, tv_show_genres, tv_shows WHERE tv_genres.id IN (SELECT tv_show_genres.genre_id FROM tv_show_genres WHERE (SELECT tv_shows.id FROM tv_shows WHERE tv_shows.title = "Dexter") = tv_show_genres.show_id) GROUP BY tv_genres.name
