from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm  # Classe de um formulario
    success_url = reverse_lazy(
        "login"
    )  # O usuario vai se cadastrar e vai ser redirecionado para o login
    template_name = "registration/register.html"
