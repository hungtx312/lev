from django.template.response import TemplateResponse

def home_page(request):
    return TemplateResponse(request, 'about.html')

def sign_up(request):
    return TemplateResponse(request, 'sign_up.html')