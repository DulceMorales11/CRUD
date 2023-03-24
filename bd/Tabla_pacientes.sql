-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-12-2022 a las 17:18:00
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `node_mysql`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carros`
--
create table 'pacientes'(
    'folio' int primary key auto_increment,
    'nombre' varchar(20) not null,
    'apellido_paterno' varchar(15)not null,
    'apellido_materno' varchar(15)not null,
    'edad' int not null,
    'direccion' varchar (100) not null,
    'codigo_postal' varchar (10) not null,
    'telefono' varchar (10) not null,
    'tipo_sangre' varchar (5) not null,
    'fecha_nacimiento' date not null
    `foto` varchar(45) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `carros`
--

insert into pacientes(nombre, apellido_paterno, apellido_materno, edad, direccion, codigo_postal, telefono, tipo_sangre, fecha_nacimiento)
values ('Dulce', 'Morales', 'Martinez', 21, '9 sur poniente', '29060', '9611240392', 'A1+', '2001-04-11');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carros`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carros`
--
ALTER TABLE `pacientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
