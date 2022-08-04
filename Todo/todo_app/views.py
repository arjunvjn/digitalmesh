from django.shortcuts import render,redirect
from  .models import Todotable
from django.http.response import JsonResponse
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    todo_list=Todotable.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(todo_list, 5)
    todos = paginator.page(page)
    # except Paginator.PageNotAnInteger:
    #     todos = paginator.page(1)
    # except Paginator.EmptyPage:
    #     todos = paginator.page(paginator.num_pages)
    return render(request,'home.html',{'todo_list':todos})

def create_todo(request):
    if request.method=='POST':
        Todotable.objects.create(name=request.POST['name'],date=request.POST['date'],repeat=request.POST.get('repeat','All'),desc=request.POST['desc'])
        return redirect('/index/')
    else:
        return render(request,'add_task.html',{'url':'/create-task/'})

def update_todo(request,id=-1):
    if id!=-1:
        todo=Todotable.objects.get(pk=id)
        if request.method=='POST':
            todo.name=request.POST['name']
            todo.date=request.POST['date']
            todo.repeat=request.POST.get('repeat','All')
            todo.desc=request.POST['desc']
            todo.save()
            return redirect('/index/')
        else:
            return render(request,'add_task.html',{'url':'/update-task/'+str(id)+'/','todo':todo})
    return redirect('/index/')

def delete_todo(request):
    if request.method=='GET':
        print('hello')
        try:
            id=int(request.GET.get('id'))
            print(id)
            Todotable.objects.filter(pk=id).delete()
            return JsonResponse({'msg':'Success'})
        except:
            return JsonResponse({'msg':'Error'})

def filter_repeat(request):
    filter = request.GET.get('filter', 'All')
    todo_list=Todotable.objects.filter(repeat=filter)
    todos=[]
    for i in todo_list:
        todos.append({'name':i.name,'date':i.date,'repeat':i.repeat,'desc':i.desc})
    return JsonResponse({'todo_list':todos})

def search_todo(request):
    if request.method=='POST':
        try:
            todo_list=Todotable.objects.filter(name__contains=request.POST['search'])
            return render(request,'',{'todo_list':todo_list})
        except:
            return redirect('/index/')
    return redirect('/index/')