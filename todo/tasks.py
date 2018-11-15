from background_task import background
from .models import Todo
from django.utils import timezone
import slackweb
import datetime
from .modules.scraping import get_html, parse_html

HOURLY = 3600
DAILY = 24 * HOURLY
WEEKLY = 7 * DAILY
EVERY_2_WEEKS = 2 * WEEKLY
EVERY_4_WEEKS = 4 * WEEKLY
NEVER = 0

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
        if i.choice == 'anime':
            Todo.objects.create(text = i.text, 
                                memo = i.memo,
                                star = i.star,
                                choice = i.choice, 
                                deadline = i.deadline + datetime.timedelta(weeks = 1)
                                )

            i.delete() #一日後に消すとかにしたほうがいい
        elif i.choice == 'book':
            page = get_html(i.text)
            prev, prev_release, nxt, nxt_release = parse_html(page)
            Todo.objects.create(text = i.text,
                                memo = '最新刊は: ' + prev + ', 発売日: ' + prev_release + '\n' + '次巻: ' +  nxt + 
                                '，発売日: ' + nxt_release,
                                star = i.star,
                                choice = i.choice,
                                deadline = nxt_release
                                )
            i.delete() 
    else:
        msg += 'です，'
    
    if not todo:
        msg = '本日の予定はありません'
    slack = slackweb.Slack(url = url)
    slack.notify(text = msg, username = 'ToDo-bot') 
       
notify_user(repeat = DAILY)

