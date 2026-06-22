-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 22 juin 2026 à 13:34
-- Version du serveur : 8.0.45
-- Version de PHP : 8.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `workshop_archilog`
--

-- --------------------------------------------------------

--
-- Structure de la table `activites`
--

DROP TABLE IF EXISTS `activites`;
CREATE TABLE IF NOT EXISTS `activites` (
  `id_act` int NOT NULL AUTO_INCREMENT,
  `titre_act` varchar(50) NOT NULL,
  `date_act` date NOT NULL,
  `lieu_act` varchar(50) NOT NULL,
  `description_act` varchar(500) NOT NULL,
  `url_image_act` varchar(500) NOT NULL,
  `dangerosite_max_act` int NOT NULL,
  `id_createur` int NOT NULL,
  PRIMARY KEY (`id_act`),
  KEY `foreignkey_activites_user` (`id_createur`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `activites`
--

INSERT INTO `activites` (`id_act`, `titre_act`, `date_act`, `lieu_act`, `description_act`, `url_image_act`, `dangerosite_max_act`, `id_createur`) VALUES
(1, 'Promenade dans les bois', '2026-06-26', 'ici', 'test', 'https://static.actu.fr/uploads/2020/11/site-repainville-rouen-960x640.jpg', 4, 1);

-- --------------------------------------------------------

--
-- Structure de la table `activites_animal_user`
--

DROP TABLE IF EXISTS `activites_animal_user`;
CREATE TABLE IF NOT EXISTS `activites_animal_user` (
  `id_act` int NOT NULL,
  `id_user` int NOT NULL,
  `id_animal` int NOT NULL,
  KEY `foreignkey_triades_animal` (`id_animal`),
  KEY `foreignkey_triades_user` (`id_act`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `activites_animal_user`
--

INSERT INTO `activites_animal_user` (`id_act`, `id_user`, `id_animal`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `animal`
--

DROP TABLE IF EXISTS `animal`;
CREATE TABLE IF NOT EXISTS `animal` (
  `id_animal` int NOT NULL AUTO_INCREMENT,
  `nom_animal` varchar(30) NOT NULL,
  `age_animal` int NOT NULL,
  `type_animal` varchar(50) NOT NULL,
  `url_image_animal` varchar(500) NOT NULL,
  `description_animal` varchar(500) NOT NULL,
  `id_user` int NOT NULL,
  `danger` int NOT NULL,
  PRIMARY KEY (`id_animal`),
  KEY `foreignkey_animal_user` (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `animal`
--

INSERT INTO `animal` (`id_animal`, `nom_animal`, `age_animal`, `type_animal`, `url_image_animal`, `description_animal`, `id_user`, `danger`) VALUES
(1, 'Julien', 5, 'Chien', 'https://media.licdn.com/dms/image/v2/D4E03AQEW-WqPYIMsrw/profile-displayphoto-shrink_800_800/B4EZUk8udkG0Ac-/0/1740081654140?e=1783555200&v=beta&t=wHjllaFs5JuPokLFge7KGMXkW2pt7XZU8h475Dgwnuo', 'Vie que la nuit\r\nSuper dangereux\r\nDans les montagnes et les forêts\r\nMange les mouches', 1, 3);

-- --------------------------------------------------------

--
-- Structure de la table `commentaire`
--

DROP TABLE IF EXISTS `commentaire`;
CREATE TABLE IF NOT EXISTS `commentaire` (
  `id_commentaire` int NOT NULL AUTO_INCREMENT,
  `commentaire` varchar(500) NOT NULL,
  `note` int NOT NULL,
  `id_user` int NOT NULL,
  `id_animal` int NOT NULL,
  PRIMARY KEY (`id_commentaire`),
  KEY `foreignkey_commentaire_user` (`id_user`),
  KEY `foreignkey_commentaire_animal` (`id_animal`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `commentaire`
--

INSERT INTO `commentaire` (`id_commentaire`, `commentaire`, `note`, `id_user`, `id_animal`) VALUES
(1, 'Chien très dangereux', 3, 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `prenom_user` varchar(30) NOT NULL,
  `nom_user` varchar(30) NOT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id_user`, `username`, `password`, `prenom_user`, `nom_user`) VALUES
(1, 'admin', 'admin', 'AgaClocloLuci', 'Admin');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `activites`
--
ALTER TABLE `activites`
  ADD CONSTRAINT `foreignkey_activites_user` FOREIGN KEY (`id_createur`) REFERENCES `user` (`id_user`) ON DELETE CASCADE ON UPDATE RESTRICT;

--
-- Contraintes pour la table `activites_animal_user`
--
ALTER TABLE `activites_animal_user`
  ADD CONSTRAINT `foreignkey_triades_activites` FOREIGN KEY (`id_act`) REFERENCES `activites` (`id_act`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `foreignkey_triades_animal` FOREIGN KEY (`id_animal`) REFERENCES `animal` (`id_animal`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `foreignkey_triades_user` FOREIGN KEY (`id_act`) REFERENCES `animal` (`id_animal`) ON DELETE CASCADE ON UPDATE RESTRICT;

--
-- Contraintes pour la table `animal`
--
ALTER TABLE `animal`
  ADD CONSTRAINT `foreignkey_animal_user` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`) ON DELETE CASCADE ON UPDATE RESTRICT;

--
-- Contraintes pour la table `commentaire`
--
ALTER TABLE `commentaire`
  ADD CONSTRAINT `foreignkey_commentaire_animal` FOREIGN KEY (`id_animal`) REFERENCES `animal` (`id_animal`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `foreignkey_commentaire_user` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`) ON DELETE CASCADE ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
