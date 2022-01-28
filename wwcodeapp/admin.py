from django.contrib import admin

# Register your models here.
from .models import Topic,Answertable
class TopicAdmin(admin.ModelAdmin):
    #topic_display = ('Question','date_added')
    pass
class AnswertableAdmin(admin.ModelAdmin):
    pass
admin.site.register(Topic,TopicAdmin)
admin.site.register(Answertable,AnswertableAdmin)
