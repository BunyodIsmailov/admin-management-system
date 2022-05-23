from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import  login, logout
from .EmailBackEnd import EmailBackEnd
from django.contrib import messages
def showDemoPage(request):
	return render(request,'demo.html')

def showLoginPage(request):
	return render(request,'login_page.html')

def doLogin(request):
	if request.method != "POST":
		return HttpResponse("<h2>Method Not Allowed </h2>")
	else:
		user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
		print(user)
		if user != None:
			login(request,user)
			return HttpResponseRedirect("admin_home")
		else:
			messages.error(request,"Invalid Login Details")
			return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")