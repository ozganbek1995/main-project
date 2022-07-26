
from django.urls import path
from .api_views import *
from .new_api_views import *
from django.shortcuts import render


def doc(request):
    return render(request, 'doc.html')






urlpatterns = [
    path('shop/<int:pk>/', ShopDetailView),
    path('shops/', ShopsView),

    path('shops/<int:pk1>/<int:pk2>/', ShopFilterView),
    path('shops/<int:pk1>/', ShopFilterView),

    

    # path('regions/<int:pk>/', TumanlarView)
]

# New
urlpatterns += [
    path('shops/get/', GetShopsView), #
    path('shops/post/', PostShopsView), #
    path('shops/add-member/', AddMemberView), #
    path('shops/members-list/<int:shop_pk>/', MembersListView),
    path('shops/products-list/<int:pk>/', ProductsListView),
    path('regions/', RegionsApiView),
    path('doc/', doc),
    path('geo/<str:lat>/<str:lon>/', GeoLocationApi),
    path('users/get/', GetUsersView),
    path('users/post/', CreateUserView),
    path('user/<int:id>/put/', PostUserUpdateView),
    path('user-test/<str:phone>/', TestUserView),
    path('shop/<int:pk>/get/', ShopDetailView),
    path('filter-by-user/<int:pk>/', FilterByUser),
    path('products/get/<int:pk>/', ProductView),
    
]
    

#     path('shops/<int:pk>/', ),
#     path('shops/<int:pk>/<int:pk>/', ),

#     path('users/get/', ),
#     path('users/post/', ),

#     path('users-test/<int:phone>/', ),

#     path('regions/<int:pk>/', ),

