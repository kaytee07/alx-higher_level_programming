-- this create a table id_not_null on MySQL server
-- attribute names id INT with a default value of 1
-- name VARCHAR(256) script shouldn't fail if table exist

CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id`   INT          DEFAULT 1,
    `name` VARCHAR(256)
);
