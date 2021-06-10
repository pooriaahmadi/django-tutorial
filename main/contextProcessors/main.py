import config

def index(request):
    context = {}
    context['website_title'] = config.website_title
    return context