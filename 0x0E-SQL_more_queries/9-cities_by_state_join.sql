-- this list all cities conatained in the db

SELECT c.`id`, c.`name`, s.`name`
FROM `cities` AS c
INNER JOIN `state` AS s
ON c.`state_id` = s.`id`
ORDER BY c.`id`;
