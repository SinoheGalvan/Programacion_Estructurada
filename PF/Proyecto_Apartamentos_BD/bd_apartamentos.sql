-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-08-2025 a las 03:19:30
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
(5, 105, 'Calle Norte 654', 'SI', 'Apartamento con patio y cochera'),
(7, 107, 'Calle Jardín 111', 'NO', 'Loft moderno cerca del metro'),
(11, 213, 'AVENIDA DEL SUR', 'NO', 'AMPLIO'),
(12, 512, 'CALLE DEL AMANANECER 512', 'SI', 'PEQUEÑO'),
(13, 932, 'CALLE AZUL 932', 'NO', 'GRANDE'),
(14, 333, 'ST. MYKE TOWERS', 'SI', 'GRANDE Y LUJOSO'),
(21, 120, 'BLVD DURANGO 120', 'SI', '2 PISOS'),
(25, 212, 'CALLE OCAMPO 212', 'NO', 'MEDIANO 2 HABITACIONES Y UN BAÑO'),
(26, 89, 'AVENIDA DEL LAGO', 'NO', 'APARTAMENTO PEQUEÑO CON 1 CUARTO');

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
(13, 'CARLOS RAMÍREZ', '554876543', 120, '3000', '5 DE FEBRERO', 'NO PAGADO'),
(37, 'EMILIO', '490392', 333, '4999', '4 DE JUNIO', 'PAGADO'),
(40, 'ALDO', '49023932', 105, '4000', '4 DE JULIO', 'PAGADO'),
(43, 'JUAN PABLO', '94283921', 512, '9999', '4 DE MAYO', 'NO PAGADO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `contrasena` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `correo`, `contrasena`) VALUES
(1, 'adrian@gmail.com', '1d6442ddcfd9db1ff81df77cbefcd5afcc8c7ca952ab3101ede17a84b866d3f3'),
(2, 'lol', 'a0e570324e6ffdbc6b9c813dec968d9bad134bc0dbb061530934f4e59c2700b9');

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
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `apartamentos`
--
ALTER TABLE `apartamentos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `ID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
