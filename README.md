# Plataforma de gestión de eventos 📆

App web desarrollada en Django para gestionar eventos, con autenticación de usuarios, autorización por roles, inscripción a eventos y control de acceso. 

Los usuarios se crearon desde el panel de administración y se utilizaron vistas basadas en funciones (FBV), en lugar de vistas basadas en clases (CBV), por lo que no se agregaron mixins como `LoginRequiredMixin`, en su lugar se usaron decoradores `@login_required` y `@permission_required`, que cumplen el mismo propósito de proteger las vistas y controlar el acceso según los permisos del usuario.

## Funcionalidades principales 📌

- Login y logout de usuarios
- Creación de eventos por usuarios autorizados 
- Inscripción a eventos
- Visualización de eventos inscritos en página de inicio
- Panel de administración con control de permisos
- Páginas personalizadas para errores 403 y 404
- Sistema de mensajes para mostrar errores y confirmaciones

## Roles de usuario 👥

- **Administrador**: acceso completo (crear, editar, eliminar eventos)
- **Organizador**: puede crear y editar eventos, pero no eliminarlos
- **Asistente**: solo puede ver e inscribirse en eventos 

Los permisos se asignan usando `auth_permission` de Django y se gestionan desde el panel de administración.

## Usuarios creados 👤

- *Administradores*: catalina y renata
- *Organizadores*: roberto y victor
- *Asistentes*: gustavo y maria
- **Contraseña de usuarios**: gestion@eventos123

## Autenticación y autorización 🔐

- Se usa el modelo `Auth` de Django
- Las vistas están protegidas con `@login_required` y `@permission_required`
- Los usuarios deben iniciar sesión para acceder a cualquier vista relacionada con eventos
- Si un usuario intenta acceder sin permisos, se muestra la página `403.html`

## Manejo de errores 💣

- Implementación de páginas 403 y 404 
- En vistas como `crear_evento`, se usa `messages.error` para mostrar errores amigables

## Configuración y seguridad ⚙

- Se configuró `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` en settings.py
- Se activó el uso de sesiones
- La configuración para HTTPS está agregada, pero comentada, ya que el proyecto está en desarrollo local

## Ejecución 🚀

1. Clonar el repositorio
2. Crear y activar entorno virtual:
    `python -m venv venv`
    `.\venv\Scripts\activate`
3. Instalar dependencias:
    `pip install -r requirements.txt`
4. Ejecutar migraciones:
    `python manage.py migrate`
5. Crear superusuario:
    `python manage.py createsuperuser`
6. Ejecutar el servidor:
    `python manage.py runserver`
7. Acceder a:
    `http://localhost:8000`

## Usuarios de prueba 👤
Puedes crear usuarios desde el admin y asignarlos a los grupos:
- Administradores
- Organizadores
- Asistentes

## Desarrolladora
Jasmin S. | Fan del código bonito ✨