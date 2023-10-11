import uuid

from django.db import models


class Account(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=100)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    pin = models.PositiveSmallIntegerField(default=None, null=True, blank=False)


class Transaction(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False, related_name="from_account")
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, blank=False, related_name="to_account")
