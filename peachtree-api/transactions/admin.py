from django.contrib import admin
from .models import *


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
  pass

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
  pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
  pass
