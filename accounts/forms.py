from django import forms

from accounts.models import User, LdapServer


class LdapServerForm(forms.ModelForm):
    class Meta:
        model = LdapServer
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'phone', 'is_lock', 'is_active', 'is_superuser')
        labels = {
            'username': '用户名',
            'nickname': '中文名',
            'email': '邮箱',
            'phone': '电话',
            'is_lock': '是否锁定',
            'is_active': '是否激活',
            'is_superuser': '管理员',
        }
