
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.main_page),
    path('doc_sorpbd/',views.render_doc_sorpbd),
    path('a/',views.render_doc_sorpbd),
    path('create_doc_sorpbd/', views.create_doc_sorpbd, name='create_doc_sorpbd'),
    path('create_evm/', views.create_evm, name='create_evm'),
    path('autor/', views.get_autor, name='create_doc_sorpbd'),
    path('create_autor/', views.create_autor, name='create_autor'),
    path('pravo/', views.get_pravo, name='get_pravo'),
    path('delete_doc_sorpbd/<int:pk>/', views.delete_doc_sorpbd, name='delete_doc_sorpbd'),
    path('delete_doc_soft/<int:pk>/', views.delete_doc_soft, name='delete_doc_soft'),
    
    path('list_SoftwareRegistrationCertificate/',views.list_SoftwareRegistrationCertificate),

    path('registrate/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('exit/', views.exit_view, name='exit'),
    path('user_profile/<str:pk>/', views.user_profile, name='user_profile'),
    path('autor_get/<int:pk>/', views.autor_get, name='autor_get'),
    path('docSorp_detail/<int:pk>/', views.DocSorp_detail, name='DocSorp_detail'),
    path('softwareregistrationertificate_detail/<int:pk>/', views.SoftwareRegistrationCertificate_detail, name='softwareRegistrationCertificate_detail'),
    path('add_pravo/',views.add_owner),

    path('list_artical_in_sbor/',views.render_article_list),
    path('delete_artical_in_sbor/<int:pk>/', views.delete_artical_in_sbor, name='delete_artical_in_sbor'),
    
    #тут у нас все связаное с десертациями
    path('list_dissertation/',views.get_Dissertation),
    path('delete_dissertation/<int:pk>/', views.delete_Dissertation, name='delete_dissertation'),
    path('add_dissertation/',views.create_dissertation),
    path('dissertation_get/<int:pk>/', views.Dissertation_detail, name='dissertation_get'),
   


    path('search_view/', views.search_view, name='search_view'),
    path('admin/', views.admin, name='admin'),

    path('ch_type/<int:pk>/', views.ch_type, name='ch_type'),


    path('edit_doc_sorpbd/<int:pk>/', views.edit_doc_sorpbd, name='edit_doc_sorpbd'),

    
]
