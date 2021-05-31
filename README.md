# Ambiente de desarrollo

Ejecuta el back con los siguiente comandos:

## crear ambiente virtual
`virtualenv env/`

## activar
`source env/bin/activate`

## instalar
`pip install -r requirements.txt`

## crear base de datos
`python manage.py migrate`

## correr la aplicación
`cd src/`
`python manage.py runserver`

# TODO
## REQUERIMENTO 1.1: Desarrolla la interfaz usando vue que permita crear un usuario con la siguiente información:
- user
- password
- email
- first_name
- last_name

## Solucion 1.1: 

## 1.2) Valida que "email" sea un correo electrónico válido

# en el back
## 2.1) crear un usuario con la siguiente información:
## Requirement OK
- user
- email
- first_name
- last_name

## 2.2) usa el método create_user disponible en views.py: create_user, para guardar un nuevo usuario en la base de datos y regresa la información ingresada más el pk:

## Requirement OK
- pk
- user
- password
- email
- first_name
- last_name

## 2.3) si el usuario ya existe regresa el usuario existente

## Notas:
- Usa python3
- Puedes usar librerías adicionales
- Para algunos bonus es posible que tengas que cambiar la configuración en settings.py

## Bonus points:
### Dominating:

## Requirement OK
- Implementa un método GET para obtener el usuario a través de un id. (no es necesario validar que existe).

### Rampage:
## Requirement OK
- Valida el método GET.
- Retorna un código de error HTTP 204 en caso de que no exista el usuario.

### Killing Spree:
## Requirement OK
- Usa django rest framework para crear los views y regresar una respuesta.
- Usa "users/" como url para estas nueva(s) vista(s).
- No sobreescribas y/o elimines la información.

### Monster kill
## Requirement OK
- Recibe y devuelve la información en formato JSON
- Envía la información con encabezado Content-Type: application/json

### Unstoppable
## Requirement OK
- Usa uno o más serializadores para validar la información.

### Ultra kill
## Requirement OK
- Recibe y devuelve la información en camelCase. Por ejemplo: "firstName" en vez de "first_name"

### Godlike
- Autentica usando JWT

### Wicked sick
- Restringe POST usando permisos.

### Holy Moly Wacamoly!

- Sube los cambios realizados como pull request.

