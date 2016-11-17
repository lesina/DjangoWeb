from video.models import Category
from video.forms import SearchForm

def coreContextProcessor(request):
    return {"categories" : Category.get_categories(), "search_form" : SearchForm(request.GET)}