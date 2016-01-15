CREATE DATABASE  IF NOT EXISTS `datap` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `datap`;
-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: datap
-- ------------------------------------------------------
-- Server version	5.5.46-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ip_maindata`
--

DROP TABLE IF EXISTS `ip_maindata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ip_maindata` (
  `ip` varchar(30) NOT NULL,
  `vendor` varchar(45) DEFAULT NULL,
  `osfamily` varchar(45) DEFAULT NULL,
  `osgen` varchar(45) DEFAULT NULL,
  `accurate` varchar(45) DEFAULT NULL,
  `updatetime` varchar(45) DEFAULT NULL,
  `hostname` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `mac` varchar(60) DEFAULT NULL,
  `country` varchar(10) DEFAULT NULL,
  `country_id` varchar(16) DEFAULT NULL,
  `area` varchar(10) DEFAULT NULL,
  `area_id` int(11) DEFAULT '0',
  `region` varchar(15) DEFAULT NULL,
  `region_id` varchar(15) DEFAULT NULL,
  `city` varchar(15) DEFAULT NULL,
  `city_id` int(11) DEFAULT '0',
  `county` varchar(45) DEFAULT NULL,
  `county_id` int(11) DEFAULT NULL,
  `isp` varchar(15) DEFAULT NULL,
  `isp_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-12-31 11:32:23
