from django.http import HttpResponse
from django.template import loader
from .models import Todo

# Create your views here.


def index(request):
    todo_list = Todo.objects.order_by('-due_date')
    output = ', '.join([t.todo_item for t in todo_list])
    template = loader.get_template('hello/index.html')
    context = {
        "todo_list": todo_list,
    }
    print(todo_list, output)
    return HttpResponse(template.render(context, request))
