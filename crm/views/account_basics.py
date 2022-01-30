from django.shortcuts import render
from modules.ez_target import get_agent
# Create your views here.
def index(request):
    ip=get_agent(request, src='home')
    print(f'IP: {ip}')
    context = {}
    return render(request, 'pages/home.html', context)


    # <meta charset="utf-8">
    # <meta http-equiv="X-UA-Compatible" content="IE=edge">
    # <meta name="viewport" content="width=device-width, initial-scale=1">
    # <!-- load MUI -->
    # <link href="//cdn.muicss.com/mui-0.7.1/css/mui.min.css" rel="stylesheet" type="text/css" />
    # <script src="//cdn.muicss.com/mui-0.7.1/js/mui.min.js"></script>