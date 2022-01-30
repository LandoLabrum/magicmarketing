from django.contrib.auth import decorators
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
 
def unauthenticated_user(view_func):
   def wrapper_func(request, *args, **kwargs):
      if request.user.is_authenticated:
         return redirect('home')
      else:
         return view_func(request, *args, **kwargs)
   return wrapper_func

def allowed_users(allowed_roles=[]):
   def decorator(view_func):
      def wrapper_func(request, *args, **kwargs):
         group = None
         if request.user.groups.exists():
            group = request.user.groups.all()[0].name
         if group in allowed_roles:
            return view_func(request, *args, **kwargs)
         else:
            # print(f'GROUP: {group}') 
            # print(f'allowed_roles: {allowed_roles}') 
            return HttpResponse('You are not authed to view this')
      return wrapper_func
   return decorator

def admin_only(view_func):
   def wrapper_func(request, *args, **kwargs):
      group = None
      if request.user.groups.exists():
         group = request.user.groups.all()[0].name
      if group == 'customer':
         return redirect ('account')
      if group == 'admin':
         return redirect (request, *args, **kwargs)
   return wrapper_func
