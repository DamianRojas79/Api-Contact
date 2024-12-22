## API  Contacts

![image alt](https://github.com/DamianRojas79/Api-Contact/blob/main/images-git/api-contact.png)

  
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)![Static Badge](https://img.shields.io/badge/Date_Release-Junio-orange)![Static Badge](https://img.shields.io/badge/API_Contact-%20V1.0.0-blue)

  

## Índice

  

*[Título e imagen de portada](#Título-e-imagen-de-portada)

  

*[Insignias](#insignias)

  

*[Índice]()

  

*[Descripción del proyecto](#descripción-del-proyecto)

  

*[Estado del proyecto](#estado-del-proyecto)

  

*[Características de la aplicación y demostración](#características-de-la-aplicación-y-demostración)

  

*[Acceso al proyecto](#acceso-al-proyecto)

  

*[Tecnologías utilizadas](https://github.com/DamianRojas79/ToDo-List/edit/main/README.md#tecnolog%C3%ADas-utilizadas-heavy_check_mark)

  

*[Personas desarrolladores del proyecto](#personas-desarrolladoras-del-proyecto)

  

*[Licencia](licencia-)

  

*[Conclusión](#conclusión)

  

## Descripción del Proyecto

  

Api contact es una Api Rest creada con Flask donde se crea una base de contactos la cual se puede acceder mediante las solicitudes HTTP. <br><br>

  


  

  

## Estado del Proyecto

  

![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)

  
  

## Características de la aplicación y demostración

  

  

:hammer: **Funcionalidades del proyecto**

  

- #### **`Funcionalidad 1`:** **Solicitudes HTTP (CRUD)** <br>

Con alguna herramienta como por ejemplo Postman se se realizan las solicitudes HTTP para ejecutar las operaciones estándar de la base de datos contactos (select, insert, update y delete )
<br>

**GET** <br>
Listar los contactos.<br>
URL: http://localhost:5000/contacts<br>
![image alt](https://github.com/DamianRojas79/Api-Contact/blob/main/images-git/get-api.png)


**POST** <br>
Crear un contacto.<br>
URL: http://localhost:5000/contacts<br>
Para el Post en el Json se debe enviar el "name", "email" y "phone" del contacto.<br>

![image alt](https://github.com/DamianRojas79/Api-Contact/blob/main/images-git/post-api.png)

**PUT** <br>
Modificar un contacto.<br>
URL: http://localhost:5000/contacts/id-contacto <br>
Para el Put se envia en la URL el id del contacto a modificar y en el Json el dato que se desea modificar.<br>
![image alt](https://github.com/DamianRojas79/Api-Contact/blob/main/images-git/put-api.png)

**DELETE** <br>
Eliminar un contacto.<br>
URL: http://localhost:5000/contacts/id-contacto<br>
Para el Delete se envia en la URL el id del contacto que se desea eliminar.<br>

![image alt](https://github.com/DamianRojas79/Api-Contact/blob/main/images-git/delete-api.png)


    

- #### **`Funcionalidad 2`**: **Subir contactos desde archivo CSV**<br>

  

Además de crear contactos mediante POST tambien es posible hacerlo a traves de un archivo CSV que se puede cargar al sistema. Para ello se debe crear un archivo csv en la carpeta "csv" con las columnas "name","mail" y "phone". De esta manera se pueden crear una lista de contactos.

Para poder crear los contactos desde el csv se debe ejecutar en la terminal:<br>
<i>python3 create_contacts_csv.py </i>

Imagen del directorio donde se debe cargar el archivo contacts.csv para crearlos
![image alt](https://github.com/DamianRojas79/Api-Contact/blob/main/images-git/crear_csv.png)

Luego de haber ejecutado el comando si el csv se genero correctamente se muestra el  siguiente mensaje mensaje: <br>

**"Contacts created successfully"**

  
  

  

## Acceso al Proyecto

  

  

Para descargar y ejecutar el proyecto se debe realizar los siguientes pasos:

  

  

:file_folder: **Acceso al proyecto**

  

- **Abrir terminal**<br>

  

Primero se debe abrir una terminal para ejecutar los comandos necesarios para descargar y ejecutar el proyecto.

  

  

- **Crear directorio para el proyecto**<br>

  

<ins>Ejecutar</ins>:<br>

  

<i>mkdir proyecto-api-contact</i>

  

  

- **Clonar repositorio**<br>

  

Para clonar el repositorio primero situarse en el directorio creado:<br>

  

<ins>Ejecutar</ins>:<br>

  

<i>cd proyecto-api-contact </i><br>

  

Luego allí clonar el repositorio:<br>

  

<ins>Ejecutar</ins>:<br>

  

<i>git clone git@github.com:DamianRojas79/Api-Contact.git </i>

  
  
  

  

:hammer_and_wrench: **Abre y ejecuta el programa**

  

- **Instalar python y modulo venv para crear entornos virtuales si no lo tienes instalado**<br>

  

Para instalar Pyhton

  

<ins>Ejecutar</ins>:<br>

  

<i>sudo apt install python3</i> <br>

  

  

Para instalar venv

  

<ins>Ejecutar</ins>:<br>

  

<i>sudo apt install -y python3-venv</i><br>

  

  

- **Crear entorno virtual para el proyecto**<br>

  

Se crea un entorno virtual para tener allí todos los paquetes necesarios para el proyecto.<br>

  

Para ello primero se debe entrar al directorio clonado.<br>

  

<ins>Ejecutar</ins>:<br>

  

<i>cd proyecto-api-contact </i>

  

  

Luego se crea el entorno virtual:

  

<ins>Ejecutar</ins>:<br>

  

<i>python -m venv env-api</i>

  

  

- **Activar entorno virtual**

  

<ins>Ejecutar</ins>:<br>

  

<i>source env-api/bin/activate</i>

  

  

- **Instalar las dependencias para el proyecto** <br>

  

Se instalan las as dependencias necesarias que se encuentra dentro del archivo requirements.txt.<br>

  

<ins>Ejecutar</ins>:<br>

  

<i>pip install -r requirements.txt</i>

  

  

- **Ejecutar el programa**

  

<ins>Ejecutar</ins>:<br>

  

<i>Python3 app.py</i>

  

  

- **Abrir aplicación en el navegador**<br>

  

En el navegador que desee ingresar la siguiente URL para abrir la aplicación:<br>

  

http://localhost:5000/

  

  

## Tecnologías Utilizadas :heavy_check_mark:

  

- **Flask**<br>

  

- **Flask-SQLAlchemy**<br>

  

- **Sqlite**<br>

  

- **JSON**<br>

  

## Personas Desarrolladoras del Proyecto

  

[<img src="https://avatars.githubusercontent.com/u/135189204?s=400&u=932907d7db09c6472e34c43c6b5ed27be7342bf4&v=4" width=115><br><sub> Damian Rojas </sub>](https://github.com/DamianRojas79)

  

## Licencia 📄

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

  

Este proyecto cuenta con licencia conforme a los términos de la licencia MIT.

## Conclusión

En este proyecto lo que se intenta demostrar es como hacer una Api Rest utilizando Flask y como mediante esta  poder acceder a las diferentes operaciones que se pueden realizar a una base de datos implementando los verbos del protocolo http.


