from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.db import models
from django.db.models.base import Model, ModelBase
from django.contrib import admin
from django.contrib import auth
from django.contrib.auth.models import User, UserManager
from django.conf import settings

#-------------------------------------------------------------------------------

#class Logueable(models.Model):
#    fecha_crea = models.DateTimeField(_('fecha creacion'), auto_now_add=True, editable=False)
#    fecha_mod = models.DateTimeField(_('fecha modificacion'), auto_now=True, editable=False)
#    usuario = models.ForeignKey(auth.models.User, editable=False)
#    def save(self,force_insert=False, force_update=False):
#        fecha_mod = datetime.now()
#        super(Logueable,self).save(force_insert, force_update)
#    class Meta:
#        abstract = True

#-------------------------------------------------------------------------------

#class LogueableAdmin(admin.ModelAdmin):
#    def save_model(self, request, obj, form, change):
#        if isinstance(obj,Logueable):
#            if not change:
#                obj.usuario = request.user
#        return super(LogueableAdmin,self).save_model(request, obj, form, change)
#    def save_formset(self,request,form,formset,change):
#        def set_user(instance):
#            if isinstance(instance,Logueable):
#                if not change:
#                    instance.usuario = request.user
#            instance.save()
#            #instance.save_m2m()
#            return instance
#        instances = formset.save(commit=False)
#        map(set_user,instances)
#        formset.save_m2m()
#        return instances

#-------------------------------------------------------------------------------


    
