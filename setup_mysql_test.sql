-- Creates a database hbnb_test_db
-- Adds a new user hbnb_test (in localhost)
-- Sets the password of hbnb_test should be set to hbnb_test_pwd
-- Grants hbnb_test all privileges on the database hbnb_test_db
-- Grants hbnb_test SELECT privilege on the database performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
