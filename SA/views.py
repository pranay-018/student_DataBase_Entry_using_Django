from django.shortcuts import render
from django.http import HttpResponse
from SA.Stuforms import stuforms,srcform,delform,upform
from SA.models import stumodel
# Create your views here.
def menu(request):
    return render(request,'menu.html',{})
def insert(request):
    stuobj=stuforms()
    txt="inserted Succesfully into DB "
    if request.method=='POST':
        stuobj=stuforms(request.POST)
        if stuobj.is_valid():
            Name=stuobj.cleaned_data['name']
            Reg=stuobj.cleaned_data['regno']
            M1=stuobj.cleaned_data['m1']
            M2=stuobj.cleaned_data['m2']
            print(Name,Reg,M1,M2)
            p=stumodel(s_name=Name,s_regno=Reg,s_m1=M1,s_m2=M2)
            p.save()
            return render(request,'ack.html',{'text':txt})
    return render(request,'insert.html',{'form1':stuobj})
def display(request):
    title="ALL DETAILS"
    queryset=stumodel.objects.all()
    context={
        "t":title,
        "query":queryset,
    }
    print(queryset)
    return render(request,'detail.html',context)
def search(request):
    title="search Student"
    srcobj=srcform(request.POST or None)
    if srcobj.is_valid():
        src_name=srcobj.cleaned_data['s_name']
        queryset=stumodel.objects.filter(s_name=src_name)
        if len(queryset)==0:
            return render(request,'ack.html',{"text":"student not found"})
        context={
            "t":title,
            "query":queryset,
        }
        return render(request,'detail.html',context)
    return render(request,'search.html',{"form":srcobj,"title":title})
def delete(request):
    title="deletion of student"
    delobj=delform(request.POST or None)
    if delobj.is_valid():
        de_name=delobj.cleaned_data['d_name']
        queryset=stumodel.objects.filter(s_name=de_name)
        if len(queryset)==0:
            return render(request,"ack.html",{"text":"student not found "})
        else:
            queryset=stumodel.objects.filter(s_name=de_name).delete()
            return render(request,"ack.html",{"text":"removed"})
    return render(request,'delete.html',{"form":delobj,"title":title})
def update(request):
    title="updation"
    upobj=upform(request.POST or None )
    if upobj.is_valid():
        upname=upobj.cleaned_data['u_name']
        queryset=stumodel.objects.filter(s_name=upname).update(s_m1=100,s_m2=100)
        return render(request,"ack.html",{"text":"updated"})
    return render(request,"update.html",{"form":upobj,"title":title})