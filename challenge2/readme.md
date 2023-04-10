# Pasos
1. Instalar librerias
~~~
python -m pip install requests
~~~

2. Darle permisos a los archivos sh
chmod +x list_files.sh
chmod +x find.sh

3. Ejecutar create_queues.py ubicado en la carpeta server para crear las colas de request y de response
~~~
python3 create_queues.py
~~~
4. Crear un usuario con el MOM
5. Ir a config de la carpeta server y en USER poner el usuario generado
6. Ir a config de la carpeta api y en USER poner el usuario generado
7. Correr el archivo app.py de la carpeta server
~~~
python3 app.py
~~~
7. Correr el archivo app.py de la carpeta api
~~~
python3 app.py
~~~
8. Ya se puede consultar los servicios (list_files GET ) y (find_files POST body: "name":"file") 
