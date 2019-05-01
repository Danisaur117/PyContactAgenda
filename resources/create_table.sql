CREATE DATABASE  IF NOT EXISTS `agenda`;
USE `agenda`;
SET NAMES utf8 ;

--
-- Estructura de la tabla `contacto`
--

DROP TABLE IF EXISTS `contacto`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `contacto` (
  `contactoId` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(25) COLLATE utf8_spanish2_ci NOT NULL,
  `apellido1` varchar(25) COLLATE utf8_spanish2_ci NOT NULL,
  `apellido2` varchar(25) COLLATE utf8_spanish2_ci NOT NULL,
  `telefono` int(9) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `direccion` varchar(100) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `codigoPostal` int(5) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `ciudad` varchar(25) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8_spanish2_ci DEFAULT NULL,
  `lastUpdate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`contactoId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

--
-- Volcado de datos para la tabla `contacto`
--

LOCK TABLES `contacto` WRITE;
INSERT INTO `contacto` VALUES (1,'Daniel','Belmonte','Urbano','961234567','San Roque 13','12045','JERICA','danisaur@gmail.com','2019-05-01 11:40:00');
INSERT INTO `contacto` VALUES (2,'Homer','Jay','Simpson','555123456','Falsa 123','45678','SPRINGFIELD','homer.simpson@yahoo.com','2019-05-01 11:41:00');
UNLOCK TABLES;
