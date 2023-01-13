# Proyecto de CRUD con python - flask - postgreSQL

### Descargar el repositorio y configuraciones
En la consola se escribe:
```sh
git clone https://github.com/ec4m/client-flask-postgres-CRUD.git
```
Posteriormente se entra en la carpeta del proyecto, se crea el entorno virtual y se activa:
```sh
python3 -m venv env
source env/bin/activate
```
Se instalan las dependencias del proyecto con:
```sh
pip3 install -r requirements.txt
```
### Creación de la base de datos
Se deben generar 3 tablas con el siguiente codigo SQL mediante postgreSQL:
#### client
```sql
CREATE TABLE IF NOT EXISTS public.client
(
    id character(36) COLLATE pg_catalog."default" NOT NULL,
    name character varying(50) COLLATE pg_catalog."default",
    lastname character varying(50) COLLATE pg_catalog."default",
    age smallint,
    CONSTRAINT client_pkey PRIMARY KEY (id)
)
```
#### usuario (esta en español por conveniencia)
```sql
CREATE TABLE IF NOT EXISTS public.usuario
(
    id character(36) COLLATE pg_catalog."default" NOT NULL,
    username character varying(50) COLLATE pg_catalog."default",
    name character varying(50) COLLATE pg_catalog."default",
    lastname character varying(50) COLLATE pg_catalog."default",
    password character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT user_pkey PRIMARY KEY (id)
)
```
#### product

```sql
CREATE TABLE IF NOT EXISTS public.product
(
    id character(36) COLLATE pg_catalog."default" NOT NULL,
    name character varying(50) COLLATE pg_catalog."default",
    description character varying(300) COLLATE pg_catalog."default",
    price integer,
    CONSTRAINT product_pkey PRIMARY KEY (id)
)
```

###Configuración de variables de entorno
Se debe crear un archivo .env para escribir las variables de entorno necesarias para la configuración del servidor y la conexión a la base de datos, se puede crear con el comando:
```sh
touch .env
```
O por medio de Vscode y se establecen las siguientes variables segun la cuenta de postgres a la que se vincule y el nombre de la database:
```
SECRET_KEY=CUALQUIER_PASSWORD
PGSQL_HOST=localhost
PGSQL_USER=usuario_postgres
PGSQL_PASSWORD=password_postgres
PGSQL_DATABASE=nombre_database
```

### Lanzamiento del servidor
Desde la consola se lanza el servidor por medio del comando:
```sh
python3 src/app.py
```

### Para consumir el servicio se usan las siguiente URLs:
#### Obtener todos los datos:
#### GET
```
http://localhost:3000/api/<name_table>/
```

#### Obtener un datos especifico:
#### GET
```
http://localhost:3000/api/<name_table>/<id_row>
```

#### Agreagar un los datos: 
#### POST
##### Enviar el elemento JSON
```
http://localhost:3000/api/<name_table>/add/
```

#### Eliminar un dato especifico
#### DELETE
```
http://localhost:3000/api/<name_table>/delete/<id_row>
```

#### Actualizar un dato especifico
#### PUT
```
http://localhost:3000/api/<name_table>/update/<id_row>