-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-08-2025 a las 06:01:49
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_apartamentos`
--
CREATE DATABASE IF NOT EXISTS `bd_apartamentos` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `bd_apartamentos`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `apartamentos`
--

CREATE TABLE `apartamentos` (
  `id` int(11) NOT NULL,
  `apartamento` int(11) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `ocupado` varchar(10) NOT NULL,
  `descripcion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `apartamentos`
--

INSERT INTO `apartamentos` (`id`, `apartamento`, `direccion`, `ocupado`, `descripcion`) VALUES
(1, 101, 'Av. Central 123', 'SI', 'Apartamento con balcón y vista al parque'),
(2, 102, 'Calle Sur 456', 'NO', 'Apartamento sin amueblar, ideal para estudiantes'),
(3, 103, 'Paseo del Lago 789', 'SI', 'Apartamento de lujo con dos recámaras'),
(4, 104, 'Av. Reforma 321', 'SI', 'Estudio compacto con cocina integrada'),
(5, 105, 'Calle Norte 654', 'NO', 'Apartamento con patio y cochera'),
(6, 106, 'Blvd. Sol 987', 'NO', 'Apartamento familiar con 3 habitaciones'),
(7, 107, 'Calle Jardín 111', 'SI', 'Loft moderno cerca del metro'),
(8, 108, 'Av. Palma 222', 'SI', 'Departamento con jardín privado'),
(9, 109, 'Av. Roble 333', 'NO', 'Apartamento remodelado recientemente'),
(10, 110, 'Calle Río 444', 'SI', 'Penthouse con terraza y jacuzzi'),
(11, 213, 'AVENIDA DEL SUR', 'NO', 'AMPLIO'),
(12, 512, 'CALLE DEL AMANANECER 512', 'SI', 'PEQUEÑO'),
(13, 932, 'CALLE AZUL 932', 'SI', 'GRANDE'),
(14, 333, 'ST. MYKE TOWERS', 'NO', 'GRANDE Y LUJOSO'),
(21, 120, 'BLVD DURANGO 120', 'NO', '2 PISOS');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `ID` int(255) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `TELEFONO` varchar(20) NOT NULL,
  `APARTAMENTO` int(11) NOT NULL,
  `MONTO` varchar(10) NOT NULL,
  `DIA` varchar(30) NOT NULL,
  `ESTATUS` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`ID`, `NOMBRE`, `TELEFONO`, `APARTAMENTO`, `MONTO`, `DIA`, `ESTATUS`) VALUES
(12, 'MARÍA GARCÍA', '554412334', 101, '2500', '10 DE ENERO', 'PAGADO'),
(13, 'CARLOS RAMÍREZ', '554876543', 932, '3000', '5 DE FEBRERO', 'NO PAGADO'),
(14, 'LAURA MARTÍNEZ', '555123456', 103, '2700', '15 DE MARZO', 'PAGADO'),
(18, 'VALERIA TORRES', '559012345', 107, '2900', '8 DE JULIO', 'NO PAGADO'),
(19, 'FERNANDO RIVAS', '550123456', 108, '2800', '30 DE AGOSTO', 'PAGADO'),
(27, 'RODRI', '3922831', 512, '9999', '5 DE NOVIEMBRE', 'PAGADO'),
(28, 'LESLI', '4902931', 110, '2000', '25 DE JULIO', 'PAGADO'),
(33, 'JUAN', '3920230', 104, '3000', '3 DE MAYO', 'PAGADO');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `apartamentos`
--
ALTER TABLE `apartamentos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `apartamento` (`apartamento`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `APARTAMENTO` (`APARTAMENTO`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `apartamentos`
--
ALTER TABLE `apartamentos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `ID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`APARTAMENTO`) REFERENCES `apartamentos` (`apartamento`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
