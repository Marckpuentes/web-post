from django.shortcuts import render
from django.views.generic.base import TemplateView 


#Templateview para devolver un template

class HomePageView(TemplateView):
    template_name = "core/home.html"

    #pasar dicionario de contexto 
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['title'] = "MarckWTF"
#        return context

    def get(self, request, *arg, **kwargs):
        return render (request, self.template_name, {'title':"La Mejor Web"})

class SamplePageView(TemplateView):
    template_name = "core/404.html"    


#def sample(request):
#    return render(request, "core/sample.html")