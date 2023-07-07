# DogDateAPI

# Link to GitHub repository

https://github.com/kalfung/DogDateAPI

# Link to Trello board

https://trello.com/b/e3F45Prp/t2a2-api-webserver-project

# R0 Installation and Setup

Clone this API repository from GitHub into your chosen folder.

Run the PostgreSQL prompt in a new terminal window:

```bash
psql
```

Create a database entitled 'dog_date_db':

```psql
CREATE DATABASE dog_date_db;
```

Connect to the database:

```psql
\c dog_date_db;
```

Create a new admin user for this database and give it a password, for example:

```psql
CREATE USER dogdatedev WITH PASSWORD 'password123';
```

Grant all privileges to this user:

```psql
GRANT ALL PRIVILEGES ON DATABASE dog_date_db TO dogdatedev;
```

In the main project directory, create an '.env' file using '.env.sample' as a template. Using the credentials we created above, the Database URI should be formatted as: 

`postgresql+psycopg2://<user>:<password>@localhost:5432/<database>`

E.g. `postgresql+psycopg2://dogdatedev:password123@localhost:5432/dog_date_db`

Navigate to the `src/` directory and run the bash script from the terminal to create a .venv folder, run the virtual environment, install requirements, create the database tables, and seed the tables with sample data:

```bash
cd src
```

```bash
$ create_and_seed.sh
```

The database and project environments are now set up. To run the app from the terminal, make sure you are in the `src/` directory to activate the virtual environment and then run the program:

```bash
$ source .venv/bin/activate
$ flask run
```

The server runs on port 5000, but this can be reassigned in the .flaskenv file.

# R1 and R2 Identification of the *problems* you are trying to solve by building this particular *app*.

Some people, like myself, find it easier to meet new people through their dogs. The creation of a web server API for creating dog play dates and meet-ups could solve several problems related to organising and facilitating interactions between dog owners and their pets. Some potential problems that this API could address include:

1. Finding compatible playmates: Some dog owners often struggle to find suitable playmates for their pets. They may rely on chance encounters at dog parks or rely on word-of-mouth recommendations. An API could provide a centralised platform where owners can connect and schedule dog playdates, improving coordination and ensuring a better social experience for their pets.

2. Time-consuming search: Searching for compatible dog playmates can be time-consuming and inefficient. An API could allow users to input preferences such as dog size, breed, temperament, location, and availability, and then match them with other owners who meet their criteria. This would save time and effort in finding suitable companions for their dogs.

3. Limited socialisation opportunities: Some dog owners may have limited access to dog parks or other socialisation events due to location, schedule, or other constraints. An API could help them expand their network by connecting with other owners nearby or even in different geographical locations, increasing their dogs' socialisation opportunities.

4. Safety concerns: When arranging dog playdates independently, there can be concerns about the safety and compatibility of the dogs involved. The API could potentially include features such as user ratings, reviews, and verification processes to ensure a safer environment for the dogs, reducing the risk of negative interactions.

5. Schedule management: Keeping track of scheduled playdates and managing appointments can be challenging. An API could provide features for scheduling, reminders, and notifications, allowing users to manage their dog's social calendar more efficiently.

6. Community engagement: Creating an API for dog dates could foster a sense of community among dog owners. It could include social features such as forums, chat functionality, and user profiles, encouraging interactions, knowledge sharing, and the formation of dog owner communities.

Overall, this dog play dates a web server API could enhance the dog-owning experience by addressing coordination challenges, expanding socialisation opportunities, improving safety, and promoting a sense of community among dog owners.

# R3 Why have you chosen this database system. What are the drawbacks compared to others?

I have chosen the PostgreSQL relational database system for this API project due to the following reasons:

1. Data organisation: An RDBMS like PostgreSQL facilitates the organisation of data in a tabular format using tables, rows, and columns. This is beneficial for managing various aspects of a dog playdates API, such as user profiles, dog information, playdate schedules, and the relationships between these different entities.

2. Data integrity: PostgreSQL provides robust support for enforcing data integrity through features such as primary keys, foreign keys, and constraints. This ensures that the data stored in the database remains consistent and accurate, preventing issues like orphaned records or data inconsistencies.

3. Querying and indexing: PostgreSQL offers a powerful query language (SQL) that allows me to retrieve, manipulate, and filter data efficiently. I can leverage SQL queries to retrieve specific information from the database, perform complex joins, aggregate data, and sort results. Additionally, PostgreSQL provides various indexing options to optimise query performance, enabling faster retrieval of data for the API.

4. Data relationships and associations: A dog playdates API involves managing relationships between different entities, such as users, dogs, parks, and playdate events. PostgreSQL's support for relational data modelling allows me to define and manage these associations using foreign keys and table relationships, facilitating efficient retrieval and manipulation of related data.

5. ACID compliance: PostgreSQL adheres to ACID (Atomicity, Consistency, Isolation, Durability) principles, ensuring that database transactions are processed reliably and consistently. This guarantees that each transaction is treated as a single, indivisible unit, maintaining data integrity and protecting against data inconsistencies in case of failures or concurrent access.

6. Scalability: PostgreSQL is designed to handle large datasets and concurrent access effectively. It offers mechanisms for horizontal scalability through features like table partitioning and replication, allowing the dog playdates API to scale as the user base and data volume increase.

7. Community support and ecosystem: PostgreSQL benefits from a vibrant and active open-source community that continuously improves and enhances the database system. The community provides regular updates, security patches, and additional features. Moreover, PostgreSQL has a rich ecosystem of extensions and plugins that can be utilised to extend the functionality of the API and integrate with other technologies.


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

