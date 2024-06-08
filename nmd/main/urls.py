
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.test),
    path('a',views.render_doc_sorpbd),
    path('create_doc_sorpbd/', views.create_doc_sorpbd, name='create_doc_sorpbd'),


]
