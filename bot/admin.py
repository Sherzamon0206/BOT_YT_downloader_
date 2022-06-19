from django import forms
# Register your models here.
from django.contrib import admin
from bot.models import AdminPanel,Profile
# Register your models here.
from  bot.forms import ProfileForm





@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =('id','exeterenal_id','username','f_name','l_name')
    form = ProfileForm




admin.site.register(AdminPanel)