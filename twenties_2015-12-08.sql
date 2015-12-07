# ************************************************************
# Sequel Pro SQL dump
# Version 4499
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: localhost (MySQL 5.6.27)
# Database: twenties
# Generation Time: 2015-12-07 17:00:50 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table apply
# ------------------------------------------------------------

DROP TABLE IF EXISTS `apply`;

CREATE TABLE `apply` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `group` int(11) NOT NULL,
  `name` char(255) NOT NULL DEFAULT '',
  `phone` char(255) NOT NULL DEFAULT '',
  `university` char(255) NOT NULL DEFAULT '',
  `gender` char(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `apply` WRITE;
/*!40000 ALTER TABLE `apply` DISABLE KEYS */;

INSERT INTO `apply` (`id`, `group`, `name`, `phone`, `university`, `gender`)
VALUES
	(1,1,'ㅇ','ㅇ','유니스트','남자'),
	(2,1,'ㅇ','ㅇ','유니스트','남자'),
	(3,1,'ㅇ','ㅇ','유니스트','남자'),
	(4,2,'ㅂ','ㅂ','유니스트','남자'),
	(5,2,'ㅈ','ㅈ','유니스트','남자'),
	(6,2,'ㄷ','ㄷ','유니스트','남자'),
	(7,3,'ㅋ','ㅋ','유니스트','남자'),
	(8,3,'ㅌ','ㅌ','유니스트','남자'),
	(9,3,'ㅋ','ㅋ','유니스트','남자'),
	(10,4,'d','dg','유니스트','남자'),
	(11,4,'d','df','유니스트','남자'),
	(12,4,'d','dd','유니스트','남자'),
	(13,5,'공대선','01048147786','유니스트','남자'),
	(14,5,'정인중','01072249537','유니스트','남자'),
	(15,5,'김도경','01025803571','유니스트','남자');

/*!40000 ALTER TABLE `apply` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
