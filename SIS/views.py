from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.


def base(request):
    return render(request,"base.html")

def add(request):
    if request.method=="POST":
        st = StudentRegistration(request.POST)
        if st.is_valid():
            st.save()
            st =StudentRegistration()
    else:
        st = StudentRegistration()
    stud = User.objects.all()
    return render(request,"addandshow.html",{'form':st,'stud':stud})

def update(request, id):
    if request.method=="POST":
        pi = User.objects.get(pk=id)
        st = StudentRegistration(request.POST, instance=pi)
        if st.is_valid():
            st.save()
    else:
        pi = User.objects.get(pk=id)
        st = StudentRegistration(instance=pi)
    return render(request,"updatestudent.html",{'form':st})

def delete(request, id):
    if request.method=="POST":
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect("/")