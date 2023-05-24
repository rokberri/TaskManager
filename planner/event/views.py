from django.shortcuts import render, redirect
from django.template.backends import django
from django.views.decorators.http import require_http_methods
from .models import Event, Day
import django.utils.timezone


def index(request):
    days = Day.objects.order_by('date')
    events = Event.objects.order_by('date')
    today = django.utils.timezone.now().date()
    # today = str(today)[0:10]
    # today =
    print(today)
    return render(request, 'Event/index.html', {'title': 'Main Page', 'days': days, 'events': events, 'today': today})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    date = request.POST['date']
    summary = request.POST['description']
    event = Event(date=date, title=title, description=summary)
    days = Day.objects.all()
    not_exsist = True
    if len(days) != 0:
        for item in days:
            print(item.date)
            print(date)
            if str(item.date) == str(date):
                item.events.append(event)
                not_exsist = False
                item.save()
                break
        if not_exsist:
            day = Day(date=date)
            day.events.append(event)
            day.save()
    else:
        day = Day(date=date)
        day.events.append(event)
        day.save()
    event.save()
    return redirect('index')


def delete(request, day_id, event_id):
    event = Event.objects.get(id=event_id)
    day = Day.objects.get(id=day_id)
    print('LEN OF EVENTS')
    print(len(day.events))
    # day.events.remove(event)
    event.delete()
    is_null = True
    for e in Event.objects.all():
        if e.date == day.date:
            is_null = False
            break
    if is_null:
        day.delete()

    return redirect('index')


def update(request, event_id):
    event = Event.objects.get(id=event_id)
    event.is_complete = not event.is_complete
    event.save()
    return redirect('index')

