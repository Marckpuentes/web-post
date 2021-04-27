from django.shortcuts import render
from .forms import CategoriesForm, CategoriesUpdateForms, PostUpdateForms
from .models import Categories, CreatePost
from django.contrib.auth.models import User
from django import forms
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CategoriesView(CreateView):
    form_class = CategoriesForm
    model = Categories  
    template_name = "post/Add_Category.html"
    def get_success_url(self):
        return reverse_lazy('post:add')+ '?ok'
    
    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        #obtiene los datos del modelo y los manda con el nombre de objects al template
        context["objects"] = self.model.objects.all()
        return context

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CategoriesDelete(DeleteView):
    model = Categories
    success_url = reverse_lazy('post:add')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #obtiene los datos del modelo y los manda con el nombre de objects al template
        context["objects"] = Categories.objects.all()
        return context

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CategoriesUpdate(UpdateView):
    form_class = CategoriesUpdateForms
    model = Categories
    success_url = reverse_lazy('post:add')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #obtiene los datos del modelo y los manda con el nombre de objects al template
        context["objects"] = Categories.objects.all()
        return context

class PostView(ListView):
    model = CreatePost
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #obtiene los datos del modelo y los manda con el nombre de objects al template
        context["objects"] = Categories.objects.all()
        return context

class DetailPost(DetailView):
    model = CreatePost

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PostUpdate(UpdateView):
    form_class = PostUpdateForms
    model = CreatePost
    template_name = "post/update_post.html"

    def get_success_url(self):
        return reverse_lazy('post:detail', args=[self.object.slug])+ '?ok' 

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PostCreate(CreateView):
    form_class = PostUpdateForms
    template_name = "post/create_post.html"
    success_url = reverse_lazy('post:view')

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PostDelete(DeleteView):
    model = CreatePost
    success_url = reverse_lazy('post:view')    
    