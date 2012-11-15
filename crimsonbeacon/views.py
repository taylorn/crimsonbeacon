from crimsonbeacon import settings
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    context = {'sidebar_on': True}
    return render_to_response('index.html', context,
                              context_instance=RequestContext(request))

def admin_panel_view(request):
    if request.user.is_staff:
        return render_to_response('admin_panel.html', context_instance=RequestContext(request))
    else: raise Http404
    
def login_view(request):
    if request.user and request.user.is_staff:
        return logout_view(request)
    context = {'login_url': settings.ADMIN_LOGIN_URL}
    # TODO: fix login attempts redirect
    try:
        if request.attempts > 3:
            return HttpResponseRedirect(reverse_lazy('index'))
    except AttributeError: request.attempts = 0
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            request.attempts += 1
    return render_to_response('admin_login.html', context,
                              context_instance=RequestContext(request))

def logout_view(request):
    context = {'login_url': settings.ADMIN_LOGIN_URL}
    if request.POST: 
        logout(request)
        return HttpResponseRedirect(reverse_lazy('index'))
    return render_to_response('admin_logout.html', context,
                              context_instance=RequestContext(request))
    
    


