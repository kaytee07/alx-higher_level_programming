-- create a database 'htbn_0d_2' and 'user_0d_2'
-- the 'user_0d_2' should have only SELECT privilege in the
-- database 'hbtn_0d_2'
-- 'user_0d_2' password should be set to 'user_0d_2_pwd'
-- script shoyld not fail if user exist

CREATE DATABASE IF NOT EXISTS hbtn_od_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
