from django.contrib import admin

from .models import MemberBoxTag
from .models import MemberShelfTag
from .models import Member

# Register your models here.

class MemberBoxTagAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User data', {'fields': ['member_id', ]}),
        ('Box data', {'fields': ['box_number', 'print_date',  'comment', 'visible']}),
    ]
    list_display = ('member_id', 'box_number', 'visible')
    

class MemberShelfTagAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'visible')

class MemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'box_num')

admin.site.register(Member, MemberAdmin)
admin.site.register(MemberBoxTag, MemberBoxTagAdmin)
admin.site.register(MemberShelfTag, MemberShelfTagAdmin)
