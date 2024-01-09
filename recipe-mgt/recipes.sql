CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(100) NOT NULL,
    role ENUM('admin', 'user') DEFAULT 'user',
    name VARCHAR(100),
    bio TEXT,
    profile_picture_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    -- Other preferences/settings columns...
);


CREATE TABLE Recipes (
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



