from curses import KEY_OPTIONS
from re import template
from turtle import end_fill
from django.db import models

class Post(models.Model):
    title =models.CharField(max_length=255)  #文字格納
    slug =models.SlugField()                #slug 投稿番号
    intro=models.TextField()                #textfield 文字が打つことができるエリア
    body=models.TextField()
    posted_date=models.DateTimeField(auto_now_add=True) #投稿日時

    class ListClass(ListView):
        template_name = 'list.html'
        template_name="list.html" 
        template_item=""

    class CreatePosts
        def change:
        t.timestamps


    



        
        
    
    






