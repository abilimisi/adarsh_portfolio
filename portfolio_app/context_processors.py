from .models import Link

def work_details_processor(request):
    links = Link.objects.all().last()
    return {'links': links}
