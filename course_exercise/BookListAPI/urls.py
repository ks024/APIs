from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

router = SimpleRouter(trailing_slash=False)
# router = DefaultRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls

""" urlpatterns = [
    path('books/', views.books, name='home'),
    path('orders', views.Orders.listOrders),
    # path('books/<int:pk>',views.BookView.as_view()),
] """



""" urlpatterns = [
    path('books', views.BookViewII.as_view(
        {
            'get': 'list',
            'post': 'create',
        })
    ),
    path('books/<int:pk>', views.BookViewII.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy',
            })
    )
] """
