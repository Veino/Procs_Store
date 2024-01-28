import functools
from django.shortcuts import redirect
from rest_framework.response import Response
from django.contrib import messages

def IsProcsAdmin(view_func):

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.isProcsAdmin:
            return view_func(request, *args, **kwargs)
            print(request.user.IsProcsAdmin)
        messages.info(request, "You need to be a Procs Admin")
        print("You need to be a Procs Admin")
        return Response("You need to be a Procs Admin")
    return wrapper