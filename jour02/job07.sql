
CREATE DATABASE IF NOT EXISTS job07;

USE job07;


CREATE TABLE employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10, 2),
    id_service INT
);


INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
    ('frah', 'mohamed', 3500000.00, 1),
    ('clavis', 'tom', 4.00, 2),
    ('beaussareat', 'val', 3000.00, 1),
    ('messi ', 'leo', 4500.00, 2),
    ('ronaldo', 'Chris', 2800.00, 1);

CREATE TABLE service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255)
);


INSERT INTO service (nom) VALUES
    ('Service RH'),
    ('Service Informatique'),
    ('Service Marketing');


