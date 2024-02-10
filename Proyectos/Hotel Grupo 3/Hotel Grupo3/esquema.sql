CREATE TABLE personas(
    persona_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    dni char(8) NOT NULL,
    numero_telefono VARCHAR(255) NOT NULL,
    nombres VARCHAR(50),
    apellidos VARCHAR(50),
    sexo char(1),
    fecha_ingreso date,
    fecha_salida date
);


Create table transaccion(
    id bigint unsigned not null auto_increment primary key,
    fecha_registro date not null,
    hora_registro time not null,
    tipo_transaccion char(1) not null,
    fecha_entrada date  not null,
    hora_entrada  time not null,
    fecha_salida date  not null,
    hora_salida  time not null,
    habitacion_id  int not null,
    persona_id  int not null
);


CREATE TABLE servicios(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL

);
Create table categoria_habitacion(
    id bigint auto_increment primary key,
    nombre varchar(30) not null,
    precio numeric(9,2)
);

CREATE TABLE Habitacion (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    estado_habitacion CHAR(1),
    descripcion VARCHAR(100) NOT NULL,
    categoria_id INT NOT NULL REFERENCES categoria_habitacion(id)
) AUTO_INCREMENT = 300;


CREATE TABLE detalle(
    servicios_id int PRIMARY KEY REFERENCES servicios(id),
    comprobante_id int not NULL REFERENCES comprobante(id),
    monto numeric(7,2) not null
);

CREATE TABLE comprobante(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo_comprobante char(1) not null,
    numero_comprobante varchar(50) not null,
    fecha_comprobante date not null,
    monto_total numeric(7,2) not null,
    transaccion_id int not null REFERENCES transaccion(id),
    persona_id int not null REFERENCES personas(persona_id)
);

CREATE TABLE detalle_servicios(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha_solicitud date NOT NULL,
    hora_solicitud time NOT NULL,
    descripcion_solicitud VARCHAR(100) NOT NULL,
    monto_servicio DECIMAL(9,2) NOT NULL,
    transaccion_id BIGINT UNSIGNED not null,
    servicio_id BIGINT UNSIGNED not null,
    foreign key(transaccion_id) references transaccion(id),
    foreign key(servicio_id) references servicios(id)
);

Create table detalle_alojamiento (
id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
transaccion_id int not null REFERENCES transaccion(id),
persona_id int not null REFERENCES personas(persona_id)
);

create table usuario(
id Bigint unsigned not null AUTO_INCREMENT primary key,
nomUsuario varchar(50) not null,
contraseña varchar(50) not null
);
