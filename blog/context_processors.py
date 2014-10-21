from blog.models import Post, Tag, Author


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }


def tags_for_posts(request):
    return {
        'tags_for_posts': Tag.objects.all()
    }


def blog_authors(request):
    return {
        'blog_authors': Author.objects.all()
    }
