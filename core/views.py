from django.views import generic as views


class HomeView(views.TemplateView):
    template_name="core/home.html"


class AboutView (views.TemplateView):
    template_name="core/about.html"   
# Create your views here.
 

