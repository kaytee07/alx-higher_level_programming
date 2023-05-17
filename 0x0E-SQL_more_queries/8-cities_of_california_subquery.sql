-- list all cities of cali that can be found in the db
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN
      (SELECT `id`
        FROM `states`
	 WHERE `name` = "california")
ORDER BY `id`;
