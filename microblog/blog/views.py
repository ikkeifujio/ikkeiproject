from django.shortcuts import render
from.models import Post

def frontpage(request):
    post=Post.object.all()  #これでmodels.pyとデータベースに接続する
    return render(request,"blog/frontpage.html")


kiminou



        

    

    



