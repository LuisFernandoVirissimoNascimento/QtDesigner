create database biblioteca;
use biblioteca;
drop table usuario;
create table usuario(id_usuario int auto_increment primary key , nome varchar(30), cpf varchar(50), telefone int, email varchar(100));