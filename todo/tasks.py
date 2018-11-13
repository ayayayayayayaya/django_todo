from background_task import background
from .models import Todo
from django.utils import timezone
import slackweb
import datetime

with open('todo/.url') as f:
    url = f.readline()
    
@background(schedule = timezone.now())
def notify_user():
    msg = '本日の予定は\n'
    now = datetime.datetime.now()
    today = now.strftime('%Y-%m-%d')
    todo = Todo.objects.filter(deadline = str(today))
   
    for i in todo:
        msg += i.text + '\n'
    else:
        msg += 'です，'
    
    if not todo:
        msg = '本日の予定はありません'
    slack = slackweb.Slack(url = url)
    slack.notify(text = msg, username = 'ToDo-bot') 
       
notify_user(repeat = 86400)
