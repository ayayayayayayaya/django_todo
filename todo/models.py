from django.db import models

CHOISES = (
        ('task', 'タスク'),
        ('anime', 'アニメ'),
        ('book', '本'),
        ('game', 'ゲーム'),
        )
class Todo(models.Model):
    id = models.AutoField(primary_key = True)
    text = models.CharField(max_length = 100)
    memo = models.TextField(null = True, blank = True)
    star = models.BooleanField(default = False)    
    choice = models.CharField(max_length = 10, blank = True, choices = CHOISES, default = 'task')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'todos'

