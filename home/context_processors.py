from datetime import datetime

def year_context(request):
    return {
        'year': datetime.now().year
    }