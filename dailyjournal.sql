CREATE TABLE `Entry` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood_id`    INTEGER NOT NULL,
    `concept`    TEXT NOT NULL,
    `entry`    TEXT NOT NULL,
    `date`    TEXT NOT NULL,
   FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`) 
);

CREATE TABLE `Moods` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`	TEXT NOT NULL
);

INSERT INTO `Moods` VALUES (null, 'Happy');
INSERT INTO `Moods` VALUES (null, 'Sad');
INSERT INTO `Moods` VALUES (null, 'Angry');
INSERT INTO `Moods` VALUES (null, 'Ok');

INSERT INTO `Entry` VALUES (null, 1, "Python", "Python seems pretty straight forward so far", "Wed Apr 13 2022 10:11:33");
INSERT INTO `Entry` VALUES (null, 2, "SQL", "SQL may be fun eventually", "Wed Apr 13 2022 11:11:33");

DELETE FROM Entries WHERE id = 2

DELETE TABLE Entries
	