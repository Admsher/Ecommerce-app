# Ecommerce App

A dummy application to order products on an online platform.

## Setup Instructions

### 1. Create and Configure the Database

This application uses a MySQL database. Follow these steps to set up and connect your database:

1. **Create a Database:**
   Create a new database in your local MySQL server.

2. **Update Database Configuration:**
   In your Django project's `ecommerce/settings.py`, configure the database settings as follows:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_db',  # Replace with your database name
           'USER': 'root',
           'PASSWORD': 'your_password',  # Replace with your MySQL root password
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }


3.  Apply migrations to set up the database schema :
       python manage.py makemigrations
        python manage.py migrate
4. Create a superuser to access the Django admin panel
5. Navigate to the Django admin panel at: http://127.0.0.1:8000/admin
6. You need to register users (including the superuser) in the Customer model to grant them customer access.
7. Add products to the Product model. These products will be shown on the customer website.
8. Visit the homepage of the store at: http://127.0.0.1:8000/store/store/
9.     Add to Cart: Use the "Add to Cart" button to add products to your cart.
        View Button: The "View" button is currently inactive.
        Cart Navigation: Click the cart logo in the top right to navigate to your cart.
        Checkout: Proceed to checkout if the cart is satisfactory. Use the up and down buttons to adjust product quantities.
        Address Form: Existing users must fill out the address form during checkout. New users will be given new credentials and need to register on the website.

10. The default password for a new user is SHA25678. If this password does not work, change it via the Django admin panel in the user model.
11. To run the application locally, use: python manage.py runserver







 
