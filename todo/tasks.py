from background_task import background
from .models import Todo
from django.utils import timezone
import slackweb

@background(schedule = timezone.now())
def notify_user():
    todo = Todo.objects.all()
    print(todo)
    #slack = slackweb.Slack(url = 'https://hooks.slack.com/services/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')
    #slack.notify(text = todo)
            
notify_user()
