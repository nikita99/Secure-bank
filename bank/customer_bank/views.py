import datetime
import hashlib

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
# Create your views here.
from django.template import RequestContext

from customer_bank.forms import CreateAccountForm, Loginform
from customer_bank.models import Accounts


def main_view(request):
    return render(request, 'customer_bank/mainpage.html', {})


def make_account_list(request):
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            # print(request.POST.get('password'))
            user = User(username=request.POST.get('account_no'), password=make_password(request.POST.get('password')),
                        email=request.POST.get('email_id'), first_name="none", last_name="none")
            user.save()
            print(str(user))
            obj = Accounts(user=user,
                           account_no=request.POST.get('account_no'),
                           # account_date = request.POST.get('account_date'),
                           )
            obj.save()
            # post.user=user
            # post.save()
            return redirect('/bank/create_account_success/', {})

    else:
        form = CreateAccountForm()

    return render(request, 'customer_bank/make_account.html', {'form': form})


def create_account_success_list(request):
    return render(request, 'customer_bank/create_account_success.html', {})


def login_bank_list(request):

    account = request.POST.get('acct')
    price = request.POST.get('price')
    item = request.POST.get('item')
    license = request.POST.get('license')
    m = request.POST.get('m')
    company_name = ''
    # hashing recieved data
    #hashing
    #account2=int(account)
    # account1 = account.encode('utf-8')
    # salt = "a0b0c0d0"
    # salt1 = salt.encode('utf-8')
    # n=(hashlib.sha512(salt1+account1).hexdigest())#.encode('utf-8')
    # print(n)
    # print(m)
    # m1 = m.encode('utf-8')
    # print(m1)
    #hashing
    #
    # n = hashlib.sha512(account1 + salt1).hexdigest()
    # hashlib
    # obj=Signup.objects.filter(user=request.user)[0]
    # obj.license_id
    password = ''
    # if (m1 != n):
    #     return redirect('/bank/corrupt/', {})

    if request.POST:
        # print("inside post")

        request.session['curr_license'] = license
        request.session['curr_item'] = item
        account_no = request.POST.get('account_no')
        password = request.POST.get('password')
        # print(company_name + password)
        # accountint=int(account)

        # if (m != n):
        #       return redirect('/bank/corrupt/', {})

        user = authenticate(username=request.POST.get('account_no'), password=password)
        if user is not None:
            # if user.is_active:
            login(request, user)
            print("You're successfully logged in!")
            obj1 = Accounts.objects.filter(account_no=account_no)[0]  # =license_id1)[0]
            bal = obj1.balance
            if (bal >= int(price)):
                bal = bal - int(price)
                # obj = Accounts(user=user,
                #          account_no = account_no,
                #          balance=bal
                #          #account_date = request.POST.get('account_date'),
                #          )
                # obj.save()
                obj1.balance = bal
                obj1.save()
                obj3 = Accounts.objects.filter(account_no=9999)[0]  # adding money to merchants account
                merchant_bal = obj3.balance
                merchant_bal = merchant_bal + int(price)
                obj3.balance = merchant_bal
                obj3.save()
                # obj2 = Accounts(user=user,
                #          account_no = 9999,
                #          balance=merchant_bal
                #          #account_date = request.POST.get('account_date'),
                #          )
                # obj2.save()

                # return render(request,'customer_bank/transaction.html',locals(),context_instance=RequestContext(request))
                return redirect('/bank/transaction/', {})
            else:
                return redirect('/bank/transaction_fail/', {})

                # else:
                #     state = "Your account is not active, please contact the site admin."
        else:
            state = " Your company_name and/or password were incorrect."
    return render(request, 'customer_bank/login_bank.html', locals(), context_instance=RequestContext(request))


    # return render_to_response('customer_bank/login_bank.html',locals(),context_instance=RequestContext(request))
    # return render_to_response('customer_bank/login_bank.html', {'form': Loginform()}, context_instance=RequestContext(request))


def transaction_list(request):
    if request.method == "POST":
        item_name = request.session.get('curr_item')
        license_id = request.session.get('curr_license')
        obj3 = Accounts.objects.filter(user=request.user)[0]
        context = {"acct": obj3.account_no, "status": 1, "item1": item_name, "license1": license_id}  # , "price":price}
        # context = {"acct":obj3.account_no, "status":1, "item1":"clothing", "license1":2828}
        print("proceeding for transaction")
        return render_to_response('customer_bank/redirect_bis.html',context, context_instance=RequestContext(request))

    else:
        # return render(request, 'customer_bank/transaction.html', {})
        # time=datetime._format_time()
        obj4 = Accounts.objects.filter(user=request.user)[0]
        return render_to_response('customer_bank/transaction.html',locals(), context_instance=RequestContext(request))



def transaction_fail_list(request):
    return render(request, 'customer_bank/transaction_fail.html', {})


def corrupt_list(request):
    return render(request, 'customer_bank/corrupt.html', {})
