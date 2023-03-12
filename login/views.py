from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .form import ProfileForm,ExempleForm
from .models import*
from django.forms import inlineformset_factory,modelformset_factory
# Create your views here.

def loginPage(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"login ёки парол нотугри")    
    return render(request,"login/login.html")

def logoutUser(request):
    logout(request)
    return redirect('login')





def setting(request):
    user=request.user.profile.id
    profile=Profile.objects.get(id=user)
    form=ProfileForm(instance=profile)
    if request.method == "POST":
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('setting')
    
    context={"form":form,"profile":profile}
    return render(request,'homes/setting.html',context)




def bolim(request):
    user=request.user.profile.id
    
    bolim=Bolim.objects.all()
    
    
    
    
    context={"bolim":bolim}
    return render(request,'homes/exemple.html',context)

def naryad(request,pk):
    user=request.user.profile.id
    exemFormSet=inlineformset_factory(Bolim,Naryad,fields=('oylar','hodim','narxnoma','miqdor','summa',),extra=3)
    bolim=Bolim.objects.get(id=pk)
    formsets=exemFormSet(queryset=Naryad.objects.none(),instance=bolim)
    
    
    if request.method == "POST":
        form=exemFormSet(request.POST,instance=bolim)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    
    
    context={"formsets":formsets}
    return render(request,'homes/formset.html',context)
