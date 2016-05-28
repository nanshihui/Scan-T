-- MySQL dump 10.13  Distrib 5.6.30, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: datap
-- ------------------------------------------------------
-- Server version	5.6.30-1

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
-- Table structure for table `http`
--

DROP TABLE IF EXISTS `http`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `http` (
  `ip` varchar(45) DEFAULT NULL,
  `cookie` text,
  `data` text,
  `host` varchar(45) DEFAULT NULL,
  `path` text,
  `username` varchar(45) DEFAULT NULL,
  `passwd` varchar(45) DEFAULT NULL,
  `method` varchar(45) DEFAULT NULL,
  `timeupdate` varchar(45) DEFAULT NULL,
  `pathsimple` varchar(200) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index2` (`ip`,`pathsimple`,`method`,`username`,`host`)
) ENGINE=InnoDB AUTO_INCREMENT=159 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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

--
-- Table structure for table `snifferdata`
--

DROP TABLE IF EXISTS `snifferdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `snifferdata` (
  `ip` varchar(45) DEFAULT NULL,
  `port` int(11) DEFAULT NULL,
  `timesearch` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `product` varchar(45) DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  `script` text,
  `detail` text,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `head` text,
  `portnumber` varchar(8) DEFAULT NULL,
  `hackinfo` text,
  `keywords` text,
  `disclosure` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index2` (`ip`,`port`),
  FULLTEXT KEY `cnFullIndex` (`version`,`product`,`head`,`detail`,`script`,`hackinfo`,`disclosure`,`keywords`) /*!50100 WITH PARSER `mysqlcft` */ 
) ENGINE=MyISAM AUTO_INCREMENT=5232647 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `subdomain`
--

DROP TABLE IF EXISTS `subdomain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subdomain` (
  `domain` varchar(100) NOT NULL,
  `ip` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`domain`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `taskdata`
--

DROP TABLE IF EXISTS `taskdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taskdata` (
  `username` varchar(45) DEFAULT NULL,
  `taskid` varchar(45) NOT NULL,
  `taskname` varchar(45) DEFAULT NULL,
  `taskprior` varchar(45) DEFAULT NULL,
  `taskstatus` varchar(45) DEFAULT NULL,
  `starttime` varchar(45) DEFAULT NULL,
  `taskaddress` varchar(45) NOT NULL,
  `taskport` varchar(45) NOT NULL,
  `result` text,
  `endtime` varchar(45) DEFAULT NULL,
  `createtime` varchar(45) DEFAULT NULL,
  `forcesearch` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`taskid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user_table`
--

DROP TABLE IF EXISTS `user_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_table` (
  `username` varchar(45) NOT NULL,
  `role` varchar(45) DEFAULT NULL,
  `userpower` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`username`)
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

-- Dump completed on 2016-05-28 16:05:45
