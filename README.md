Table of Content

1.0 Introduction
    1.1 Main Features
        1.1.1 Login page
        1.1.2 User Signup Page
        1.1.3 Menu Page
        1.1.4 Index Page
        1.1.5 Cart Preview Page
        1.1.6 Gallery Page
        1.1.7 Contact us Page
        1.1.8 About Us page
    1.2 Built With
2.0 Getting Started
4. Prerequisites
5. Installation
6. Usage
7. Roadmap
8. Contributing
9. License
10.Contact
11.References


1 .0 Introduction

This project is a food delivery web application. Customers come to the web application, search for food menu they like and select them for order. Once food menus are selected, all selected menu is added to cart. When menu selection is completed, the visitor clicks on checkout to view a summery of what was selected. The customer must be logged on as a valid customer with delivery address information captured. The customer proceeds to complete order by selecting payment mode.

1.1 Main Features

- Login Page: 
This page contains user login form with username and password fields and a login button. It also contains information on the required fields.

- User Signup Page:
 This page contains customer signup form. It contain all fields required to identify a customer. Username, Email Address, First Name, Last Name, Phone Number, Home Address, City, Post Code. It contains a signup button to submit the sign up request and persist the inputted data to the database.

- Menu Page: 
This page contains our menu form for our web application. It shows the list of available menu items in with descriptions and price tags with an add to order button that adds menu item to cart. The menu item is arranged in categories. The categories are starter, main, vegitarian, desserts, soft drinks, alcoholic beverages and alcoholic drinks.

- Index Page:
This page displays our index form. It contains the pictures of the kinds of menu items we have on our menu page. It also contains our map address, contact information and service available periods. We also have the an "Order Now" button that should take us to the menu page when clicked.

- Cart Preview Page:
The cart preview page show the list of selected menu items and quantities. It also shows the unit price and total price of selected menu items. It allows customer to change the quantity of each menu before checking out. On this page you can go back to the menu page to continue menu item selection by clickin the "Continue shopping" button. The "Checkout" button is for confirming checkout and should take the customer to select payment mode to complete order page. 

- Gallery Page:
This acts like our show room to display different picture galleries that help make the web application product more interesting. It is also used to pass information to the customers in pictures.

- Contact Us Page:
This page contains an enquiry form that customers can fill to pass informtion to the backend team. It also has a map that describes our contact address. We also have our mobile and email contact information on the page.

- About Us Page:
This page shows information about our product to existing or prospective customers. It gives a brief information about the history, vision, and mission of the business. It also has the information about the business team members.


1.2 Built With

Food menu delivery web application is built using django a python based framework for web application development. We had to use some django custom plugin modules to develop the web application. All the plugin modules are as listed in "requirement.txt". The django version used for the project is Django version 4.1.3. The application is written using python 3.11.

The database used is postgresql database version 14. We had to install database django plugin for django called psycopg2-binary version 2.9.5. The psycopg2-binary helps us connect to the database and create database and all defined tables, entities and relationships as defined in our model.py python file .


2.0 Getting Started

This session describes how to setup our project to get it to run successfully. We used Visual Studio Code as the IDE for development.




References

https://django-allauth.readthedocs.io/en/latest/views.html#signup-account-signup