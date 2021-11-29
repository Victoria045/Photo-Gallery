# Photo-Gallery

## Author 
Built by: [Victoria Beryl](https://github.com/Victoria045)

# Description
Photo-Gallery is a Django application where as a user you are able to view different photos, expand the photo and also view the details of the photo based on the location taken.

# User Story 
* Able to view different photos interesting me.
* Click on a single photo to expand it and view the details of the photo.
* Search for dfferent categories of photos. 
* Copy a link to the photo to share.
* View photos based on location taken.


#### Prerequisites 
* python3.6
* pip
* Django

# Setup and Installation
#### Cloning the repository
* Open Terminal:

        $ git clone https://github.com/Victoria045/Photo-Gallery.git
        $ cd Photo-Gallery
        $ code . or atom . based on your text editor 

* Navigate into the folder, install and activate virtual environment

        $ sudo pip3 install virtualenv

        $ virtualenv virtual

        $ source virtual/bin/acivate

* Install all dependencies in requirements.txt

        (virtual)$ pip install -r requirements.txt

#### Setup the Database
* Setup the database username, password, host

        (virtual)$ python manage.py makemigrations 
        posted_photos

* Run migrations

       (virtual)$ python manage.py migrate

### Running the Application
* To run the application, open the cloned repo in terminal and run the following commands:

        (virtual)$ python3 manage.py runserver

### Testing the Application       
* To run unittests for the class application and check if it functions well:

        (virtual)$ python3 manage.py test posted_photos

## Known Bugs
* No known bugs so far, incase a bug is spotted pull requests are allowed.


## Technologies Used
* markdown

* Django_Bootstrap3 - for bootstrap version 3

* Heroku - online deployment


## Support and contact details
Incase of any issues at hand, please email me at victoriaberyl45@gmail.com

### License
MIT License. 