

from django.shortcuts import render,get_object_or_404


from .models import Manu

def manu(request,restname):
    foll = get_object_or_404(Manu,pk=restname['pach vai'])

    return render(request,'manu.html',{'manu': foll})


def show(request,manu_id):
    srest = get_object_or_404(Manu , pk=manu_id)
    return render(request, 'show.html', {'show':srest})