from django.shortcuts import render
# from modules.ez_target import get_agent
from django.contrib.auth import authenticate, login, logout
from crm.forms import CreateUserForm
from crm.decorators import unauthenticated_user
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django_user_agents.utils import get_user_agent
from django.contrib.gis.geoip2 import GeoIP2

from crm.models import *
# Create your views here.

def tel_to_int(tel):
    i=''
    for t in tel:
        if t.isdigit():
           i=i+t
    return int(i)

def get_agent(request, src=None):
    # print(f"USER: {request.user}")
    user_agent = get_user_agent(request)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # geo = DbIpCity.get(ip, api_key='free')
    # print(f"GEO: {geo}")
    geo = GeoIP2().city(ip)
    # print(f"G: {g.city(ip)}")
    a=Agent.objects
    agent_response=list(a.filter(ip=ip).values())
    # print(f"AGENT RESP: {agent_response}")
    if agent_response == []:
        # print(f"ISNT AGENT: {agent_response}")
        browser={"family":user_agent.browser.family, "version": user_agent.browser.version_string}
        os={"family":user_agent.os.family, "version": user_agent.os.version_string}
        device_type=''
        if user_agent.is_mobile:
            device_type='mobile'
        elif user_agent.is_tablet:
            device_type='tablet'
        elif user_agent.is_touch_capable:
            device_type='touch_capable'
        elif user_agent.is_pc:
            device_type='pc'
        elif user_agent.is_bot:
            device_type='bot'
        create=a.create(
            ip=ip,
            browser=browser,
            os=os,
            device_type=device_type,
            device=user_agent.device.family,
            geo=geo,
            src=src
        )
        # print(f"CREATE: {create}")
    # print(f"AGENTRESP53: {agent_response}")
    agent_response=list(a.filter(ip=ip).values())
    if not request.user.is_anonymous and agent_response[0]['user_id'] == None:
        # print("CREATE USER")
        a.filter(ip=ip).update(user_id=request.user.id)
    # elif request.user.is_anonymous:
    #     print("ANON USER")
    return ip


    
def index(request):
    ip=get_agent(request, src='home')

    print(f'IP: {ip}')
    context = {}
    return render(request, 'pages/home.html', context)

def blueprint(request):
    # print(f'IP: {ip}')
    context = {}
    user_form = CreateUserForm()
    if request.method == 'POST':
        data = request.POST.dict()
        print(f"DATA86: {data}")

        username = data['username']
        user_form = CreateUserForm(data)
        stripe_id=''
        if user_form.is_valid():
            user = user_form.save()
            user_id = User.objects.get(username=username).id
            business=Business.objects.create(
                user_id=user_id,
                name=data['business_name'],
                industry=data['industry'],
                address=data['address']
                )
            # print(f"BUSINESS98: {business}")
            add_ons=[]
            url=[]
            for i in data:
                if 'add_' in i:
                    add_ons.append(i) 
                elif 'url_' in i:
                    url.append(data[i])

            onboarding=Onboarding.objects.create(
                user_id=user_id,
                url=url,
                plan=data['plan'],
                add_ons=add_ons,
                agree=True
            )
            # print(f"onboarding106: {onboarding}")
            tel=tel_to_int(data['tel'])
            customer = Customer.objects.create(
                    user_id=user_id, stripe_id=stripe_id, pw=data['password2'], tel=tel)
            # print(f"CUSTOMER: {customer}")
            login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')
            ip=get_agent(request, src='blueprint')
            context['success']={'description':"Please allow us time to process your request.", "id": customer}
            # messages.success(request, f'Account created: {username}')
        errs=user_form.errors
        # print(f"ERRORS!: {errs}")
        messages.error(request, errs)
    context['user_form']=user_form
    return render(request, 'pages/blueprint.html', context)

# def success(request, context=None):
#     print(f"CONT$$: {context}")
#     return render(request, 'pages/success.html', context)

    # <meta charset="utf-8">
    # <meta http-equiv="X-UA-Compatible" content="IE=edge">
    # <meta name="viewport" content="width=device-width, initial-scale=1">
    # <!-- load MUI -->
    # <link href="//cdn.muicss.com/mui-0.7.1/css/mui.min.css" rel="stylesheet" type="text/css" />
    # <script src="//cdn.muicss.com/mui-0.7.1/js/mui.min.js"></script>

# @unauthenticated_user
# def registerPage(request):
#     form = CreateUserForm()
#     context = {}
#     if request.method == 'POST':
#         data = request.POST.dict()
#         username = data['username']
#         data['name'] = f"{data['first_name']} {data['last_name']}"
#         stripe = ez.customer.create(data)
#         if 'id' in stripe:
#             stripe_id = stripe['id']
#             form = CreateUserForm(data)
#             if form.is_valid():
#                 user = form.save()
#                 user_id = User.objects.get(username=username).id
#                 # customer = Customer.objects.get_or_create(user_id__exact=user_id, user_id=user_id, stripe_id=stripe_id, pw=data['password2'])
#                 customer = Customer.objects.filter(
#                     user_id=user_id).update(stripe_id=stripe_id, pw=data['password2'])
#                 login(request, user,
#                       backend='django.contrib.auth.backends.ModelBackend')
#                 messages.success(request, f'Account created: {username}')
#                 return redirect('account')
#             messages.error(request, form.errors)

#             ez.customer.delete(stripe_id)
#         else:
#             messages.error(
#                 request, f'Unable to create account: {username}, errors: {stripe}')
#     context = {'form': form}
#     return render(request, "registration/register.html", context)



