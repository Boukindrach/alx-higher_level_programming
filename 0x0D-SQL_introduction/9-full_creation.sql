-- script that creates a table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS `second_table` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NOT NULL,
  `score` INT NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `second_table` (`name`, `score`) VALUES
  ("John", 10),
  ("Alex", 3),
  ("Bob", 14),
  ("George", 8);
