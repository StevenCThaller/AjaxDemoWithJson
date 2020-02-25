from django.urls import path
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path('', RedirectView.as_view(url='/snakes')),
    path('snakes', views.index),
    path('snakes/add', views.addSnake),
    path('snakes/all', views.allSnakes),
    path('snakes/new', views.snakeForm),
    path('snakes/<int:snake_id>', views.oneSnake),
    path('snakes/delete/<int:snake_id>', views.deleteSnake),
    path('ajax/snakes/<int:snake_id>', views.oneSnakeAjax),
    path('ajax/snakes/all', views.allSnakesAjax),
    path('ajax/snakes/form', views.snakeFormAjax),
    path('ajax/snakes/add', views.addSnakeAjax),
    path('ajax/snakes/delete/<int:snake_id>', views.deleteSnakeAjax)
]
