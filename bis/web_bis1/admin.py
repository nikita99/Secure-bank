from django.contrib import admin
from .models import Signup, ItemInfo, TransactionInfo

# Register your models here.

admin.site.register(Signup)
admin.site.register(ItemInfo)
admin.site.register(TransactionInfo)
