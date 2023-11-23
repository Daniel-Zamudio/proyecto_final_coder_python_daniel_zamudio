from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

#Para las imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path("about/", views.about, name = "quiensoy"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('register/', views.user_register, name="user_register"),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('cambiarContraseña/', views.CambiarContraseña.as_view(), name="CambiarContraseña"),
    
    path('pages/', views.PostListView.as_view(), name="post_list"),
    path('pages/crear', views.PostCreateView.as_view(), name="crear_post"),
    path('pages/<pk>', views.PostDetailView.as_view(), name="detalle_post"),
    path('pages/<pk>/editar', views.PostUpdateView.as_view(), name="editar_post"),
    path('pages/<pk>/eliminar', views.PostDeleteView.as_view(), name="eliminar_post"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
