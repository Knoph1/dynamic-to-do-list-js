from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post, Comment 
from .forms import PostForm, CommentForm
from django.db.models import Q
# Create your views here.
# blog/views.py

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
      user_form = UserUpdateForm(request.POST, instance=request.user)
      if user_form.is_valid():
        user_form.save()
        return redirect('profile')
      else:
           user_form = UserUpdateForm(request.POST, instance=request.user)
           context = {
            'user_form': user_form,
           }
    return render(request, 'blog/profile.html')


class PostListView(ListView):
  model = Post
  template_name = 'blog/base.html' # <app>/<model>_<viewtype>.html
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 5

class PostDetailView(DetailVIew):
  model = Post
  template_name = 'blog/post_detail.html' # Default: <app_name>/<model_name>_detail.html 
  class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post 
    form_class = PostForm
    template_name = 'blog/post_form.html' 
    def form_valid(self, form):
       form.instance.author = self.request.user 
       return super().form_valid(form) 
       
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
  model = Post 
  form_class = PostForm 
  template_name = 'blog/post_form.html' 

  def form_valid(self, form):
     form.instance.author = self.request.user
  return super().form_valid(form)
  
  def test_func(self): 
    post = self.get_object()
  return self.request.user == post.author 
     
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
  model = Post 
  template_name = 'blog/post_confirm_delete.html' 
  success_url = reverse_lazy('post-list')
   
  def test_func(self):
     post = self.get_object() 
  return self.request.user


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

def search(request): 
  query = request.GET.get('q') 
  results = Post.objects.filter( 
    Q(title__icontains=query) | 
    Q(content__icontains=query) | 
    Q(tags__name__icontains=query) 
  ).distinct() 
  return render(request, 'blog/search_results.html', {'results': results, 'query': query})