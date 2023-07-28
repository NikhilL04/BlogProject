from django.shortcuts import render,get_object_or_404
from blogapp.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.mail import send_mail
from blogapp.forms import EmailSendingForm,CommentsForm,LoginForm

# Create your views here.
def test_list(request):

    return render(request,'blogapp/test.html')

def post_list(request):
    post_list=Post.objects.filter(status__exact='published')


    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')# page is a predefined word
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blogapp/post_list.html',{'post_list':post_list})

def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    comments=post.comm.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True

    else:
        form=CommentsForm()
    return render(request,'blogapp/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})
def mail_sending_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False

    if request.method=='POST':
        form=EmailSendingForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            message = post.body
            subject=post.title
            send_mail(subject,message,'pythondjango84@gmail.com',[cd['Email']])
            sent=True

    else:
        form=EmailSendingForm()
    return render(request, 'blogapp/mail.html',{'form':form,'post':post,'sent':sent})

def login_view(request):
    csubmit=False
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            form_save=form.save(commit=False)
            form_save.save()
            csubmit=True

    else:
        form=LoginForm()
    return render(request,'blogapp/login.html',{'form':form,'csubmit':csubmit})
