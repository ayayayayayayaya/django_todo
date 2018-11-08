from django.forms import ModelForm , TextInput, Textarea, CheckboxInput, SelectDateWidget, ChoiceField, Select
from .models import Todo
   
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['text', 'memo', 'star', 'choice']
        labels = {
                'text': 'Todo',
                'memo': 'メモ',
                'star': '重要',
                'choice': '種別',
                }
        widget = {
                'text': TextInput(attrs = {'class': ''}),
                'memo': Textarea(attrs = {'class': ''}),
                'star': CheckboxInput(attrs = {'class': ''}), 
                'choice': Select(attrs = {'class': ''}),
                }

