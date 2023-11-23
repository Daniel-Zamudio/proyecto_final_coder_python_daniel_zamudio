from django.shortcuts import render,redirect
from .models import Post, Img
from .forms import UserCreationFormCustom, UserEditForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def about(request): #verrrrrr acerca de mi
    return render(request, "about.html")

def post_list(request):
    post = Post.objects.all()
    # print(post)
    return render(request, "post.html", {"post" : post})

class PostCreateView(CreateView):
    model = Post
    template_name = "crear_post.html"
    success_url = reverse_lazy("post_list")
    fields = ["articulo", "texto", "autor", "fecha", "imagen"]

class PostDetailView(DetailView):
    model = Post
    template_name = "detalle_post.html"

class PostListView(ListView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"

class PostUpdateView(UpdateView):
    model = Post
    template_name = "editar_post.html"
    success_url = reverse_lazy("post_list")
    fields = ["articulo", "texto", "autor", "fecha", "imagen"]

class PostDeleteView(DeleteView):
    model = Post
    template_name = "eliminar_post.html"
    success_url = reverse_lazy("post_list")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("inicio")
        else:
            # Manejo de error de inicio de sesión
            return render(request, 'login.html', {'error': 'Verificar. El usr o la contraseña son incorrectos'})
    return render(request, 'login.html') 

def user_register(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationFormCustom()
        return render(request, 'register.html', {'form': form})      

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST, request.FILES, instance=usuario) 
        if mi_formulario.is_valid():
            if mi_formulario.cleaned_data.get("imagen"):
                    usuario.img.imagen = mi_formulario.cleaned_data.get("imagen")
                    usuario.img.save()
            
            mi_formulario.save()
            return render("inicio.html")
    else:
        mi_formulario = UserEditForm(initial={'imagen':usuario.img.imagen}, instance=request.user)
    return render(request, "editarPerfil.html", {"mi_formulario": mi_formulario, "usuario": usuario})


class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = "cambiar_contraseña.html"
    success_url = reverse_lazy("inicio")


