from flopblog import views
from movie.views import HomeView, MovieList,MovieDetail ,MovieCategory,MovieLanguage , MovieSearch , MovieYear

from django.urls import path


app_name='movie'

urlpatterns = [
   
    path('home/' , HomeView.as_view(),name='home_View'),
    path('movielist/', MovieList.as_view() , name='movie_list'),
    path('category/<str:category>', MovieCategory.as_view() , name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view() , name='movie_language'),
    path('search/', MovieSearch.as_view() , name='movie_search'),
    path('<slug:slug>', MovieDetail.as_view() , name='movie_detail'),
    path('year/<int:year>', MovieYear.as_view() , name='movie_year'),
    # path('create/',Create.as_view(),name='create'),


    


    

]