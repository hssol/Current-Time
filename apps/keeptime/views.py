from django.shortcuts import render
from time import gmtime, strftime, localtime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %I:%M %p", localtime())
    }
    return render(request,'keeptime/index.html', context)

