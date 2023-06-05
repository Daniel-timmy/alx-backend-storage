-- creates a table users
-- with the following attributes
CREATE TABLE IF NOT EXISTS users ( 
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
	email  VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255));
