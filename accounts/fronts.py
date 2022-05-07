from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import CreateView, UpdateView, ListView

from accounts.forms import UserForm, LdapServerForm
from accounts.models import User,   LdapServer, UserLoginInfo


class UserListView(LoginRequiredMixin,  ListView):
    model = User


class LdapServerListView(LoginRequiredMixin,  ListView):
    model = LdapServer


class LdapServerCreateView(LoginRequiredMixin, CreateView):
    model = LdapServer
    form_class = LdapServerForm
    success_url = '/accounts/ldapserver/list/'
    template_name = 'accounts/ldapserver_form.html'


class LdapServerUpdateView(LoginRequiredMixin, UpdateView):
    model = LdapServer
    form_class = LdapServerForm
    success_url = '/accounts/ldapserver/list/'
    template_name = 'accounts/ldapserver_form_update.html'


def ldapserver_detail(request, pk):
    this_object = LdapServer.objects.get(pk=pk)
    return render(request, 'accounts/ldapserver_detail.html', locals())



@login_required
def user_delete(request, pk):
    status = 1
    try:
        sg = User.objects.get(pk=pk)
        UserLoginInfo.objects.filter(user=sg).delete()
        sg.delete()
        status = 0
    except Exception as e:
        pass
    return JsonResponse({'status': status})


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = '/accounts/user/list/'
    template_name = 'accounts/user_form.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = '/accounts/user/list/'
    template_name = 'accounts/user_form_update.html'


@login_required
def ldapserver_delete(request, pk):
    status = 1
    try:
        sg = LdapServer.objects.get(pk=pk)
        sg.delete()
        status = 0
    except Exception as e:
        pass
    return JsonResponse({'status': status})


@login_required
@xframe_options_exempt
def ldap_user_add_to_local(request):
    status = 1
    aid = 0
    if request.method == 'POST':
        email_prefix = request.POST['email_prefix']
        email_suffix = request.POST['email_suffix']
        display_name = request.POST['display_name']
        cn = request.POST['cn']
        email = "{email_prefix}@{email_suffix}".format(email_prefix=email_prefix, email_suffix=email_suffix)
        try:
            result,b = User.objects.get_or_create(username=cn, email=email, nickname=display_name)
            aid = result.id
            status = 0
        except Exception as e:
            print(e)
    return JsonResponse({'status': status, 'aid': aid})
