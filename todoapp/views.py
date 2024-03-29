from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Todo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse  


ITEMS_PER_PAGE = 5

def index(request):
    todos = Todo.objects.all().order_by('pk') 
    # Define the number of items per page
    page = request.GET.get('page', 1)
    per_page = 5
    paginator = Paginator(todos, per_page) 
    print(page)
    # start_index = (int(page) - 1) * per_page
    # end_index = start_index + per_page
    # paginated_todos = todos[start_index:end_index]

    try:
        paginated_todos = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page
        paginated_todos = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g., 9999), deliver the last page
        paginated_todos = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        new_todo = Todo(title=request.POST['title'])
        new_todo.save()
        return redirect('/')
    print("yo",paginated_todos)

    return render(request, 'index.html', {'todos': paginated_todos})

def load_more_todos(request):
    page = request.GET.get('page')
    todos = Todo.objects.all().order_by('pk')   # Query your Todos based on the current page
    paginator = Paginator(todos, ITEMS_PER_PAGE)

    try:
        todo_page = paginator.page(page)
    except EmptyPage:
        return JsonResponse({'error': 'No more data available'})

    todo_data = [{'id': todo.id,'title': todo.title} for todo in todo_page]
    print(todo_data)
    # Return the paginated data as JSON
    return JsonResponse({'todos': todo_data})



def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')