
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.test),
    path('doc_sorpbd/',views.render_doc_sorpbd),
    path('a/',views.render_doc_sorpbd),
    path('create_doc_sorpbd/', views.create_doc_sorpbd, name='create_doc_sorpbd'),
    path('create_evm/', views.create_evm, name='create_evm'),
    path('autor/', views.get_autor, name='create_doc_sorpbd'),
    path('create_autor/', views.create_autor, name='create_autor'),
    path('pravo/', views.get_pravo, name='get_pravo'),
    path('delete_doc_sorpbd/<int:pk>/', views.delete_doc_sorpbd, name='delete_doc_sorpbd'),
    path('list_SoftwareRegistrationCertificate/',views.list_SoftwareRegistrationCertificate),


]
