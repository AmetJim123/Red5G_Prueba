API para registrar médicos y realizar el login, registrar pacientes, buscarlos todos, por id, editarlos
y eliminarlos de la base de datos. Lenguaje usado Python con framework Flask y DB PostgreSQL

Al clonar el repositorio hay que crear la carpeta "lib" y el archivo ".env"

En la carpeta "lib" Hay que crear el archivo "__init__.py" y "authorizer.py", el contenido 
del archivo authorizer se encuentra en el archivo coding.txt, donde también se encontrará
la información del archivo .env que irá a nivel de la carpeta src y env.

Para instalar la base de datos hay que abrir pgAdmin4 y en la sección que dice bases de datos
damos clic derecho en postgres y clicamos en la opción restaurar y buscamos el archivo
prueba_tecnica_backend.sql 

Una vez hecho todo esto, solo hay que ejecutar el archivo app.py y utilizar las diferentes rutas
junto con el puerto local.