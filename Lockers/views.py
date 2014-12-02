# coding=utf-8
from django.contrib.auth.decorators import login_required
import django_filters
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics
from Lockers.serializers import *

from django.conf.urls import patterns
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect

# Este metodo hace el login del usuario y lo redirecciona a la pagina de
# administrador, si no lo hace lanza un mensaje de error
def login_user(request):
    state = "Inicie sesion"
    username = password = ''
    if not request.user.is_authenticated():
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    state = 'Inicio de sesion exitoso'
                    # urlpatterns =patterns ('', (r'^admin_page/$', RedirectView.as_view(url='http://google.com')),)
                    # return redirect('/admin_page/')
                    return HttpResponseRedirect('/Administrador/')
                else:
                    state = 'Verifique su Nombre de Usuario y Contraseña'
            else:
                state = 'Verifique su Nombre de Usuario y Contraseña'

        return render_to_response('auth.html', {'state': state, 'username': username}, RequestContext(request))
    else:
        return HttpResponseRedirect('/login'
                                    '/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')


@login_required
def login_authentification(request):
    if request.path == "/Administrador/" :
        return render_to_response('admin_lockers.html', RequestContext(request))
    elif request.path == "/Usuarios/" :
        return render_to_response('admin_users.html', RequestContext(request))
    elif request.path == "/Lockers_Areas/" :
        return render_to_response('admin_areas.html', RequestContext(request))
    elif request.path == "/Historial/" :
        return render_to_response('admin_log.html', RequestContext(request))

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AreasViewSet(viewsets.ModelViewSet):
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LockersViewSet(viewsets.ModelViewSet):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RatesViewSet(viewsets.ModelViewSet):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# Filters
class LockersFilter(django_filters.FilterSet):
    # area = django_filters.CharFilter(name='log_timestamp', lookup_type='startswith')
    area = django_filters.NumberFilter(name='fk_area', lookup_type='exact')
    status = django_filters.NumberFilter(name='locker_status', lookup_type='exact')
    # max_date = django_filters.DateTimeFilter(name='area_date_received', lookup_type='lte')
    #min_date = django_filters.DateTimeFilter(name='area_date_received', lookup_type='gte')

    class Meta:
        model = Lockers
        fields = ['locker_id', 'locker_status', 'fk_area', 'fk_user']
        #fields = ['locker_id', 'locker_match', 'locker_status', 'fk_area']


class LockersSearch(generics.ListCreateAPIView):
    queryset = Lockers.objects.all()
    serializer_class = LockersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = LockersFilter

