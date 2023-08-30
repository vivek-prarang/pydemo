from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def is_employee(view_func):
    @login_required
    def decorated_view_func(request, *args, **kwargs):
        if not request.user.is_employee:
            return redirect('/login')  # Replace 'login' with the appropriate URL name for your login page
        return view_func(request, *args, **kwargs)
    return decorated_view_func

def is_client(view_func):
    @login_required
    def decorated_view_func(request, *args, **kwargs):
        if not request.user.is_client:
            return redirect('/login')  # Replace 'login' with the appropriate URL name for your login page
        return view_func(request, *args, **kwargs)
    return decorated_view_func