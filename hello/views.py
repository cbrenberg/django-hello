from django.shortcuts import render

from .models import Todo

# Create your views here.


def index(request):
    todo_list = Todo.objects.order_by('-due_date')
    output = ', '.join([t.todo_item for t in todo_list])
    context = {
        "todo_list": todo_list,
    }
    print(todo_list, output)
    return render(request, 'hello/index.html', context)
