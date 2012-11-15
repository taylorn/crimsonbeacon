from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def admin_panel_view(request):
    if request.user.is_staff:
        return render_to_response('admin_panel.html', context_instance=RequestContext(request))
    else: raise Http404
    
def login(request, attempts=0):
    if attempts > 3:
        return render_to_response('/')
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_staff:
            login(request, user)
        else: 
            attempts += 1
            return render_to_response('login.html', {'attempts': attempts},
                                      context_instance=RequestContext(request))
    return render_to_response('admin_login.html', context_instance=RequestContext(request))