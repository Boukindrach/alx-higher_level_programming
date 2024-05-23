--
SELECT t.`title`, SUM(r.`rate`) AS `rating`
FROM `tv_shows` AS t
INNER JOIN `tv_show_ratings` AS r ON t.`id` = r.`show_id`
GROUP BY t.`title`
ORDER BY `rating` DESC;
