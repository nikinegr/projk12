from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, ProjectForm, TaskCreateForm, TestForm
from django.contrib.auth import login, authenticate
from .models import Project , Task, User
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, FormView, TemplateView
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from pathlib import Path
from django.core.files import File
from .serializers import UserSerializer
from .models import Post
from .forms import PostForm
from django.db.models import Q


class qrange(CreateView):
    template_name = "qrange.html"
    form_class=['email pasword']
    success_url = reverse_lazy('home')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User(username=name, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'home.html', context)


class Registration (CreateView):
    template_name = 'registration.html'
    model = User
    #fields = ['username', 'email', 'password1', 'password']
    form_class = RegistrationForm
    success_url = reverse_lazy('/home')


class LoginPage (LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user=True


class Create_project (CreateView):
    template_name = 'project_create.html'
    form_class = ProjectForm
    success_url = reverse_lazy('home')



def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/login')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'home.html', context)


def home (request):
    projects = Project.objects.all()
    context = {'projects': projects }
    return render(request, 'home.html', context)


class Home (ListView):
    template_name = 'home.html'
    model = Project
    paginate_by = 1
    #context object name 'projects'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        context['pages'] = len(projects)
        return context


def project(request):
    id = request.kwargs['id']
    project = Project.object.get(id=id)
    tasks = Task.object.filter(project=project)


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            project = Project(name=name)
            project.save()
            return redirect('/')
    else:
        form = ProjectForm()
        return render(request, 'project_create.html', {'form': form})


def project(request, **kwargs):
    project = Project.objects.get(id=kwargs['id'])
    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            status = form.cleaned_data['status']
            deadline = form.cleaned_data['deadline']
            task = Task(text=text, status=status, deadline=deadline,project=project)
            task.save()
            return redirect('/')
    else:
        tasks = Task.objects.filter(project=project)
        form = TaskCreateForm()
        context = {'fore': form, 'tasks': tasks, 'project': project}
        return render(request, 'projects.html', context)


class Projects(CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = Project
    success_urt = reverse_lazy('home')


def edit_project(request, **kwargs):
    project = Project.objects.get(id=kwargs['id'])
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            project.name = name
            project.save()
            return redirect('/')
    else:
        form = ProjectForm()
        return render(request, 'project create.html', {'form', form})


class ProjectEditPage(UpdateView):
    model = Project
    template_name = 'project_edit.html'
    form_class = ProjectForm
    success_url = reverse_lazy ('/')


class FormPage (FormView):
    template_name = 'form.html'
    form_class = TestForm
    success_url = reverse_lazy()

    def form_valid (self, form):
        response = HttpResponse()
        response.set_cookie('name', form.cleaned_data['name'])
        return super().form_valid(form)



class TestPage(TemplateView):
    template_name = 'test.html'


    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, sate=False)


    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         task = Project.objects.filter(projecttask=project)
         projects = Project.objects.get(id=self.kwargs['id'])
         context['tasks'] = task
         context['project'] = projects
         return context


    def post(self, request):
         data = request.POST
         print(data['test'])
         return JsonResponse({'resp': 'OK'}, safe=False)


    def post(self, request, wargs):
        data = request.POST
        if len(data.keys())== 5:
            project = Project.objects.get(id=self.kwargs["10"])
            task = Task(text=data['text'])
            task.save()
            return JsonResponse({"resp:OK"})
        elif len(data.keys()) == 2:
            task = Task.ojects.get(id=int(data['id']))
            resp = render_to_string('edit_form.html', {'form': TaskCreateForm(initial={'name': task.name,
                                                                                       'deadline':task.deadline,
                                                                                        'status': task.status})})
            return JsonResponse (resp, safe=False)




class ProjectPage(TemplateView):
    template_name='project.html'


    def get_success_url(self):
        return f'/project/{self.kwargs["id"]}'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        project = Project.objects.get(id=self.kwargs['id'])
        context['project'] = project
        context['tasks'] = Task.objects.filter(project-project)
        context['form'] = TaskCreateForm()
        return context


    def post(self, request, **kwargs):
        data = request.POST
        project = Project.objects.get(id=self.kwargs['id'])
        task = Task(text=data['text'],status=data['status'],project=project,deadline=data['deadline'])
        task.save()
        return JsonResponse({ 'resp': 'OK'})


    def post(self, request):
        data = request.POST
        resp = render_to_string('response.html', {'name': data['name'],'email':data['email'],'password':data['password']})
        return JsonResponse (resp, safe=False)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def search_users(request):
    query = request.GET.get('q')
    users = User.objects.filter(Q(usernameicontains=query) | Q(first_nameicontains=query) | Q(last_name__icontains=query))
    return render(request, 'search_users.html', {'users': users})


