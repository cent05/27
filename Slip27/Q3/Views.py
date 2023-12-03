from django.shortcuts import render

# Create your views here.
def learn_dj(request):
    course_name='python'
    duration='5 weeks'
    fees='5000|-'
    details={'nm':course_name,'du':duration,'fs':fees}
    return render(request,'course1.html',details)