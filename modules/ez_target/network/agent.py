from django_user_agents.utils import get_user_agent
from django.contrib.gis.geoip2 import GeoIP2

def get_agent(request, src=None):
    context={}
    user_agent = get_user_agent(request)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    geo = GeoIP2().city(ip)
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
    context={"ip":ip,"geo":geo,"browser":browser,"device_type": device_type,"os":os}
    return context