from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from class_periods.models import ClassPeriods, SessionTokens, StudentCheckin

# Create your views here.
@login_required(login_url='/login')
def IndexView(request):
    classes = ClassPeriods.objects.all().filter(owner=request.user)
    classes_dict = [{'name': a.name, 'id': a.id} for a in classes]
    return render(request,'ClassList.html', {'classes': classes, 'user': request.user.username})

def ClassesView(request):
    return "hi"

@login_required(login_url='/login')
def HelpView(request):
    return render(request, 'Help.html', {'user': request.user.username})

@login_required(login_url='/login')
def SessionsView(request, class_id=None):
    print(class_id)
    class_obj = get_object_or_404(ClassPeriods, id=class_id)
    class_name = class_obj.name
    sessions = SessionTokens.objects.all().filter(class_period=class_obj)
    if sessions.exists():
        sessions_dict = [{'token': a.token, 'creation_date': a.creation_date, 'expiration_date': a.expiration_date, 'id': a.id} for a in sessions]
    else:
        sessions_dict = []
    return render(request, 'SessionList.html', {'sessions': sessions_dict, 'name': class_name, 'user': request.user.username})

@login_required(login_url='/login')
def AttendanceView(request, session_id=None):
    session_obj = get_object_or_404(SessionTokens, id=session_id)

    checkins = StudentCheckin.objects.all().filter(session=session_obj)
    if checkins.exists():
        sessions = [{'pid': a.pid, 'name': a.name, 'checkin_date': a.checkin_date} for a in checkins]
    else:
        sessions = []
    return render(request, 'AttendanceList.html', {'checkins': sessions, 'name': session_obj.token, 'user': request.user.username})