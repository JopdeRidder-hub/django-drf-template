from django.contrib.auth.views import LoginView


class CustomAdminLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True
