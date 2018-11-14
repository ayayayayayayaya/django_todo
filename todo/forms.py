from django.forms import ModelForm , TextInput, Textarea, CheckboxInput, Select, SelectDateWidget
from .models import Todo
#import bootstrap_datepicker_plus as datetimepicker

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['text', 'memo', 'star', 'choice', 'deadline']
        labels = {
                'text': 'Todo',
                'memo': 'メモ',
                'star': '重要',
                'choice': '種別',
                'deadline': '通知',
                }
        widget = {
                'text': TextInput(attrs = {'class': ''}),
                'memo': Textarea(attrs = {'class': ''}),
                'star': CheckboxInput(attrs = {'class': ''}), 
                'choice': Select(attrs = {'class': ''}),
                'deadline': SelectDateWidget(attrs = {'class':''}),
                #'deadline': datetimepicker.DatePickerInput(format = '%Y-%m-%d', options = {'locale': 'ja', 'dayViewHeaderFormat': 'YYYY/MMMM'}),
                }

