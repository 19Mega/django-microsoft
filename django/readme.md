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
- python manage.py showmigrations
- python manage.py runserver

Agregar datos a la base de datos:
- python manage.py shell (ejecutar para empezar en entorno database)
- from dog_shelters.models import Shelter, Dog (se importa los modelos a agregar)

(ADD) Creamos un nuevo shelter (refugio), como crear un nuevo objeto.
- shelter = Shelter(name="Demo shelter", location="Seattle, WA")
- shelter.save()

(UPDATE)
- shelter.location = "Redmond, WA"
- shelter.save()

(ADD) Creamos dogs.
- Dog(name="Sammy", description="Cute black and white dog", shelter=shelter).save()
- Dog(name="Roscoe", description="Lab mix", shelter=shelter).save()

(GET)
- shelter.dog_set.all()
- Dog.objects.get(pk=1)  >> Trae el id 1, o sea primary key.
- Dog.objects.filter(shelter__name='Demo shelter')  >> Trae con filtro.


## Para models.py, tipo de datos:
CharField: una línea de texto única.
TextField: varias líneas de texto.
BooleanField: una opción booleana true/false.
DateField: una fecha.
TimeField: una hora.
DateTimeField: fecha y hora.
URLField: una dirección URL.
IntegerField: un número entero.
DecimalField: un número decimal de precisión fija.


## DEPLOY : 

Modo de depuración
Como desarrollador, quiere ver los mensajes de error que puede generar la aplicación. Sin embargo, esta información puede proporcionar a un atacante información sobre cómo se ejecuta la aplicación, lo que podría permitir el acceso no autorizado. Por lo tanto, en settings.py, establezca la opción DEBUG en False antes de implementar la aplicación en producción.

- Modo de depuración: False

Clave secreta
Para proteger la información confidencial, Django usa una clave secreta para firmar los valores que no se deben alterar. Durante el desarrollo, la clave secreta se almacena en texto no cifrado en settings.py. Cuando se implementa en producción, la clave secreta se debe leer desde una ubicación más segura, como Configuración de App de Azure o Azure Key Vault.

Hosts permitidos
El archivo settings.py contiene una lista de nombres del servidor denominada ALLOWED_HOSTS. Esta lista determina el lugar desde el que se puede ejecutar la aplicación. De manera predeterminada, la lista vacía permite que la aplicación se ejecute desde localhost. Actualice esta configuración antes de implementar en el host de producción.


Archivos estáticos
Los archivos estáticos son archivos que no forman parte del sistema de plantillas de Django. Normalmente, estos archivos incluyen archivos JavaScript o CSS. Pero también podrían incluir archivos HTML estáticos. En concreto, el sitio de administración utiliza archivos estáticos para el estilo y el formato.

Mientras la aplicación está en desarrollo, Django sirve automáticamente los archivos estáticos. En producción, debe configurar un servicio para que sirva cualquier archivo estático. Una solución común es una biblioteca WhiteNoise.

Durante el proceso de implementación, todos los archivos estáticos se recopilan en la ubicación que indica STATIC_ROOT en settings.py. Se recopilan mediante la ejecución de python manage.py collectstatic. Azure ejecuta este comando automáticamente, por lo que no es necesario ejecutarlo localmente antes de la implementación.

- python manage.py collectstatic


