CREATE DATABASE start_for_x;


CREATE TABLE `start_for_x`.`startup_tag` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `startup_name` VARCHAR(45) NULL,
  `tag` VARCHAR(128) NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `start_for_x`.`startup_news` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `startup_name` VARCHAR(45) NULL,
  `link` VARCHAR(1024) NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `start_for_x`.`employee` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_name` VARCHAR(64) NULL,
  `location` VARCHAR(256) NULL,
  `work_history` VARCHAR(4096) NULL,
  `startup_name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `start_for_x`.`startup_evaluation` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `startup_name` VARCHAR(45) NULL,
  `current_valuation` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `start_for_x`.`startup_funding` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `funding_date` DATETIME NULL,
  `event` VARCHAR(45) NULL,
  `amount_raised` VARCHAR(45) NULL,
  `investors` VARCHAR(2048) NULL,
  `startup_name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
