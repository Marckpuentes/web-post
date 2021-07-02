from django.shortcuts import render
from django.shortcuts import Http404, get_object_or_404
from .forms import CategoriesForm, CategoriesUpdateForms, PostUpdateForms
from .models import Categories, CreatePost
from django.contrib.auth.models import User
from django import forms
from cap.models import Cap
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.urls import reverse_lazy

# Create your views here.

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CategoriesView(CreateView):
    form_class = CategoriesForm
    model = Categories  
    template_name = "post/Add_Category.html"
    def get_success_url(self):
        return reverse_lazy('post:add')+ '?ok'
    

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CategoriesDelete(DeleteView):
    model = Categories
    success_url = reverse_lazy('post:add')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #obtiene los datos del modelo y los manda con el nombre de objects al template
        context["objects"] = self.model.objects.all()
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
        
    def get_success_url(self):
        return reverse_lazy('post:search', args=[self.object.category])
        
class DetailPost(DetailView):
    model = CreatePost
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = context['object']
        #obtiene los datos del modelo y los manda con el nombre de objects al template
        if Cap.objects.filter(title = title):
            context["objects"] = Cap.objects.filter(title = title)
            return context
        return context    
    

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


    model = CreatePost
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #obtiene los datos del modelo y los manda con el nombre de objects al template
        context["objects"] = Categories.objects.all()
        return context


class Search(ListView):
    model = CreatePost
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #obtiene los datos del modelo y los manda con el nombre de objects al template
        context["objects"] = Categories.objects.all()
        return context

    def get_queryset(self, **kwargs):
        category = self.kwargs.get('category',None)
        if CreatePost.objects.filter(category__category = category):
            Search = CreatePost.objects.filter(category__category = category)
            return Search
        else:
            raise Http404()
    