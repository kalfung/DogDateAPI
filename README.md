# DogDateAPI

# Link to GitHub repository

https://github.com/kalfung/DogDateAPI

# Link to Trello board

https://trello.com/b/e3F45Prp/t2a2-api-webserver-project

# R0 Installation instructions

Clone this API repository from GitHub into your chosen folder.

Connect to a 

```
psql
```

# R1 and R2 Identification of the *problems* you are trying to solve by building this particular *app*.

Some people, like myself, find it easier to meet new people through their dogs. The creation of a web server API for creating dog play dates and meet-ups could solve several problems related to organising and facilitating interactions between dog owners and their pets. Some potential problems that this API could address include:

1. Finding compatible playmates: Some dog owners often struggle to find suitable playmates for their pets. They may rely on chance encounters at dog parks or rely on word-of-mouth recommendations. An API could provide a centralised platform where owners can connect and schedule dog playdates, improving coordination and ensuring a better social experience for their pets.

2. Time-consuming search: Searching for compatible dog playmates can be time-consuming and inefficient. An API could allow users to input preferences such as dog size, breed, temperament, location, and availability, and then match them with other owners who meet their criteria. This would save time and effort in finding suitable companions for their dogs.

3. Limited socialisation opportunities: Some dog owners may have limited access to dog parks or other socialisation events due to location, schedule, or other constraints. An API could help them expand their network by connecting with other owners nearby or even in different geographical locations, increasing their dogs' socialisation opportunities.

4. Safety concerns: When arranging dog playdates independently, there can be concerns about the safety and compatibility of the dogs involved. The API could potentially include features such as user ratings, reviews, and verification processes to ensure a safer environment for the dogs, reducing the risk of negative interactions.

5. Schedule management: Keeping track of scheduled playdates and managing appointments can be challenging. An API could provide features for scheduling, reminders, and notifications, allowing users to manage their dog's social calendar more efficiently.

6. Community engagement: Creating an API for dog dates could foster a sense of community among dog owners. It could include social features such as forums, chat functionality, and user profiles, encouraging interactions, knowledge sharing, and the formation of dog owner communities.

Overall, a web server API for creating dog dates could enhance the dog-owning experience by addressing coordination challenges, expanding socialisation opportunities, improving safety, and promoting a sense of community among dog owners.




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

## Park

### **GET** `/parks`

Retrieves a list of all parks in the database. 

- methods: **GET**
- parameters: None
- headers: Authorisation: {Bearer Token}
- response: _200_
- response: _401_

![get all cards](./docs/postman/parks_GET.PNG)



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

