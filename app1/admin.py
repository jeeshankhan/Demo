from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,upload,manuscript_upload
class AccountAdmin(UserAdmin):
    list_display =('email','username','last_login','is_admin','is_staff','is_reviewer','is_editor','is_publisher')
    search_fields=('email','username')
    readonly_fields = ('last_login',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account,AccountAdmin)
admin.site.register(upload)
admin.site.register(manuscript_upload)