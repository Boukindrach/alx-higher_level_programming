-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT s.title, GROUP_CONCAT(g.genre_id) AS genres
FROM tv_shows AS s
INNER JOIN tv_show_genres AS g ON s.id = g.show_id
GROUP BY s.id, s.title
ORDER BY s.title;
