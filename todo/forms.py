from django.forms import ModelForm , TextInput, Textarea, CheckboxInput, SelectDateWidget, ChoiceField, Select
from .models import Todo
   
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['text', 'memo', 'star', 'choice', 'notice']
        labels = {
                'text': 'Todo',
                'memo': 'メモ',
                'star': '重要',
                'choice': '種別',
                'notice': '通知',
                }
        widget = {
                'text': TextInput(attrs = {'class': ''}),
                'memo': Textarea(attrs = {'class': ''}),
                'star': CheckboxInput(attrs = {'class': ''}), 
                'choice': Select(attrs = {'class': ''}),
                'notice': SelectDateWidget(attrs = {'class': ''}),
                }

