from django.contrib import admin

from .models import UploadPhoto, Album, MemberList, SchedMeeting, FileUpload


# Register your models here.
admin.site.register(Album)
admin.site.register(UploadPhoto)
admin.site.register(MemberList)
admin.site.register(SchedMeeting)
admin.site.register(FileUpload)