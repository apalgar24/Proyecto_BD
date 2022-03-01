mysql -u root -p
create database proyecto;
GRANT ALL PRIVILEGES ON proyecto TO 'proyectobd'@'localhost'
IDENTIFIED BY 'proyectobd' WITH GRANT OPTION;


CREATE TABLE campeon (
    id varchar(15),
    name varchar(20),
    fecha_creacion date,
    title varchar(45),
    clase varchar(15),
    constraint pk_campeon PRIMARY KEY(id)
);

INSERT INTO campeon values ('aatrox','Aatrox','2018-03-24','the darkin blade','fighther');
INSERT INTO campeon values ('reksai','Rek Sai','2015-11-11','the void Burrower','fighther');
INSERT INTO campeon values ('sivir','Sivir','2021-2-5','the battle mistress','marksman');


CREATE TABLE estadistica(
    id varchar(15),
    codigo numeric(3),
    vida numeric(3),
    velocidad numeric(4),
    armadura numeric(3),
    daño numeric(4),
    CONSTRAINT pk_estadistica PRIMARY KEY(codigo),
    CONSTRAINT fk_campeon FOREIGN KEY(id) REFERENCES campeon(id) 
);

INSERT INTO estadistica values ('aatrox',1,580,345,38,60);
INSERT INTO estadistica values ('reksai',2,570,335,36,64);
INSERT INTO estadistica values ('sivir','3',562,335,26,63);


