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
    2.1 Prerequisites
    2.2 Installations
    2.3 Source Code Download

3.0 Attributions
    3.1 Users and Customer Management
    3.2 Menu, Cart and Checkout 
    3.3 Gallery 
    3.4 Contact Us

4.0 Technologies and Libraries Used
    4.1 Backend
    4.2 Frontend
    4.3 Database
    4.4 Version Control
    
5.0 Roadmap
6.0 References


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

The database used is postgresql database version 14. We had to install database django plugin for django called psycopg2-binary version 2.9.5. The psycopg2-binary helps us connect to the database and create database and all defined tables, entities and relationships as defined in our model.py python file. We used boostrap 5 for the view design.


2.0 Getting Started

This session describes how to setup our project to get it to run successfully. We used Visual Studio Code as the IDE for development. We ensure all the required extensions that is need for the project as listed in the requirement.txt are installed.

To create Virtual Environment

$python3 -m venv /path/to/directory

2.1 Prerequisites

- Python3 must be linked to valid installatio of python 3. 
- The "pip" should be installed and pip3 valid for installing python 3 packages.
- You must have virtual environment created to help isolate your project artifacts from systems artifacts. 
- Ensure your git is istalled on your computer and login account set.

2.2 Installtions

- Download and install Visual Studio Code from here; https://code.visualstudio.com

Then open the extension tab and install all the required django extensions as listed in the requirements.txt file.

- If you do not have django installed for python 3, then run the following command

For Mac OS Users

$ pip3 install django

- Install all requirement by running the following. All requirements will be installed in your virtual environment.

For Mac OS Users

$ pip3 install -r requirements.txt

- Download and install Postgresql 14. Ensure the port is set to 5434.

2.3 Source Code Download

To download the source code, change directory to where you want to store the source code on your terminal or command prompt of your VSCode. Then run the following command;

$ git clone https://github.com/elivinus/DBS.git

Once the project is cloned, change directory to your virtual environment and activate your project to use your virtual environemnt as follows;

You’ll need to use different syntax for activating the virtual environment depending on which operating system and command shell you’re using.

On Unix or MacOS, using the bash shell: source /path/to/venv/bin/activate
On Unix or MacOS, using the csh shell: source /path/to/venv/bin/activate.csh
On Unix or MacOS, using the fish shell: source /path/to/venv/bin/activate.fish
On Windows using the Command Prompt: path\to\venv\Scripts\activate.bat
On Windows using PowerShell: path\to\venv\Scripts\Activate.ps1

3.0 Attributions
All features of the application is attributted to each member of the project team to acknowledge their effort and dedication.

3.1 Users and Customer Management

The user signup and login pages was created and implemented by Enoja Livinus. He did the design, created the html, CSS and Javascript based web pages, implemented the page switch, redirects and implemented the backend controllers for each pages. All new user signup are persisted to the database and used for authentication during login. 

3.2 Menu, Cart and Checkout 

The Menu, cart and checkuot pages were created and implemented by Michael Doyle. He was an integral team member that put a lot off effort to ensure we deliver the project.He did the design, created the html, CSS and Javascript based web pagee. He implemented the page switches, redirects and implemented the backend conrollers for each pages. All display and creation of menu items on the menu page was done by him. The checkout summerry page that allows quantity of selected item to be modified was implemented by him.

3.3 Gallery 

The gallery page was created and implemented by Yash. He did the design, created the html, CSS and Javascript based web page. He implemented the page switches, redirects and the backend conrollers for the page.

3.4 Contact Us

The contact us page was created and implemented by Ebele Onyeka. She did the design, created the html, CSS and javascript based web page. She implemented the page switch, redirects and the backend controller for the pag.

4.0 Technologies and Libraries Used
This section shows the technologies and libraries used to implement the project. After our initial project meeting, the team decided to use the following techonlogies for different aspects of the project.

4.1 Backend
The team used the following technologies for the backend

a) Python version 3.11
b) Django version 4.1.3

4.2 Front End
The following technologies was used for the frontend implementation

a) Bootstrap 5
b) HTML 5
c) Javascript
d) CSS

4.3 Database
We decided to use a relational dabase management system (RDBMS) for our database. We chose to use Postgresql 14.

4.4 Version control 
The version control used for the project implementation is GitHub. This was because GitHub is a free version control solution for limited source code management. The project was commited on github https://github.com/elivinus/DBS/. The github allowed for collaboration among team members and helped us track progress of each team member during the implementation.

5.0 Road Map

We started the project by holding meetings to discuss the idea and design. We agreed on the design and shared responsibilities with all members. There were so many review sessions to align on changes and additions to the application design. We had a lot of challenges during the implementation of this project. we had to make concultations to person we feel could help clarify challeneges and guide us towards resolving them. 

6.0 References

https://django-allauth.readthedocs.io/en/latest/views.html#signup-account-signup
https://studygyaan.com/django/how-to-extend-django-user-model
https://www.infoworld.com/article/3239675/virtualenv-and-venv-python-virtual-environments-explained.html
