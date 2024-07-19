from django.urls import path
from . import views
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['Ecommerce']
collection = db['Users']
# print(collection.find()['user'])


urlpatterns = [
    # path('navbar/', views.home, name='navbar'),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]

