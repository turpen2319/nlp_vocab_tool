from django.urls import path #need path func to define each route
from . import views #need thees to map routes to view funcs/classes (kinda like controllers)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('lists/', views.lists_index, name='lists_index'),
    path('lists/<int:list_id>', views.list_details, name='details'),
    path('lists/<int:list_id>/add_word', views.add_word, name='add_word'),
    path('lists/create/', views.ListCreate.as_view(), name='lists_create'), #this will show a form and let users create a new list
    path('lists<int:pk>/update', views.ListUpdate.as_view(), name='lists_update'),
    path('lists/<int:pk>/delete', views.ListDelete.as_view(), name='lists_delete'),
    #IMPORTANT: by convention, CBVs that work with individual model instances will expect to find a named parameter of pk.
    #This is why we don't use list_id like we did in our details route
    

    path('students/', views.StudentList.as_view(), name='students_index'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='students_detail'),
    path('students/create/', views.StudentCreate.as_view(), name='students_create'),
    path('students/<int:pk>/update/', views.StudentUpdate.as_view(), name='students_update'),
    path('students/<int:pk>/delete/', views.StudentDelete.as_view(), name='students_delete'),
    # path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy')
]