# Bienvenidos a los requerimientos necesarios (proyecto_BD_capybara)

*es necesario seguir estos pasos para que el proyecto funcione con normalidad e impedir algunos mal entendidos a la hora de realizar los respectivos cambios en las ramas que corresponden al proyecto inicial (mucho ojo con esto).*

## Instalación de el IDE base
> El IDE en donde se trabajará es [visual studio code](https://code.visualstudio.com/)

## Instalación de las herramientas principales (Frontend Devs):

>para los que trabajan solo en el frontend es necesario descargar la libreria de [Tailwind](https://tailwindcss.com/). *esta explicación se tendrá que estudiar para implementar más pasos.*

### zona de trabajo para el rol frontend:

![zona de trabajo](/app/static/img/Captura%20de%20pantalla%202025-10-07%20103716.png)

## Intalacion de las herramientas principales (Backend devs):

**Se necesita la intalacion de las siguientes herramientas:**

> El lenguaje de programación que se usará en este proyecto es [Python](https://www.python.org/) (**version:** 3.12.4 o superior).

Despues de haber instalado las herramientas principales es necesario crear una entorno virtual o embebido para no contaminar el entorno global de librerias que no se usaran para los proyectos que utilices.

> Es necesario hubicarse en la carpeta principal del proyecto para realizar el proceso de virtualización y seguidamente abrir la consola, la carpeta que contendrá esta función simpre se llamará `.venv` en todas las instancias del proyecto.

```
python -m venv .venv
```
> Estas son las principales formas para activar nuestro entorno virtula, **es importante activarlo antes de instalar las librerias**.

**comando para activar el entorno virtual:**
```
.venv/Scripts/activate
```

**comando para desactivar el entorno virtual:**
> Esto solo cuando termines de trabajar en el proyecto, **por lo que siempre tienes que tener activo el entono.**

```
deactivate
```

*es importante esperar un tiempo para que se cargue toda la logica y scripts necesarios del entorno virtual.*


> los requerimientos se encuentran en el archivo `requirements.txt` ya que aquí se encuentran las dependencias de las librerias de Flask, ante mando a esta indicación tienes que abrir la consola de tu VSC (visual studio code). 

```
pip install -r requirements.txt
```
si presenta problemas al realizar el procedimiento anterio, por favor, cambie el entorno en donde esta compilando el proyecto con la conjugada de las teclas **Ctrl + shift + P** y le saldrá lo siguiente captura:

![zona de interprete](app/static/img/Captura%20de%20pantalla%202025-10-15%20071810.png)

En este caso deberas de escoger la opcion **Select Interpreter** para cambiar el compilador del proyecto encargado como aparecer en la siguiente captura:

![zona del compilador](app/static/img/Captura%20de%20pantalla%202025-10-15%20072433.png)

> porfavor, es necesario comprobar si existe un punto embebido en el proyecto aplicando los pasos anteriormente mensionados.

**Iniciar servidor del entorno virtual**

para prender el servidor del entorno virual escribe en el terminal

```
python wsgi.py
```

**Iniciar la base de datos**

Crea en la raiz del proyecto un archivo .env que contenga

```
DATABASE_URL=mysql+pymysql://root:@localhost/capybara_db
```

Crea tu base de datos en el workbench con el nombre correspondiente `capybara_db` recuerda usar:

 ```
create database capybara_db;
```
luego en la terminal escribe

```
flask db upgrade
```

Esto añadira las tablas a tu base de datos

