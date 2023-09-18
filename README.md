# TecnoWave - Plataforma de Blogs de Tecnología

TecnoWave es una plataforma web desarrollada en Django que permite a los usuarios registrados crear y compartir publicaciones sobre tecnología. La plataforma ofrece diversas funciones para mejorar la experiencia de usuario, como paginación, gestión de usuarios, likes, comentarios y perfiles de usuario.

Puedes ver un video de demostración en [este enlace]([https://www.loom.com/share/8c57401046304c359a57c7d9d6a2d35e?sid=364d5838-0fac-4e20-9977-a62439497861]).

## Funciones Principales

### 1. Paginación
La plataforma TecnoWave utiliza la paginación para mostrar una lista organizada de publicaciones, lo que facilita la navegación y la búsqueda de contenido.

### 2. Gestión de Usuarios
- Los usuarios no registrados no pueden realizar acciones como editar, borrar publicaciones o dar "likes".
- Los usuarios pueden registrarse en la plataforma para tener su propio perfil y acceder a todas las funciones.
- Ejemplo de usuario registrado: **Luis García**

### 3. Publicaciones
- Los usuarios registrados pueden crear sus propias publicaciones sobre tecnología.
- Cada publicación muestra detalles como el título, el autor y la fecha de creación.
- Los usuarios pueden ver un post individual para obtener más detalles.

### 4. Likes
- Los usuarios registrados pueden dar "likes" a las publicaciones que les gusten.

### 5. Comentarios
- Los usuarios registrados pueden comentar en las publicaciones, lo que permite una interacción más activa en la plataforma.

### 6. Perfiles de Usuario
- Los usuarios pueden crear y personalizar sus perfiles en TecnoWave, lo que les permite mostrar información sobre ellos mismos.

### 7. Cambio de Contraseña
- Los usuarios pueden cambiar su contraseña en cualquier momento.

### 8. Cerrar Sesión
- Los usuarios pueden cerrar sesión para proteger su cuenta en dispositivos compartidos.

### 9. Super Usuario
- Un super usuario tiene acceso especial y puede crear categorías.
- Las categorías permiten organizar el contenido, y los usuarios pueden explorar publicaciones por categoría.
- Si no hay contenido en una categoría, se muestra un mensaje informativo.

## Configuración y Ejecución

A continuación, se proporcionan los pasos básicos para configurar y ejecutar TecnoWave en su entorno de desarrollo:

1. Clone el repositorio desde GitHub:

```
git clone https://github.com/fellgar246/ch_py_pf_garcia
cd tecnowave
```

2. Instale las dependencias del proyecto:

```
pip install -r requirements.txt
```

3. Realice las migraciones de la base de datos:

```
python manage.py migrate
```

4. Cree un superusuario para acceder a las funciones de administración:

```
python manage.py createsuperuser
```

5. Inicie el servidor de desarrollo:

```
python manage.py runserver
```

6. Abra su navegador y vaya a [http://localhost:8000/](http://localhost:8000/) para acceder a TecnoWave.


    ¡Esperamos que TecnoWave sea una plataforma útil y emocionante para la comunidad tecnológica!  



