-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-10-2025 a las 03:35:47
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
-- Base de datos: `flasktest`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admin_main`
--

CREATE TABLE `admin_main` (
  `id_admin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agente_virtual`
--

CREATE TABLE `agente_virtual` (
  `id_agenVitual` int(11) NOT NULL,
  `type_agent` varchar(60) NOT NULL,
  `level_access` varchar(60) NOT NULL,
  `status_agent` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('8ad00a0037ec');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo`
--

CREATE TABLE `grupo` (
  `id_group` int(11) NOT NULL,
  `name_group` varchar(60) NOT NULL,
  `description_group` varchar(255) NOT NULL,
  `date_creation_group` date NOT NULL,
  `id_creator_group_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `grupo`
--

INSERT INTO `grupo` (`id_group`, `name_group`, `description_group`, `date_creation_group`, `id_creator_group_fk`) VALUES
(2, 'GrupoGoat', 'Bienvenidos a mi humilder grupo :)', '2025-10-25', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `miembro_grupo`
--

CREATE TABLE `miembro_grupo` (
  `id_perfil_fk` int(11) NOT NULL,
  `id_group_fk` int(11) NOT NULL,
  `date_register_member` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfil`
--

CREATE TABLE `perfil` (
  `id_perfil` int(11) NOT NULL,
  `name_perfil` varchar(60) NOT NULL,
  `date_creation` date NOT NULL,
  `label_perfil` varchar(255) DEFAULT NULL,
  `description_perfil` text DEFAULT NULL,
  `img_perfil` varchar(255) DEFAULT NULL,
  `img_portada_perfil` varchar(255) DEFAULT NULL,
  `id_user_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `perfil`
--

INSERT INTO `perfil` (`id_perfil`, `name_perfil`, `date_creation`, `label_perfil`, `description_perfil`, `img_perfil`, `img_portada_perfil`, `id_user_fk`) VALUES
(1, 'Vicmax_098', '2025-10-21', NULL, NULL, NULL, NULL, 1),
(2, 'Diamon89', '2025-10-25', NULL, NULL, NULL, NULL, 2),
(3, 'ClavoUnClavito', '2025-10-25', NULL, NULL, NULL, NULL, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nameuser` varchar(60) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `is_activate` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `nameuser`, `email`, `password`, `is_activate`) VALUES
(1, 'Victor', 'victor01.25@gmail.com', 'scrypt:32768:8:1$9XGwWufk4zaKrdC8$ec863ea22edd3f3ed7fea5e3807df3422acb64cef307fed2cdd4bd2232063c872872197f7492d0860ce60ad4b4d5c0fa556de69b553037e45526f7eaefa389b2', 1),
(2, 'Oscar', 'oscar_gonzales@gmail.com', 'scrypt:32768:8:1$NqqOM14Tofkmf14v$30fe733fe27784e2cfc82f4bd74c12467aea42ed2ce568bef0a8bce0f26740c3282cd1fcc9908fb773f750646338e1de2964bf182377c607bbeb92ba17a5c647', 1),
(3, 'Pablito', 'pablo_artiaga@gmail.com', 'scrypt:32768:8:1$Vme9POcp8TVv6Auf$4b937664ea65f7747bbe008a374ba841ba6c3cf71be5b2e3bbc2791c91bed2082e8641cd8f3159faecead4e3de77ef028a191c545991d244d52321a0f98c6f4a', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `video`
--

CREATE TABLE `video` (
  `id_video` int(11) NOT NULL,
  `title_video` varchar(60) NOT NULL,
  `description_video` varchar(255) DEFAULT NULL,
  `publication_date_video` date NOT NULL,
  `miniatura_video` varchar(255) NOT NULL,
  `like_video` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `admin_main`
--
ALTER TABLE `admin_main`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indices de la tabla `agente_virtual`
--
ALTER TABLE `agente_virtual`
  ADD PRIMARY KEY (`id_agenVitual`),
  ADD UNIQUE KEY `level_access` (`level_access`),
  ADD UNIQUE KEY `type_agent` (`type_agent`);

--
-- Indices de la tabla `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indices de la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`id_group`),
  ADD UNIQUE KEY `name_group` (`name_group`),
  ADD KEY `id_creator_group_fk` (`id_creator_group_fk`);

--
-- Indices de la tabla `miembro_grupo`
--
ALTER TABLE `miembro_grupo`
  ADD PRIMARY KEY (`id_perfil_fk`,`id_group_fk`),
  ADD KEY `id_group_fk` (`id_group_fk`);

--
-- Indices de la tabla `perfil`
--
ALTER TABLE `perfil`
  ADD PRIMARY KEY (`id_perfil`),
  ADD UNIQUE KEY `id_user_fk` (`id_user_fk`),
  ADD UNIQUE KEY `name_perfil` (`name_perfil`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `nameuser` (`nameuser`);

--
-- Indices de la tabla `video`
--
ALTER TABLE `video`
  ADD PRIMARY KEY (`id_video`),
  ADD UNIQUE KEY `like_video` (`like_video`),
  ADD UNIQUE KEY `miniatura_video` (`miniatura_video`),
  ADD UNIQUE KEY `title_video` (`title_video`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `admin_main`
--
ALTER TABLE `admin_main`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `agente_virtual`
--
ALTER TABLE `agente_virtual`
  MODIFY `id_agenVitual` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `grupo`
--
ALTER TABLE `grupo`
  MODIFY `id_group` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `perfil`
--
ALTER TABLE `perfil`
  MODIFY `id_perfil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `video`
--
ALTER TABLE `video`
  MODIFY `id_video` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD CONSTRAINT `grupo_ibfk_1` FOREIGN KEY (`id_creator_group_fk`) REFERENCES `perfil` (`id_perfil`);

--
-- Filtros para la tabla `miembro_grupo`
--
ALTER TABLE `miembro_grupo`
  ADD CONSTRAINT `miembro_grupo_ibfk_1` FOREIGN KEY (`id_group_fk`) REFERENCES `grupo` (`id_group`),
  ADD CONSTRAINT `miembro_grupo_ibfk_2` FOREIGN KEY (`id_perfil_fk`) REFERENCES `perfil` (`id_perfil`);

--
-- Filtros para la tabla `perfil`
--
ALTER TABLE `perfil`
  ADD CONSTRAINT `perfil_ibfk_1` FOREIGN KEY (`id_user_fk`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
