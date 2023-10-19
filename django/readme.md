# Como ejecutar proyecto Django

## En powershell: 
- Crear entorno virtual:
python -m venv venv

- Activar entorno virtual:
venv\Scripts\activate

## En GitBash:
- Crear entorno virtual:
python -m venv venv

- Activar entorno virtual:
source venv/Scripts/activate


## Requeriments.txt
- Instalar todos los paquetes necesarios para que funcione la app en nuestro entorno virtual.
- Necestiamos entrar al entorno virtual antes de ejecutar este comando (venv).
pip install -r requirements.txt


## Proyectos frente a aplicaciones:
- Proyecto: 
    - Solo hay un proyecto.
    - Incluye la configuración o aplicaciones necesarias para un sitio web específico.
    - Los proyectos no se usan en otros proyectos.
- Aplicación:
    - Puede haber muchas aplicaciones en el proyecto único.
    - Es un componente del sitio web de mayor tamaño.
    - Las aplicaciones pueden usarse en varios proyectos.


Tal como se ha resaltado anteriormente, un proyecto de Django es el contenedor para todo el proyecto y cualquier aplicación que vayamos a crear. Vamos a crear nuestro proyecto. El punto final del comando es importante. Indica a django-admin que use la carpeta actual. Si deja fuera este punto final, se creará un subdirectorio adicional.

- gitBash: django-admin startproject helloproject .
    
La utilidad de la línea de comandos manage.py se crea en cada proyecto de Django. Tiene la misma función que django-admin. En el ejemplo siguiente se muestra cómo se podría usar si estuviera en la carpeta del proyecto y quisiera ver los subcomandos disponibles.

- gitBash: python manage.py help

▪ helloproject se considera como el paquete de Python para el proyecto.
▪ init.py es un archivo vacío que funciona para indicar a Python que este directorio se debe considerar como un paquete.
▪ settings.py incluye todos los valores o configuraciones.
▪ urls.py incluye las direcciones URL del proyecto.
▪ asgi.py y wsgi.py sirven como punto de entrada para los servidores web en función del tipo de servidor implementado.

### Iniciar servidor:
- gitBash: python manage.py runserver
### Terminar servidor:
- Control + C


## Creación de la aplicación Hola mundo

Hemos descubierto los aspectos básicos sobre el marco de Django y examinado la estructura de carpetas de nuestro proyecto. Ahora es el momento de crear nuestra primera aplicación. La aplicación ¡Hola mundo! permitirá comprender cómo se crean las aplicaciones y cómo funcionan al unísono con el proyecto de Django.

- gitBash: python manage.py startapp hello_world

- imagen1.png


- python manage.py createsuperuser
- python manage.py migrate
- python manage.py makemigrations
- python manage.py runserver