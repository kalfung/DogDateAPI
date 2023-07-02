# DogDateAPI

# Link to GitHub repository

https://github.com/kalfung/DogDateAPI

# Link to Trello board

https://trello.com/b/e3F45Prp/t2a2-api-webserver-project

# R0 Installation instructions

```python

```

# R1 Identification of the *problem* you are trying to solve by building this particular *app*.

This app is for organising dog play dates and meet-ups for dog owners.

Some people, like myself, find it easier to meet new people through their dogs. This app will allow dog owners to arrange social events.

Because of the Covid-19 pandemic, fewer people visited dog parks. 

# R2 Why is it a *problem* that needs solving?



# R3 Why have you chosen this database system. What are the drawbacks compared to others?

I have chosen the PostgreSQL database system because it is a relational database system. The tables 

pros vs cons compared to other systems

# R4 Identify and discuss the key functionalities and benefits of an ORM

# R5 Document all endpoints for your API

/dogs/breed GET list of all dogs of a specific breed


/dogs/dogpark

/dogs/park GET list of all dogs that frequent a specific dog park


/users/dogpark

/users/park GET list of all users that frequent a specific dog park

GET, POST, PUT, DELETE, PATCH

CRUD create read update delete


# R6 An ERD for your *app*

Users:
- name
- parks frequented (users_parks)
- dogs owned (users_dogs)
- 

# R7 Detail any third party services that your *app* will use

# R8 Describe your project's *models* in terms of the relationships they have with each other

Models include:
- users
- dogs
- dog parks
- events

Relationships:
- Users can have more than one dog, so the User/s model has a a one-to-many relationship with the Dogs model
- Users have a one to many relationship with dog parks
- Users have a one to many relationship with events
- Dogs have a one to many relationship with dog parks
- Dogs have a one to many relationship with events
- Dog parks have a one to one relationship with events

# R9 Discuss the database relations to be implemented in your application

# R10 Describe the way tasks are allocated and tracked in your project

