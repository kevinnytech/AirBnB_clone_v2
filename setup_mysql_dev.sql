-- Creates a database hbnb_dev_db
-- Adds a new user hbnb_dev (in localhost)
-- Sets the password of hbnb_dev should be set to hbnb_dev_pwd
-- Grants hbnb_dev all privileges on the database hbnb_dev_db
-- Grants hbnb_dev SELECT privilege on the database performance_schema
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
