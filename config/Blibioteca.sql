create database biblioteca;
use biblioteca;
drop table usuario;
create table usuario(id_usuario int auto_increment primary key , nome varchar(100), cpf varchar(50), telefone varchar(100), email varchar(100), senha varchar(100));
insert into usuario(nome, cpf, telefone, email, senha) values ( "Bah", "beh", "67993067555", "yipe@gmail.com", "pass");
create table admins(id_admin int primary key);
select * from usuario;

create table emprestimo(cod_livro int, email varchar(100));

drop table livro;
create table livro( titulo varchar(100), autor varchar(100), genero varchar(100), isbn varchar(50), status set("DISPONÍVEL","EMPRESTADO"));

select * from livro;