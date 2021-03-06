DROP DATABASE IF EXISTS mus;
CREATE DATABASE mus CHARACTER SET 'utf8';

USE mus;

CREATE TABLE User (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL,
    avatar VARCHAR(100),
    PRIMARY KEY (id)
)
ENGINE=INNODB;

CREATE TABLE Message (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    userId SMALLINT UNSIGNED NOT NULL,
    date DATETIME NOT NULL,
    text TEXT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (userId) REFERENCES User(id)
)
ENGINE=INNODB;

CREATE TABLE Team (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    user1Id SMALLINT UNSIGNED NOT NULL,
    user2Id SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user1Id) REFERENCES User(id),
    FOREIGN KEY (user2Id) REFERENCES User(id),
    UNIQUE INDEX ind_uni_user1_user2 (user1Id, user2Id)
)
ENGINE=INNODB;

CREATE TABLE Round (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    team1Id SMALLINT UNSIGNED NOT NULL,
    team2Id SMALLINT UNSIGNED NOT NULL,
    date DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (team1Id) REFERENCES Team(id),
    FOREIGN KEY (team2Id) REFERENCES Team(id)
)
ENGINE=INNODB;

CREATE TABLE Score (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    roundId INT UNSIGNED NOT NULL,
    teamId SMALLINT UNSIGNED NOT NULL,
    value SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (roundId) REFERENCES Round(id),
    FOREIGN KEY (teamId) REFERENCES Team(id),
    UNIQUE INDEX ind_uni_roundId_teamId (roundId, teamId)
)
ENGINE=INNODB;
