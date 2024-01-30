
CREATE DATABASE IF NOT EXISTS zoo;

USE zoo;


CREATE TABLE animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    race VARCHAR(255),
    id_cage INT,
    date_naissance DATE,
    pays_origine VARCHAR(255)
);


CREATE TABLE cage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    superficie DECIMAL(10, 2),
    capacite_max INT
);
