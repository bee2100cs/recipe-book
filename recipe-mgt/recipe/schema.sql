DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS recipe;

CREATE TABLE User (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    user_role ENUM('admin', 'user') DEFAULT 'user',
    bio TEXT,
    profile_pic VARCHAR(255)
);


CREATE TABLE recipe (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    instructions TEXT NOT NULL,
    servings INT,
    prep_time INT, -- in minutes
    cook_time INT, -- in minutes
    total_time INT, -- in minutes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    -- Add other relevant columns as needed:
    -- For example: difficulty, cuisine type, dietary information, etc.
);



