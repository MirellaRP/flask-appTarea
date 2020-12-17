drop database db_poo;

create database db_poo;

use db_poo;

CREATE TABLE usuario (
  id int(3) NOT NULL primary key auto_increment,
  codigo varchar(10) NOT NULL,
  nombres varchar(50) NOT NULL,
  login varchar(20) NOT NULL,
  clave varchar(20) NOT NULL,
  tipo varchar(9) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

insert into usuario(codigo,nombres,login, clave , tipo)
values ('201620035','Mirella','mire','123456', 'Alumno');
