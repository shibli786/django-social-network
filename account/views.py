from django.shortcuts import render ,render,get_object_or_404
from  django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


def user_login(request):
	if(request.method=="POST"):
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])
			if user is not None:

				if(user.is_active):
					login(request,user)
					return HttpResponse('Authenticated successfully')
				else:
					return HttpResponse('Disabled Account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
		return render(request,'account/login.html',{'form':form})
@login_required
def dashboard(request):
	return render(request,'account/dashboard.html',{'section':'dashboard'})

def register(request):
	if request.method=="POST":
		user_form =UserRegistrationForm(request.POST)
		if(user_form.is_valid):
			new_user= user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			return render(request,'account/register_done.html',{'new_user':new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request,'account/register.html',{'user_form':user_form})

@login_required
def user_list(request):
	users = User.objects.filter(is_active=True)
	return render(request,'account/user/list.html',{'section':'people','users':users})

@login_required
def user_detail(request):
	user =get_object_or_404(User,username=username,is_active=True)
	return render(request,'account/user/detail.html',{'section':'people','user':user})


