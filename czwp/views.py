from django.shortcuts import render_to_response
from django.template import RequestContext


def my_404_view(request):
    #return render(request, 'blog/404.html')
    response = render_to_response('blog/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
