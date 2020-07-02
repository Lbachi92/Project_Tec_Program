CREATE DATABASE cadastros;

CREATE TABLE geositio(
	id serial not NULL,
	data TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP,
	nome VARCHAR(100) not NULL,
	sitio VARCHAR(100) not NULL,
	lat VARCHAR(100) not NULL,
	longi VARCHAR(100) not NULL,
	descri VARCHAR(250) not NULL
	);