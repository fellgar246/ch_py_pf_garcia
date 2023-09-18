from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, PostEditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpRequest, HttpResponseRedirect

# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else: 
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('ArticleDetail', args=[str(pk)]))

def HomeView(request, start=1):
    direction = request.GET.get("direction")
    start = int(start)

    paginate_by = 3
    begin = start * paginate_by
    final = (start + 1) * paginate_by

    total_posts = Post.objects.count()  # Obtener el total de publicaciones
    posts_page = Post.objects.all().order_by('-post_date')[begin:final]
    category_menu = Category.objects.all()

    if direction == "next" and final < total_posts:
        start += 1
    elif direction == "before" and start > 0:
        start -= 1
    elif direction != "next" and direction != "before":
        start = 0

    begin = start * paginate_by
    final = (start + 1) * paginate_by
    posts_page = Post.objects.all().order_by('-post_date')[begin:final]

    context = {
        'posts_page': posts_page,
        'category_menu': category_menu,
        'current_page': start,
    }

    return render(request, 'home.html', context)

def CategoryListView(request):
    category_menu_list = Category.objects.all()
    return render(request, 'category_list.html',{'category_menu_list': category_menu_list})

def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories.replace('-',' '))
    return render(request, 'categories.html', {'categories': categories.title().replace('-',' '),'category_posts': category_posts })

class ArticleDetailView(DetailView):
    model=Post
    template_name= 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["category_menu"] = category_menu
        context["total_likes"]= total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form) 

    success_url = reverse_lazy('Home')

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('Home')
 
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    
def About(req):
    return render(req, "about.html")

def handleNotFound(request, exception):
    return render(request, 'not_found.html')
