CREATE DATABASE IF NOT EXISTS bank; 
USE bank;

CREATE TABLE IF NOT EXISTS User (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Using numeric ID instead of name
    name VARCHAR(50) UNIQUE,  -- Ensuring names are unique
    pass VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS entrys (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,  -- Now links to User(id)
    entry VARCHAR(150),
    amount INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
    
);

CREATE INDEX amount_index ON entrys(amount);
ALTER TABLE User ADD COLUMN mode varchar(30) DEFAULT 'system';
SELECT  * FROM User;
select * from entrys;
ALTER TABLE user DROP column mode;
delete from User where name = 'veer';
call total(12,@t); ----  
select @t;
DESCRIBE user;


