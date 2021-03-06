# About this site.

We were presented with a task to reflect what we have learned about Python and Django and enabling CRUD functions.
I took the opportunity to create a E-comerce websie where users can purchase healthy food items.
The website is programmed with the ability to allow a consumer/user to search for their favourite healthfood , add it to the cart and purchase. The consumer 
can also create reviews, delete reviews and see other reviews.
There is also a function where an admin can log in and perform CRUD on the products either in the backend or from the frontend. Ths feature is only available to Admin or SuperUser.

![picture](/static/images/screenshot.png)

To test the Admin user, plese use the following login credentials.

ADMIN 

username: Admin
password:admin12345

 Public User

username:Uncle Roger
password: haiyaa12345


# Demo 

A demo of the page can be seen [here](https://healthfoodmart.herokuapp.com/) on this link.

# Programmig Languages used
1. HTML
2. CSS
3. Python
4. Javascript

# Features

The overall website's look is achieved as planned. Users are able to search and purchase their favourite healthfood , add to cart, purchase via a credit card, create reviews and leave reviews.

The admin / superuser is able to update, delete, create new food
items leave a feedback and perform the same functions the user does.

# Features left to implement

The future plans for this website is to add discount and coupon popues for the past consumers.

There are also plans to increase the Emart database and make the site searchable by producer and price.

# Deployment

The website was deployed on Heroku and can be seen [here](https://healthfoodmart.herokuapp.com/)

The following steps were taken to successfully deploy the app

1) Install the fllowing dependencies
pip3 install gunicorn
pip3 install psycopg2
pip3 install Pillow
pip3 install whitenoise 
pip3 install dj_database_url

2) Add Whitenoise to your middleware inside settings.py:

3) Initially repository

4) Login to Heroku

5) Double check if the Heroku App is created
git remote -v 

6) Copy environment variables from .env to heroku config variables
![picture](/static/images/configvar.png)

7) Created Procfile and inseretd the following. Ensure Procfile is in the same root folder location
 web: gunicorn <PROJECT_FOLDER>.wsgi:application

8) Install local requirements.
pip3 freeze --local > requirements.txt

9) Ensure static directory are typed out as such

   <img src="{% static "images/>filename" %}" alt="Hi!" />

10) Deply by typing in</br>
git add . </br>
git commit -m "commit message"</br>
git push heroku master</br>

# Testing

| Item Tested         | Result            |   Expected Result                       |
| --------------------|:-----------------:|:-------------------------------  |
| Navbar-dropdown     | Works as intended | transforms into burger dropdown  |  
| Log-in button       | Works as intended | bring user to login page and username appears on top right hand         |  
| Log-out button      | Works as intended | bring user to landing page       | 
| Sign up link.       | Works as intended | New users are able to sign up for an accoount     |
| Image               | Works as intended | Let user see details of food     | | Add to Cart         | Works as intended | Users can add items to cart      
|   Update Quantity        | Works as intended | Users can add items to cart 
|  View Cart    | Works as intended | Users can see item and qty in cart   | 
| Remove Items        | Works as intended | Users can remove items in cart   | 
| Total Cost          | Works as intended | The total cost is calcuated      | 
| Checkout            | Works as intended | Users can pay for the item and sucesfuly bring them to sucess checkout page.                                |  
| Search              | Works as intended | Users can search for food        | 
| Add Food            | Works as intended | Users can add to the list        |
| Review Button.      | Works as intended | Users are able to see reviews    |
| Add Review          | Works as intended | Users can give feedback          |
| Delete Reviews.     | Works as intended | Users can delete reviews         |
| admin/super user    | Works as intended |Superuser status can delete or edit food items    
| Checkout.           | Works as intended | Users can pay for the item       |
| Alert messages.     | Works as intended | Users will see a flash message when they - add items in cart 
| Alert messages.     | Works as intended | Users will see a flash message when they - remove items in cart    
| Alert messages.     | Works as intended | Users will see a flash message when they - add reviews
| Alert messages.     | Works as intended | Users will see a flash message when they - delete reviews   
| Responsiveness      | Works as intended | Site works well in mobile devices   |


# Content

All content was authored by me and referenced from pages which are mentioned in the Credit Section.

# Media

Pictures and icons for the home page were taken from
1. https://www.healthline.com
2. https://www.Bicycling.com/
3. https://www.healthyeating.org
4. https://www.livescience.com/
5. https://www.jessicagavin.com/
6. https://www.culinaryhill.com
7. https://www.cleaneatingkitchen.com/
8. https://www.verywellfit.com/
9. https://www.pexels.com/
10. https://solidstarts.com/
11. https://timesofindia.indiatimes.com/
12. https://icons8.com/


# Credit

References,Javascript and bootstrap codes were used from the following websites.

1. https://www.stackoverflow.com
2. https://www.w3schools.com
3. https://www.w3.org/
4. https://getbootstrap.com/


# Page Structure Design 

<h2> Layout and Design  </h2>

The page layout was designed with this deisgn originally as such using Adobe wireframe.

![picture](/static/images/wireframe1.png)

The final outcome of the webpage was achieved as intended

The main page or also known as the landing page will tell the user abit about the website.

![picture](/static/images/screenshot.png)

Logging in, will bring him /  her to the catalogue page where he / she can shop for items.

![picture](/static/images/login.png)

![picture](/static/images/screenshot2.png)

A simple navigation bar allows the user to navigate through the website.
A shopping cart icon which allows the user to see his / her shopping cart. before checkout is located at the top right hand corner.
The logged in user is also displayed at the navigation bar.

![picture](/static/images/navigation_bar.png)

Users can add in reviews as shows in the image below.

![picture](/static/images/screenshot3.png)

Users can see the reviews as shows below.

![picture](/static/images/screenshot4.png)

Users can also add to the catalogue as shown below.

![picture](/static/images/screenshot5.png)

After adding items to their cart, the user can see what is currently in his / her shopping cart and update or remove the item.

![picture](/static/images/viewcart.png)

Upon checking out, users will be brought to the payment page.
The user will need to fill in the credit card details before being able to checkout.

![picture](/static/images/checkout.png)

Upon successfully checking out, the user will be brought to a page showing the payment is successful.

![picture](/static/images/payment_success.png)

<h2>Database</h2>

The database was created using Django.
Food details including the maker are listed here.
The list of users and those detailing the superusers are are also found here.

![picture](/static/images/Djangodb1.png)

![picture](/static/images/Djangodb2.png)

![picture](/static/images/Djangodb3.png)

# Logical Schema Diagram

The databse for this project was planned out using a logical schema diagram.
For this project, it was intended to for one food manufacturer to have several different types of Food thus staisfying the One to Many relationship

 A many to many relationship was also intended. In this case,
 One Food item can have many reviews from different customers and one customer can give different reviews for each products

 ![picture](/static/images/ERD.png) 

# Validation

The validation function works as planned.
Users will need to fill in the necessaty details before submitting the from
to add food items to the catalogue.

![picture](/static/images/validation.png)


All field needs to be filled before a feedback can be submitted.

![picture](/static/images/validation2.png)

HTML codes were validated with majority errors resolved

![picture](/static/images/htmlvalidation.png)

CSS codes were validated until there were no more errors
![picture](/static/images/cssvalidator.png)

# Email Testing

The user is able to sign up for an account and get a confirmation from healthfoodmart.

![picture](/static/images/emailtest1.png)

![picture](/static/images/emailtest2.png)










              
                                          
                                            
      
 
 