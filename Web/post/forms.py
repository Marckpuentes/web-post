from django import forms

from .models import Categories, CreatePost

class CategoriesForm(forms.ModelForm):

    def clean_category(self):
        #captura el valor enviado por input
        category = self.cleaned_data.get("category")
        if 'category' in self.changed_data:
            if Categories.objects.filter(category=category.capitalize()).exists():
                raise forms.ValidationError("Esta Categoria ya esta registrada")
        #manda el valor con la primera letra en mayuscula
        return category.capitalize()

    class Meta:
        model = Categories
        fields = ['category']
        widgets =  {
            'category':forms.TextInput(attrs={'placeholder':'Ingresa la nueva categoria', 'class':'form-control'})
            }

class CategoriesUpdateForms(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ['category']
        widgets =  {
            'category':forms.TextInput(attrs={'class':'form-control'})
            }
            
    def clean_category(self):
        #captura el valor enviado por input
        category = self.cleaned_data.get("category")
        if 'category' in self.changed_data:
            if Categories.objects.filter(category=category.capitalize()).exists():
                raise forms.ValidationError("Esta Categoria ya esta registrada")
        #manda el valor con la primera letra en mayuscula
        return category.capitalize()          
        

class PostUpdateForms(forms.ModelForm):
    

    #category = CustomMMCF(queryset=Categories.objects.all(),
    #widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = CreatePost
        fields = ['title', 'img', 'category', 'content' ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            #'category':forms.CheckboxSelectMultiple()
        }

"""     def __init__ (self, *args, **kwargs):
        super(PostUpdateForms, self).__init__(*args, **kwargs)
        self.fields["category"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["category"].help_text = "" 
        self.fields["category"].queryset = Categories.objects.all()   """ 
            
