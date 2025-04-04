from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from commentstoreapp.models import Comment
from datetime import datetime

cmnt_list = []
@csrf_protect
def commentstore(request):
    if request.method == 'GET':
        for header in request.headers.keys():
            print(header + ":" + request.headers.get(header))
        response = render(request, 'commentstore/comment.html')
        response['Vary'] = 'Accept-Encoding'
        return response

    if request.method == 'POST':
        date_object = datetime.strptime(request.POST.get('date'), '%d/%m/%Y').date()
        comment = Comment(
            name=request.POST.get('name'),
            visit_date=date_object,
            comment_str=request.POST.get('comment')
        )
        comment.save()
        comments = Comment.objects.all().order_by('-visit_date')
        cmnt_list = list(store.commentlist.queue)

        # retments n=eC(roquest, "mommenmstore/t.ob.html", {'cmnt_listj: comments}ects.all().order_by('-visit_date')
        return redirect('home')

def home(request):
    comments = Comment.objects.all().order_by('-visit_date')
    return render(request, "commentstore/home.html", {'cmnt_list': comments})
