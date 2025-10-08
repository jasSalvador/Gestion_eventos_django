from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm
from django.contrib import messages

#modelo auth
from django.contrib.auth import authenticate, login, logout
#decorador @ / login_required restringe/obliga a iniciar sesion
from django.contrib.auth.decorators import login_required, permission_required


#login
def login_view(request):
    #revisar tipo de metodo q tenemos en peticion
    if request.method == 'POST': #recibiendo la info del form
        #accedemos al valro del form y lo guardamos en variable
        username = request.POST['username'] 
        password = request.POST['password']
	    #autenticar al usuario
        #revisamos si existe el usuario y contraseña correcta
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
	    #inicio sesion
            login(request, usuario) #se guarda en sesion la info del usuario
            return redirect('inicio')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')



#logout
def logout_view(request):
    logout(request)
    return redirect('login')



#inicio
#@login_required solo si se inicio sesion se puede acceder a inicio
#@permission_required tambien debe tener permiso para ver inicio
@login_required 
def inicio(request):
    eventos = Evento.objects.filter(asistentes=request.user)
    return render(request, 'inicio.html', {'eventos': eventos})

    

#crear eveento
#@login_required solo si se inicio sesion se puede acceder a inicio
#@permission_required tambien debe tener permiso para ver inicio
@login_required 
@permission_required('appeventos.add_evento', raise_exception=True)
def crear_evento(request):
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)

        if evento_form.is_valid():
            # Guardar evento
            evento = evento_form.save(commit=False)
            evento.creador = request.user
            evento.save()

            # Mensaje de éxito
            messages.success(request, f"El evento fue creado con éxito ✅")
            return redirect('inicio')
        else:
            # Mensajes de error
            messages.error(request, "Ah ocurrido un error ⚠")
    else:
        evento_form = EventoForm()
    return render(request, 'crear_evento.html', {'evento_form': evento_form,})


#para mostrar eventos disponibles para registrarse
@login_required
def eventos_disponibles(request):
    eventos = Evento.objects.exclude(asistentes=request.user)
    return render(request, 'eventos.html', {'eventos': eventos})


#para procesar inscripcion
@login_required
def inscribirse(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.asistentes.add(request.user)
    messages.success(request, "Te has inscrito correctamente al evento ✅")
    return redirect('inicio')

