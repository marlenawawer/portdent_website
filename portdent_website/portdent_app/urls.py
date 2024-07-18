from django.urls import path, include
from portdent_app import views



app_name = 'portdent_app'

urlpatterns = [
    path('blog/', views.Blog.as_view(), name='blog'),
    path('article/<int:pk>', views.PostDetails.as_view(), name='post-detail'),
    path('contact/', views.contact, name='contact'),
    path('addpost', views.addpost, name='addpost'),
    path('article/update/<int:pk>', views.UpdatePost.as_view(), name='update-post'),
]