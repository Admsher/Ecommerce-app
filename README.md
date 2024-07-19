# Ecommerce app

.A dummy applicaion to order products on an online platform
.This app is using a mysql database , please craete a database in you local mysql server and connect it via this function in ecommerce/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db',
        'USER': 'root',
        'PASSWORD': 'your_apassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


.0O naviagte to admin panel use http://127.0.0.1:8000/admin
.YOu will have to create a super user to access the admin panel
.You will have to register users(including superuser) in the Customer model for them to get Customer access
.A new user who is not registerdcan also access the website
.You will have to add your products in the Product Model , these will be shown on the customer website later
.To navigate to homepage use http://127.0.0.1:8000/store/store/
.You can add products via using ADd to Cart button
.The View button is inactive
.You can navigate to your cart by pressing the car logo on the top right
.YOu can proceeed to checkout if the cart is satisfactory, use up and down buttons in front of the product to increase/reduce their quantity
.YOu will ave to fill the form for your adresss only if you are a existing user
.For the new user , you will b giving new credentials as well to register in the website
.The default password for  a new user is 'SHA25678'
.If the password doesnt work pease change it via the admin panel in user model.

