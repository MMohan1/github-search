# Django GitHub Search

Django GitHub Search application built using Requests, Bower, Twitter Bootstrap and Github API

# Installation

To install the required libraries for this file, simply run the following:

    pip install -r requirements.txt

This project also requires using Bower, which requires NPM. In order to get NPM, simple install <a href="https://nodejs.org/download/">Node.js</a>. Once you have node, you can install <a href="http://bower.io/">Bower</a>:

    npm install -g bower

**Note**: On a Mac, you'll need to use:

    sudo npm install -g bower

With Bower, you can install the front-end dependencies by running:

    bower install

This will generate the **static** folder along with **bootstrap** and **jquery** inside it.


# Running the project

To run this project:


    # Setup the database
    python manage.py migrate
    python manage.py makemigrations

    # Run the server
    python manage.py runserver

You can now visit the following URLS:

	* http://127.0.0.1:8000/github/search/

# Tests

Run the test suite:

    python manage.py test


## Problem Statement  
Given a target website to you [Github at https://github.com](https://github.com) which allows finding results based on input search query. Use the search box to perform search based on input query - **artifical intelligence**. Provide answers to below questions -  

1.  Github url and description of top 50 projects having maximum stars given by the users for the input query. *Note* description / title will be available on click of the title of the search result   
2.  Unique list of programming languages involved in top 50 projects  
3.  Average star rating of all top 50 projects  
