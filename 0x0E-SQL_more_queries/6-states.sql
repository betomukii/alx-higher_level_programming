-- creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on your MySQL server.
CREATES DATABASE IF NOT EXISTS 'hbtn_0d_usa';
CREATES TABLE IF NOT EXISTS 'hbtn_0d_usa'.'states'(
PRIMARY KEY('id'), 'id' INT	NOT NULL AUTO_INCREMENT,
'name' VARCHAR(256) NOT NULL);
