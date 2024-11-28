create database biblioteca;
use biblioteca;
drop table usuario;
create table usuario(id_usuario int auto_increment primary key , nome varchar(30), cpf varchar(50), telefone int, email varchar(100), senha varchar(100));
create table admins(id_admin int primary key);
select * from usuario;