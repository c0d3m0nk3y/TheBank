from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import TemplateView, View

from bank.models import Account, Transaction


class IndexView(TemplateView):
    template_name = "bank/index.html"


class LoginView(View):
    template_name = "bank/login.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {},
        )


class AccountView(View):
    template_name = "bank/account.html"

    def get(self, request, id):
        account, created = Account.objects.get_or_create(pk=id)
        return render(
            request,
            self.template_name,
            {
                'account': account,
            },
        )


class SendForm(forms.Form):
    from_account = forms.UUIDField()
    pin = forms.IntegerField(min_value=0, max_value=9999)
    to_account = forms.UUIDField()
    amount = forms.IntegerField(min_value=1)


class SendView(View):
    template_name = "bank/send.html"

    def get(self, request):
        form = SendForm()

        return render(
            request,
            self.template_name,
            {
                'po': request.POST,
                'ge': request.GET,
                'form': form,
            },
        )

    def post(self, request):
        from_account = get_object_or_404(Account, uuid=request.POST['from_account'])
        to_account = get_object_or_404(Account, uuid=request.POST['to_account'])

        if from_account == to_account:
            return HttpResponseRedirect(reverse('bank:home'))

        pin = int(request.POST['pin'])

        # Passwords of "zero" are unsafe
        if from_account.pin is None:
            from_account.pin = pin
            from_account.save()

        if from_account.pin != pin:
            return HttpResponseRedirect(reverse('bank:home'))

        amount = int(request.POST['amount'])

        if from_account.balance < amount:
            return HttpResponseRedirect(reverse('bank:home'))

        from_account.balance -= amount
        from_account.save()
        to_account.balance += amount
        to_account.save()

        Transaction.objects.create(
            from_account=from_account,
            to_account=to_account,
            amount=amount,
        )

        return HttpResponseRedirect(reverse('bank:track'))


class TrackView(View):
    template_name = "bank/track.html"

    def get(self, request):
        transactions = Transaction.objects.order_by('-created_on')
        return render(
            request,
            self.template_name,
            {
                'transactions': transactions,
            },
        )


