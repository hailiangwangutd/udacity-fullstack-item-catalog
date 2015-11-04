# udacity-fullstack-p3-item-catalog

### About

Udacity Full Stack Web Development project: Item Catalog. This project provides an application that provides a lits of electronic shops with a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

This project uses python 2.7.9, the flask framework, an sqlite db and facebook and google 3rd party authentication API's to create a webapp to display and update shop and item menus. 

Besides, this project provides several json api like below:
```bash
shop list: http://localhost:5000/shop/JSON
menu list for certain shop: http://localhost:5000/shop/`shop id, ex. 1`/menu/JSON
certain menu of certain shop: http://localhost:5000/shop/`shop id, ex. 1`/menu/`menu id, ex. 1`/JSON
```
### Quick Start

First you need to install vagrant, then commect to virtual machine by `vagrant up`, `vagrant ssh`. Clone this repository directory and first run `python database_setup.py` to setup database, then run `python lotsofmenus.py` to initialize some sample, finally run `python project.py` to start the server. Now you could view the website at `http://localhost:5005`.

Index page not login:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot1.png)

Store page not login:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot2.png)

Login page:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot3.png)

Index page login:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot4.png)

New shop page:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot5.png)

Index page with shop created:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot6.png)

Shop page login:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot7.png)

Add new item:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot8.png)

Shop page with item created: 
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot9.png)

Delete item:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot10.png)

Item deleted:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot11.png)

Delete shop:
![Alt text](https://github.com/hailiangwangutd/udacity-fullstack-p3-item-catalog/blob/master/pics/Screen%20Shot12.png)
