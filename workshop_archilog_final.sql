-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 25 juin 2026 à 10:06
-- Version du serveur : 8.4.7
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `activites`
--

INSERT INTO `activites` (`id_act`, `titre_act`, `date_act`, `lieu_act`, `description_act`, `url_image_act`, `dangerosite_max_act`, `id_createur`) VALUES
(10, 'Plouf Plouf', '2026-06-25', 'Piscine', 'Plongez avec vos toutous !', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ47coo6_M_1HhEQ4galypQiJCoRTIXPTXk6ozfEtN0tQ&s=10', 2, 1),
(11, 'Course en folie', '2026-06-30', 'Le gazon', 'Participez à une course dejantée', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgKh5OxXQYZYvZA9a-j3tO858WvmIusLZ7WQVwUilxig&s=10', 5, 1),
(13, 'Balade de vache', '2026-07-28', 'Prairie', 'Profitez d\'une belle météo et accompagnez votre boviné favoris', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLn6snN_htl6fGZ9FnVy-pTXS4ZH2SrUilUQ&s', 3, 2),
(14, 'Exploration sous marine', '2026-07-09', 'Sous l\'océan', 'Découvrez un nouveau monde dans leau', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT52WgarDuLp2XsG6S6QbN3dAuB5svRJZulDQ&s', 5, 2),
(15, 'karaoke avec krikri', '2026-07-04', 'Chez krikri', 'Affrontez moi et ma super voix', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREOX0cBiYyq-vBoi8FzrO4W87lDn1Z2gozvQ&s', 2, 3),
(16, 'Concours de la meilleure boule de poils', '2026-08-11', 'Le salon', 'La boule la plus ronde remporte une tonne de croquette', 'https://i.pinimg.com/736x/4f/13/ff/4f13ff4a0e559a5c735c082648c167f8.jpg', 4, 4),
(17, 'Epilation d\'un kiwi', '2026-07-08', 'Dans le cuisine', 'Testez votre patience et votre agilité autour d\'un kiwi', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCLltp6lfuvk8aq_i710eFOCay-j1FOLMmnA&s', 5, 4),
(18, 'Chasse au lutin magique', '2026-08-20', 'For for lointain', 'Chevauchez votre licorne préférée et partez en quête de la légende du lutin magique', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQO5YbJDp--22XCjIUtiRePD1lvKQnEosFTmQ&s', 4, 4),
(19, 'A vos marques, prêts, PARTEZ !', '2026-07-12', 'au stade', 'Prenez vos baskets, on va chauffer les mollets', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRhNxLDhyCN2k5pSrt2eV0svFn9-yTcIj0sQ&s', 5, 5),
(20, 'Glissade avec les loutres', '2026-08-29', 'WaterPark', 'Amusez vous dans un parc aquatique de loutre', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvaGyXqsGo0GQ3ghUmoPkdAGtdma7n9L4Trg&s', 2, 5);

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
(10, 1, 1),
(11, 1, 2),
(13, 2, 4),
(14, 2, 3),
(15, 3, 6),
(16, 4, 7),
(17, 4, 8),
(18, 4, 9),
(19, 5, 11),
(20, 5, 12);

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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `animal`
--

INSERT INTO `animal` (`id_animal`, `nom_animal`, `age_animal`, `type_animal`, `url_image_animal`, `description_animal`, `id_user`, `danger`) VALUES
(1, 'Julien', 5, 'Chien', 'https://media.licdn.com/dms/image/v2/D4E03AQEW-WqPYIMsrw/profile-displayphoto-shrink_800_800/B4EZUk8udkG0Ac-/0/1740081654140?e=1783555200&v=beta&t=wHjllaFs5JuPokLFge7KGMXkW2pt7XZU8h475Dgwnuo', 'Vie que la nuit\r\nSuper dangereux\r\nDans les montagnes et les forêts\r\nMange les mouches', 1, 3),
(2, 'Benoit', 22, 'Escargot', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkfv7KWseBDNzxqM1D5dpLYkkmw3r9DCsGs2Ulwlf11g&s=10', 'Un escargot un peu baveu mais très touchant <3', 1, 5),
(3, 'Agathe', 23, 'Limace', 'https://bbfreesing.s3.ap-southeast-1.amazonaws.com/wp-content/uploads/2018/07/19113931/images_Blog_F5UE959HMMF6ZJ0.LARGE_.jpg', 'Une limace toute belle plus belle que toi', 2, 4),
(4, 'Chloé', 21, 'Vache', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZHBmEdOrgbKEqm62FEjjWoGC4Kvc8GQr3Dg&s', 'Une vache trop cute qui vous tiens compagnie', 2, 1),
(5, 'Léna', 21, 'chien', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNK2Oi1znAlLXhR_h8PcjHlPqNEJpRlKX-Fw&s', 'Une saucisse, nan un chien ? oh je sais plus', 2, 2),
(6, 'Krikri d\'amour', 500, 'Blob Fish', 'https://aussieanimals.com/wp-content/uploads/2025/07/mr-blobby-psychrolutes-microporos-profile.jpg', 'Un peu gluant mais sympa', 3, 1),
(7, 'Lucille', 21, 'Chat', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbXAK_QdT7qZbk9-MWubG_dmDzV7UDCVYcQw&s', 'attention, peut voler votre nourriture quand vous avez le dos tourné', 4, 3),
(8, 'Steve', 45, 'Poisson', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTA13K36G1Z75uoB_elctHTpsqWlTEopdEj7g&s', 'Steve - le- POiAaAaaAAh, le poisson Steve', 4, 1),
(9, 'Jade', 500000, 'Licorne', 'https://lh4.googleusercontent.com/proxy/MW2Qk8rBwseqOo6cOY_N1z_qfjALAlYVyDTQXOthq6zEbX2wfe9Cl0Yu7xVo5JrYBCUwmaAHLT-ZHp7bZMdQVI_lqPNC5SiW-_Q', 'Rarement aperçu, mais la légende raconte qu\'on la trouverait s\'abreuver à un lac en arc en ciel et en paillettes', 4, 2),
(10, 'Elea', 10, 'Corneille', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSi4ueSVnQHns4W1EETvw-B_tJWM23n_X2row&s', 'Oiseau edgy qui aime l\'ombre et le musique emo', 4, 2),
(11, 'Matthieu', 22, 'Hérisson', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpkDOm7n90kOSeMqrDDQiKT98vGnHbd9peZQ&s', 'Impressionnant de part sa vitesse incroyable', 5, 1),
(12, 'Alex B.', 20, 'Loutre', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjFSCH6oeZbne4QhV3Rkdm5nbDt0cCt0hDag&s', 'Vraiment trop mignon', 5, 5),
(13, 'Romane J.', 21, 'Renard', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHJvFcBRJ8bVWMJh0zoXTJ6xhLq2291Q9YLw&s', 'Peut vous voler un fromage si vous êtes pas attentif (ou si vous êtes un corbeau)', 5, 4);

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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `commentaire`
--

INSERT INTO `commentaire` (`id_commentaire`, `commentaire`, `note`, `id_user`, `id_animal`) VALUES
(1, 'Chien très dangereux', 3, 1, 1),
(3, '', 5, 4, 3),
(4, 'adorable', 4, 2, 12),
(5, 'ouaf', 5, 2, 1),
(6, 'super rapide', 5, 2, 2),
(7, 'incroyable', 5, 2, 3),
(8, 'gluant', 2, 2, 6);

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `prenom_user` varchar(30) NOT NULL,
  `nom_user` varchar(30) NOT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id_user`, `username`, `password`, `prenom_user`, `nom_user`) VALUES
(1, 'admin', 'scrypt:32768:8:1$jOURFZNsflJZ4VvW$b9bb94ecb3c348ef1d60da0ae1d97650717bfccac15601156939df25b362b5f8c34697962208ae71d81c814b22e8447724652f7e89eea57bcbd2221eae16fe8f\n', 'AgaClocloLuci', 'Admin'),
(2, 'Lucli', 'scrypt:32768:8:1$3DVumkUxNTAw4i5l$a45f107564aa575fe2014c80956d460fde82b4b1c060cbc9b6fa83d64b853b0bb88d50435203153b7d0f369fad806021e76af1d726bec2d50c1a686f074fe45b', 'Lucille', 'azerty'),
(3, 'Krikri_lover', 'scrypt:32768:8:1$JsMIM5DweZLPSgnF$f4be3b3c0ad2d5512040813039b9577cfe10291955d2161cd0e5de605b8f660cbaf6140bd7806796304b0556e000af174ff16999a4c3461cb65660606e5f7aaf', 'Krikri', 'D\'amour'),
(4, 'fan_des_animaux', 'scrypt:32768:8:1$N1dAspTFjNZD65CS$15774723eb50519bf56dcbc4629bcfec0bcc181292f12eb56699df8f86690ce56d1e2e975e68a0beeaa4db8c71c7897494d2d8d841617c9884a3d05a2a9fe551', 'Patrick', 'Animal'),
(5, 'marco', 'scrypt:32768:8:1$PCU4wzDoQh3iHcM3$02eaf60625ef2626fdd76a2778c5b723dd82715c65243661e87d8e38da8e77e0a5308498941cd571fc7650fda08729f3a751f5ba4bd27230327cca654c6a06d8', 'Marco', 'Polo');

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
  ADD CONSTRAINT `foreignkey_triades_act` FOREIGN KEY (`id_act`) REFERENCES `activites` (`id_act`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `foreignkey_triades_activites` FOREIGN KEY (`id_act`) REFERENCES `activites` (`id_act`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `foreignkey_triades_animal` FOREIGN KEY (`id_animal`) REFERENCES `animal` (`id_animal`) ON DELETE CASCADE ON UPDATE RESTRICT;

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
