from django.conf import settings

def name(request):
    return {'SITE_NAME': settings.SITE_NAME,}