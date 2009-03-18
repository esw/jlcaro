from django.contrib import admin
from django.utils.translation import ungettext, ugettext_lazy as _
from django.http import HttpResponseRedirect, Http404
from django.conf.urls.defaults import patterns, url
from chronograph.models import Job, Log

try:
    from batchadmin.admin import BatchModelAdmin as ModelAdmin
except ImportError:
    from django.contrib.admin import ModelAdmin

class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'next_run', 'last_run', 'frequency', 'params', 'get_timeuntil',)
    list_filter = ('frequency', 'disabled',)
    
    fieldsets = (
        (None, {
            'fields': ('name', ('command', 'args',), 'disabled',)
        }),
        ('Frequency options', {
            'classes': ('wide',),
            'fields': ('frequency', 'next_run', 'params',)
        }),
    )
    
    def run_job_view(self, request, pk):
        """
        Runs the specified job.
        """
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404
        job.run(save=False)
        request.user.message_set.create(message=_('The job "%(job)s" was run successfully.') % {'job': job})        
        return HttpResponseRedirect(request.path + "../")
    
    def get_urls(self):
        urls = super(JobAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^(.+)/run/$', self.admin_site.admin_view(self.run_job_view), name="admin_chronograph_job_run")
        )
        return my_urls + urls

class LogAdmin(ModelAdmin):
    list_display = ('job_name', 'run_date',)
    search_fields = ('stdout', 'stderr', 'job__name', 'job__command')
    date_hierarchy = 'run_date'
    
    def job_name(self, obj):
      return obj.job.name
    job_name.short_description = _(u'Name')

admin.site.register(Job, JobAdmin)
admin.site.register(Log, LogAdmin)