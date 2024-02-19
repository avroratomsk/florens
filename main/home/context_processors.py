from home.models import BaseSettings 
 
def load_settings(request):
    return {'site_settings': BaseSettings.load()}