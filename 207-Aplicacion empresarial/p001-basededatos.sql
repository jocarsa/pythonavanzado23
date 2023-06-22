CREATE DATABASE aplicacion

USE aplicacion

CREATE TABLE `aplicacion`.`productos` (
    `Identificador` INT(255) NOT NULL AUTO_INCREMENT ,
    `nombre` VARCHAR(255) NOT NULL , 
    `descripcion` VARCHAR(255) NOT NULL , 
    `precio` VARCHAR(255) NOT NULL , 
    PRIMARY KEY (`Identificador`)
) ENGINE = InnoDB;

CREATE TABLE `aplicacion`.`clientes` (
    `Identificador` INT(255) NOT NULL AUTO_INCREMENT , 
    `nombre` VARCHAR(255) NOT NULL , 
    `apellidos` VARCHAR(255) NOT NULL , 
    `email` VARCHAR(255) NOT NULL , 
    PRIMARY KEY (`Identificador`)
) ENGINE = InnoDB;

INSERT INTO `clientes`(`Identificador`, `nombre`, `apellidos`, `email`) VALUES (NULL,'JoseVicente','Carratalá','info@clase.com');
INSERT INTO `clientes`(`Identificador`, `nombre`, `apellidos`, `email`) VALUES (NULL,'Ana','García','info@clase.com');
INSERT INTO `clientes`(`Identificador`, `nombre`, `apellidos`, `email`) VALUES (NULL,'Rodrigo','Riquelme','info@clase.com');
INSERT INTO `clientes`(`Identificador`, `nombre`, `apellidos`, `email`) VALUES (NULL,'Henry','Serra','info@clase.com');
INSERT INTO `clientes`(`Identificador`, `nombre`, `apellidos`, `email`) VALUES (NULL,'Raul','Vecerra','info@clase.com');
INSERT INTO `clientes`(`Identificador`, `nombre`, `apellidos`, `email`) VALUES (NULL,'Tristán','Hernandez','info@clase.com');

INSERT INTO `productos`(`Identificador`, `nombre`, `descripcion`, `precio`) VALUES (NULL,'Vela de color azul','Decripción de la vela','2.00');
INSERT INTO `productos`(`Identificador`, `nombre`, `descripcion`, `precio`) VALUES (NULL,'Vela de azahar','Decripción de la vela','3.00');
INSERT INTO `productos`(`Identificador`, `nombre`, `descripcion`, `precio`) VALUES (NULL,'Vela de miel','Decripción de la vela','2.50');


CREATE USER 'aplicacion'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';GRANT USAGE ON *.* TO 'aplicacion'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;GRANT ALL PRIVILEGES ON `aplicacion`.* TO 'aplicacion'@'localhost';

CREATE TABLE `aplicacion`.`usuarios` (`Identificador` INT(255) NOT NULL AUTO_INCREMENT , `usuario` VARCHAR(255) NOT NULL , `contrasena` VARCHAR(255) NOT NULL , `nombrecompleto` VARCHAR(255) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;