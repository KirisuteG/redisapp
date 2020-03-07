CREATE SCHEMA database0;


CREATE TABLE `data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` timestamp(3) NOT NULL,
  `temperature` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci