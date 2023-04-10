# Info de la materia: ST0263 Tópicos especiales en Telemática
#
# Estudiantes:
### Julian Andres Ramirez Jimenez, jaramirezj@eafit.edu.co
### Samuel David Villegas Bedoya, sdvillegab@eafit.edu.co
### Julian Giraldo Perez, jgiraldop@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#

# MOM Server con Replicación y Tolerancia a fallos
#

# 1. Descripción del proyecto

En este proyecto se llevó a cabo el desarrollo de un Message-Oriented Middleware, que corresponde a un middleware para el intercambio de mensajes de manera asíncrona entre un conjunto de clientes o servidores. Para lograr esto, utilizamos el lenguaje de programación Python y nos enfocamos en la replicación de los datos para garantizar que ante cualquier fallo del servidor podamos garantizar la restauración de los datolisas, lo que hace a nuestro sistema tolerante a fallos. De esta manera, los mensajes intercambiados por los clientes se almacenan primero en memoria para poder realizar un rapido intercambio cuando alguno de los clientes los solicite  y posteriormente se almacenan en una base de datos y se pueden recuperar en caso de que el servidor falle.

Además, creamos un cliente que le permite a los usuarios del MOM utilizar las funcionalidades con un buen nivel de abstracción. Este cliente
hace peticiones a una API que desarrollamos, la cual se comunica con el Message-Oriented Middleware a través de comunicación por gRPC. 
Esto permite una comunicación rápida y eficiente entre el cliente, la API, y el MOM. Y además facilita la integración de otros servicios en el servidor. 
En resumen, nuestro Message-Oriented Middleware es una solución escalable y confiable para la comunicación entre nodos distribuidos en una red, que puede ser utilizado para diversas aplicaciones y plataformas.


## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

 Los aspectos propuestos por el profesor inicialmente eran construir el MOM teniendo en cuenta ciertos criterios como enfocarse en replicación 
 o particionamiento, tener muy en cuenta la tolerancia a fallos y algunas funcionalidades especificas relacionadas con los tópicos y las colas en el MOM
 como lo son crear, listar, eliminar, suscribirse, publicar mensajes y consumir mensajes. Además otro requisito era desplegar el proyecto
 en AWS con algo similar a lo hecho en el reto 2.
 
 En nuestro caso cumplimos con todos los items requeridos por el profesor enfocando nuestra solución especialmente en la tolerancia a fallos
 y la replicación. Implementando una solución final con lo hecho en el reto 2.
 
## 2. Información general de diseño de alto nivel y arquitectura

 ### Vista general de la arquitectura del proyecto
 
 ![Architecture](https://user-images.githubusercontent.com/57159295/230795312-ea09ba6e-e1b3-461d-adcd-15b3b16eeb50.png)
 
 Como se puede ver en la imagen, la arquitectura del proyecto se compone de 3 partes especialmente. Que son un cliente, una API, y el
 propio core del MOM que incluye la base de datos. El cliente y la API actuan como intermediaros proporcionando una capa de abstracción y
 haciendo nuestra solución más escalable a futuro. EN cuanto a la API esta se desarrolló siguiendo un modelo MVC.
 En nuestro proyecto el cliente y la API se a comunicacan por REST y entre la API y el MOM se establece la comunicación por gRPC.
 
 En cuanto al propio core del MOM este se desarrolló teniendo en cuenta que los mensajes y demás información se manejarian inicialemente en 
 memoria pero también garantizando que estos persistan y que se puedan restuarar  en caso de un fallo en el servidor.
 
 A continuación se presentan un par de diagramas que sirven para ilustrar la arquitectura interna del MOM.
 
 ##### Modelo de base de datos

 ![Proyecto1_db](https://user-images.githubusercontent.com/57159295/229974138-fe289a0f-78e0-46d3-8e83-cc8229abf4a2.png)

 ##### Diagrama de clases

 file:///home/julianramirezj/Downloads/Untitled%20Diagram.drawio.png![image](https://user-images.githubusercontent.com/57159295/230107761-0fb433cf-9666-4e9d-bae9-33018cd7fa79.png)

   

# 3. Descripción del ambiente de desarrollo y técnico

   - Para desarrollar el proyecto se utilizó principamennte el lenguaje de programación python en su versión 3.10.6. En este lenguaje se programó tanto el cliente          como la API y el mismo MOM.
   - También se uso C++ en los archivo .proto para definir la estructura de la comunicación en gRPC.
   - Para desarrollar el API se utilizó el micro Framework Flask como servidor, implementando en este los endpoints de la API.
   - En cuanto a base de datos se utilizó MySQL.
   - Para lograr hacer la comunicación con gRPC se utilizó la libreria 'grpcio',en su  versión 1.37.1 con la utilidad 'grpcio-tools'. 
   - Para el correcto funcionamiento de grpc en cuanto a la concuerrencia se utilizó la libreria 'futures'.
   - Para la conexión con la base de datos se utilizó la libreria mysql-connector de python.
   - Se hace uso de la libreria 'os' para obtener la lista de archivos del directorio seleccionado.
   - Se hizo uso de la libreria 'json' para poner los mensajes que retornan los microservicios en formato json.
   - Se utilizó la libreria 'sys' para manejar las importaciones en ciertos directorios.


## Como se compila y ejecuta.

#### Instalación
 Antes de ejecutar el proyecto hay que tener en cuenta que se deben instalar las siguientes cosas:
                  
           MySQL DB:
                     sudo apt-get update
                     sudo apt-get install mysql-server
                     sudo systemctl start mysql
           Python:
                     sudo apt install python3
                     sudo apt install python3-pip
                     pip install mysql-connector-python
                     pip install grpcio
                     pip install flask
                    
 #### Configuración
 
  Como primer paso en la configuaración del entorno está correr las migraciones, para esto se debe configurar el archivo config.py
    según los requerimientos, inicialmente la base de datos está configurada para trabajar en local para el MOM, pero si es de su preferencia
    también podría estar en otro servidor. Para correr las migraciones debe estar instalado previamente mysql y estar activado,
    luego posicionese en la carpeta /migrations debe dar permisos a un archivo bash y ejecutarlo:
    
                    cmod a+x run-migrations.sh
                    ./run-migrations.sh
                    
  Luego de que tenga las migraciones listas puede proceder a lanzar el MOM server, para esto posicionese en la carapeta /mom
    y ejecute:
    
                  python3 server.py
             
   A continuación puede proceder a levantar la API, para esto pocisionse en la carpeta api y ejecute:
    
                  python3 api.py
                  
   En este punto ya tenemos el MOM funcionado por completo y el resto de cosas ya estarian más relacionadas con los clientes
     o usuarios finales del proyecto. Esto se explicará más a detalle en la descripción del ambiente de ejecución
     


## Detalles del desarrollo

El desarrollo se hizo de una manera ágil, en donde cada dia en una reunión se asignaban ciertas tareas a realizar por los integrantes
del grupo y estos las desarrollaban duurante el dia. Esta froma de trabajo agilizó, mejoró la comunicación y nos permitió avanzar muy rapido 
en el proyecto logrando hacer un producto funcional en alrededor de 1 semana. Cada integrante se especializó en una capa del proyecto, por ejemplo
Julian Ramirez estuvo especialmente enfocado en la base de datos y el cliente, Julian Giraldo en la API y el manejo de los datos en memoria del MOM y
Samuel Villegas en la integración de todos los componentes y la comunicación entre ellos.
A pesar de esta especialización, todos los integrantes participaron activamente en el desarrollo de cada una de las capas y contribuyeron al excelente resultado 
que se obtuvo al final con el proyecto.


## Detalles técnicos



## Descripción y como se configura los parámetros del proyecto

Para configurar los parametros con los que se va a ejecutar el proyecto se tiene un archivo de configuración por cada nodo en el proyecto que
recibe o envia datos. Por ejemplo en la api se tiene una carpeta /config se tienen varios archivos, entre ellos está connection_grpc.py donde se  puso la
configuración del host y el puerto para comunicarse con grpc en el MOM. De igual forma en el mom se tiene un archivo de configuración llamado 
config_mom.py donde se define el puerto para la comunación grpc. De igual forma tanto para las migraciones como para los modelos que a traves de una
abstracción permiten la comunicación con la base de datos se establecen archivos de configuración que establecen los parametros de conexión a la
base de datos.
Además de todo lo anteriormente mencionado lo que mejor permite establecer los parametros de conexión es el cliente, ya que es el mismo
usuario que está invocado las funcionalidades de nuestro MOM que dice donde está el host y el port de la API. De la siguiente manera:
                  
                    conn = ChasquiConnector('localhost','5000')


## ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO
## 

![image](https://user-images.githubusercontent.com/57159295/230796759-e3206c26-5b2e-41fb-9a1b-c5ff9e33f00a.png)
![image](https://user-images.githubusercontent.com/57159295/230796786-43afa71e-a048-4d25-9e7a-6a349c52364e.png)
![image](https://user-images.githubusercontent.com/57159295/230796803-b8cd0dd1-9739-4b70-a54a-4f2e71e4f1c3.png)

En las imagenes anteriores se puede ver como está organizado el codigo del proyecto. Como carpetas principales tenemos api, client y mom. 
Para el MOM son importantes las funcionalidades que proveen los directorios migrations y models, ya que estos le permiten realizar todo lo relacionado
con la base de datos. Además como archivo principal en esta capa tenemos server.py  que es el que permite lanzar el MOM e inicializar las funcionalidades que
este tiene.

En cuanto a la API, podemos ver claramente que la estructura de directorios obedece a un Model-View Controller, donde las rutas contienen los endpoints. Para
lanzar la API se usa el archivo api.py.

En cuanto al cliente este consta simplemente de un archivo y simplemente basta con que un usuario final ponga este archivo en el directorio donde hará uso
de nuestro MOM.

## Resultados o pantallazos (En desarrollo)


# 4. Descripción del ambiente de EJECUCIÓN (en producción)

# IP o nombres de dominio en nube o en la máquina servidor.

El proyecto fue desplegado con AWS, la maquina que contiene el proyecto expone la api con la ip y puerto 34.203.88.198:5000


## Como se lanza el servidor.
    
En caso de querer lanzar su propio servidor con la aplicacion tendra dos opciones las cuales se mostraran a continuacion.

### Monolitico

Crear la instancia para el despliegue, y una vez creada clonar este respositorio.

Posterior a esto tendra que correr las migraciones siguiendo las instrucciones ubicadas en la carpeta /migrations

Una vez tenga la base de datos montada debera correr la api y el mom, para esto corra el siguiente comando desde la carpeta fuente del repositorio
         ```
         python3 api/api.py & python3 mom/server.py
         ```
 
NOTA: Asegurese de tener correctamente configurada la seguridad y puertos de la/las instancias
 
### Distribuido

Para este despliegue se separaran la base de datos con el mom.

Primero cree dos instancias y clone el respoitorio en ambas.

Dentro de la instancia donde desea crear la base de datos tendra que correr las migraciones siguiendo las instrucciones ubicadas en la carpeta /migrations

Una vez se tenga la base de datos tendra que cambiar la configuracion de la misma 

Para esto configure el siguiente archivo y cambie el bind-adress a 0.0.0.0
```
 sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
 ```
Posteriormente tendra que crear un nuevo usuario para que nuestro otro servidor se conecte
```
 sudo mysql

 CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

 GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;

 CREATE USER 'username'@'%' IDENTIFIED BY 'password';

 GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' WITH GRANT OPTION;

 FLUSH PRIVILEGES;
 ```
 
Esto completaria nuestra configuracion de la instancia de base de datos
 
Ahora en la instancia del mom server tendra que ir a los archivos de configuracion dentro de /migrations y /models, ingresar el host adecuado de la base de datos y el usuario creado anteriormente.
 
Con esto estaria lista la configuracion del acercamiento distribuido

NOTA: Asegurese de tener correctamente configurada la seguridad y puertos de la/las instancias
   
## Guia de como un usuario utilizaría el software o la aplicación

Para un usuario final el uso de la aplicación se haria mediante Python, ya que en este lenguaje desarrollamos el cliente,
aún así se podria hacer uso desde cualquier otro lenguaje de programación, solo que de momento no se tendria una libreria que
implemente la abstracción que tenemos en python con lo que seria más complejo darle uso.

A continuación se presenta un codigo de ejemplo que sirve como guia para un usuario final.
( Hay que tener en cuenta que el archivo chasqui.py debe estar en el directorio )
        
        ```python
          from chasqui import ChasquiConnector     #Para importar teniendo el archivo chasqui.py en el mismo directorio
          
          def main():
             # Se crea la conexión, los parametros corresponden a donde esta corriendo la API
             conn = ChasquiConnector('localhost','5000') # Conectarse de esta forma crea un nuevo usuario
             conn = ChasquiConnector('localhost','5000', ''4jqa06l7yf') # De esta forma nos conectamos con un usuario existente
             
             # Para crear un uevo topico o cola pasamos el nombre 
             conn.create_topic('topico1')  # Pasamos como parametro el nombre
             conn.create_queue('queue1')
             
             # Para listar topicos o colas
             conn.list_topics()
             conn.list_queues()
             
             # Para eliminar topicos y colas
             conn.delete_topic('topico1')
             conn.delete_queue('queue1')
             
             # Para suscribirse a un topico o cola (Creado por otro usuario)
             conn.suscribe_topic('topico_prueba') # Pasamos como parametro el nombre
             conn.suscribe_queue('queue_test')
             
             # Para publicar mensajes en un topico o cola (Parametros: Nombre del topico, Mensaje)
             conn.publish_message_topic('topico1','Hola, este es un mensaje') 
             conn.publish_message_queue('queue1','Hola, este es un mensaje') 
             
             # Para consumir mensajes de un topico o cola (Parametros: Nombre del topico, Reintento activado)
             # Si el reintento activado es True, se espera hasta que haya un mensaje en la cola o el topico, y cuando se encuentre se 
             retorna. De lo contrario se pregunta si hay mensajes, si hay se obtienen y si no se deja de consumir.
             # Solo se consume un mensaje al tiempo.
             conn.consume_message_topic('topico_prueba') 
             conn.consume_message_topic('topico_prueba', True) 
             conn.consume_message_queue('queue_test') 
             conn.consume_message_queue('queue_test', True) 
             
        ```


## Resultados o pantallazos (En producción)
        
![image](https://user-images.githubusercontent.com/110442546/231009220-543d6586-fc3f-48a5-a867-e4c4ce2f7c97.png)
![image](https://user-images.githubusercontent.com/110442546/231009543-20f9a658-82b1-4ff2-a7b9-07250fab99e6.png)
![image](https://user-images.githubusercontent.com/110442546/231009611-c09f1f94-f21a-4fbb-95ff-c6fe7716a6dd.png)


# referencias:

## Código del profesor - Edwin Montoya
      https://github.com/st0263eafit/st0263-231/tree/main/Laboratorio-RPC
## Quickstart - Oficial Flask documentation
      https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application
## Quickstart - Oficial grpc documentation
      https://grpc.io/docs/languages/python/quickstart/

#### versión README.md -> 1.0 (2023-Marzo)



