from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is no items in your bag at the moment")
        return redirect(reverse('product'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PdVphRo27LVDAwk7ck0TUeNf8VH6XdZUEe9eccn3ZBCfm0ayPRNKSLSW9GtHu8wvikMHVGUCZxsFGWSzXJ5ppjl00FwZtFUcm',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
