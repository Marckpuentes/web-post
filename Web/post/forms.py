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
      
    def __init__(self, *args, **kwargs):
        super(PostUpdateForms, self).__init__(auto_id=True, *args, **kwargs)
        self.fields['category'].label = ''
        self.fields['title'].label = ''
        self.fields['content'].label = ''
        self.fields['img'].label = ''

    
    class Meta:
        model = CreatePost
        fields = ['title', 'img', 'category', 'content' ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'img':forms.ClearableFileInput(),
            'category':forms.CheckboxSelectMultiple(),
            'content':forms.Textarea(attrs={'class':'form-control'})
        }

            
