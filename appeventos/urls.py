from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('crear_evento/', views.crear_evento, name='crear_evento'),
    path('eventos/', views.eventos_disponibles, name='eventos'),
    path('inscribirse/<int:evento_id>/', views.inscribirse, name='inscribirse'),
]
