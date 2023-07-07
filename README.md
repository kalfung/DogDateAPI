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

Some people, like myself, find it easier to meet new people through their dogs. The app allows users to create play dates, meet-ups, or other events at dog parks. The creation of a web server API for creating dog play dates and meet-ups could solve several problems related to organising and facilitating interactions between dog owners and their pets. Some potential problems that this API could address include:

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

7. Geospatial capabilities: Becauseg the dog playdates API involves geolocation or spatial data, PostgreSQL's built-in support for geospatial data types and indexing can be advantageous. It enables efficient storage and querying of location-based data, allowing features like finding parks or playdates near a specific location.

8. Community support and ecosystem: PostgreSQL benefits from a vibrant and active open-source community that continuously improves and enhances the database system. The community provides regular updates, security patches, and additional features. Moreover, PostgreSQL has a rich ecosystem of extensions and plugins that can be utilised to extend the functionality of the API and integrate with other technologies.

Despite its strengths, PostgreSQL also has some drawbacks compared to other database systems:

1. Performance: In certain scenarios, PostgreSQL's performance may be slightly lower than some other database systems like MySQL. However, this difference is often negligible and highly dependent on the specific use case and workload.

2. Learning curve: PostgreSQL's advanced features and extensibility come at the cost of increased complexity. Developers who are unfamiliar with PostgreSQL may require some additional learning and training to make the most of its capabilities.

3. Resource requirements: PostgreSQL may require more system resources (CPU, memory) compared to lighter-weight database systems. This consideration becomes relevant when deploying the API on limited hardware or in resource-constrained environments.

4. Replication and clustering: While PostgreSQL offers replication and clustering capabilities, they might be more complex to set up and manage compared to some other database systems. Achieving high availability and scalability in distributed environments may require additional configuration and expertise.

# R4 Identify and discuss the key functionalities and benefits of an ORM

## Functionality

Some of the key functionalities of an ORM include:

1. Object-Relational Mapping: The primary function of an ORM is to map the relational data model to objects in an application. It automatically converts database tables, columns, and relationships into corresponding classes, attributes, and associations in the programming language of choice.

2. Data Manipulation: ORM tools provide methods and APIs to perform common database operations, such as creating, retrieving, updating, and deleting records (often referred to as CRUD operations). Developers can work with objects and use ORM methods to perform these operations, abstracting away the underlying SQL statements.

3. Querying and Filtering: ORM frameworks typically offer query language abstractions that allow developers to construct complex database queries using object-oriented syntax. Instead of writing raw SQL queries, developers can use ORM query methods to retrieve specific data based on conditions, perform aggregations, and join tables.

4. Transaction Management: ORM tools provide transaction management capabilities, allowing developers to group a set of database operations into a single transaction. Transactions ensure the atomicity, consistency, isolation, and durability (ACID) properties of database operations, ensuring data integrity and preventing issues such as partial updates or data inconsistencies.

5. Relationship Management: One of the core features of an ORM is managing relationships between objects and database tables. ORM frameworks handle associations like one-to-one, one-to-many, and many-to-many relationships, automatically fetching related data and managing foreign key constraints.

6. Schema Migrations: ORM frameworks often include functionality for managing database schema changes over time. They provide migration tools that allow developers to define and execute database schema modifications, such as creating tables, adding or modifying columns, and establishing relationships, while preserving existing data.

7. Performance Optimisation: ORM tools often include performance optimisation features, such as caching, lazy loading, and query optimisation. These features aim to reduce the number of database queries and improve the overall performance of the application by minimising unnecessary round trips to the database.

8. Database Agnosticism: Many ORM frameworks strive to be database-agnostic, meaning they can work with multiple database systems, including PostgreSQL, MySQL, SQLite, and others. This allows developers to switch between different databases without modifying their application code significantly.

ORMs provide a convenient and productive way to interact with databases by abstracting away much of the low-level SQL and database-specific details. They simplify database operations, reduce boilerplate code, and promote cleaner, more maintainable code.

## Benefits

Benefits of an ORM when working with relational databases include:

1. Productivity and Code Maintainability: ORM frameworks provide a higher-level abstraction that allows developers to work with objects instead of writing raw SQL queries. This abstraction simplifies database interactions, reduces the amount of boilerplate code, and promotes cleaner and more maintainable code. Developers can focus on business logic rather than dealing with low-level database operations.

2. Object-Oriented Programming Paradigm: ORM bridges the gap between the object-oriented programming model and the relational database model. It allows developers to directly work with objects and relationships, providing a more natural and intuitive way to represent and manipulate data in the application code.

3. Data Abstraction: ORM provides a layer of abstraction that shields developers from the complexities of database-specific operations and optimisations. Developers can focus on the logical structure of the data and interact with it using object-oriented concepts, rather than getting into the intricacies of SQL syntax or database-specific features.

4. Schema Migration and Version Control: ORM tools often include functionality for managing database schema changes over time. They provide migration tools that allow developers to define and execute database schema modifications while preserving existing data. This makes it easier to evolve the database schema alongside application development and integrate schema changes into version control systems.

5. Testing and Mocking: ORM's abstraction layer simplifies the testing process by allowing developers to work with mock objects or in-memory databases during testing. This promotes easier unit testing and facilitates the isolation of database interactions from the rest of the application logic.

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

![ERD for dog date API](./docs/DogDateAPI_ERD.png)

# R7 Detail any third party services that your *app* will use

**Flask**

Flask is a lightweight and flexible web framework for building web server APIs. It is written in Python and provides a simple and intuitive interface for developers. Flask is used in this app to handle routing, request handling, and response generation. It also supports various extensions, allowing database integration and authentication. Flask's simplicity and extensive documentation make it the best choice for creating a RESTful API for this app.

**Flask-Bcrypt** 

Flask-Bcrypt is a Flask extension that simplifies the process of hashing passwords in web server APIs. It integrates the bcrypt hashing algorithm into Flask, which is known for its strong security. By using Flask-Bcrypt, this app can easily generate secure hash representations of passwords, making them more resistant to attacks. It provides functions for hashing passwords during user registration and for comparing hashed passwords during user authentication. Flask-Bcrypt ensures that password handling is done securely, adding an additional layer of protection to the Dog Date API when dealing with sensitive user information.

**Flask-JWT-Extended**

Flask-JWT-Extended is a Flask extension that simplifies the implementation of authentication and JSON Web Tokens (JWT) in web server APIs. It provides a straightforward way to handle user authentication and authorisation. With Flask-JWT-Extended, the Dog Date API app generates JWTs upon user login, which can then be used for subsequent API requests to verify the user's identity and access rights. It supports features like token expiration, token refreshing, and role-based access control.

**Flask-SQLAlchemy**

Flask-SQLAlchemy is a Flask extension that simplifies the use of Object-Relational Mapping (ORM) when building web server APIs. It provides an intuitive interface for interacting with databases using SQLAlchemy, a powerful ORM library. With Flask-SQLAlchemy, the Dog Date API's database models can be defined as Python classes, allowing for easy manipulation and querying of data. It handles the mapping between the objects and the underlying database tables, abstracting away the complexities of SQL.

**Flask-Marshmallow**

Flask-Marshmallow is a Flask extension that simplifies the process of serialising and deserialising data when building web server APIs. It integrates Marshmallow, a powerful library for object serialisation, into Flask. With Flask-Marshmallow, we can define schemas within the Dog Date API app that specify how data should be validated, formatted, and transformed before being sent over the API or stored in a database. It also provides easy integration with Flask-SQLAlchemy, allowing for seamless serialisation of SQLAlchemy models.

**PostgreSQL**

PostgreSQL is a reliable and feature-rich Relational Database Management System (RDBMS) often used when building web server APIs. It offers advanced data integrity and transaction management capabilities, making it suitable for handling complex data relationships. With support for JSON data types, full-text search, and spatial data, PostgreSQL provides flexibility in storing and querying diverse data formats. Its open-source nature and active community ensure regular updates and strong security measures. PostgreSQL integrates well with popular web frameworks like Flask and provides efficient data storage and retrieval, which made it the perfect choice for building the Dog Date API webserver.

**Psycopg2-binary**

Psycopg2-binary is a PostgreSQL adapter for Python that facilitates communication between a web server API and a PostgreSQL database. It allows the DogDate API app to interact with the database by executing SQL queries, fetching results, and managing transactions. Psycopg2-binary provides a high-performance and efficient way to connect to PostgreSQL databases, ensuring reliable and secure data operations. It handles data type conversions and supports features like connection pooling and server-side cursors, optimising the performance of database interactions.

**Python-dotenv**

Python-dotenv is a Python library that simplifies the management of environment variables in web server APIs. It allows developers to store sensitive configuration variables, such as database credentials or API keys, in a separate .env file. Python-dotenv automatically loads these variables into the application's environment, making them accessible within the API code. This approach enhances security by keeping sensitive information separate from the source code and allows for easy deployment across different environments.

# R8 Describe your project's *models* in terms of the relationships they have with each other

**User**

Represents a user of the API, typically a dog owner. It has a one-to-many relationship with the Dog model since a user can have multiple dogs, but each dog can only have one user. Additionally, a user has a one-to-many relationship with the Event model because a single user can create multiple events, but each event can only have one creator.

**Dog**

Represents a dog participating in the play dates and meet-ups. It has a many-to-one relationship with the User model since multiple dogs can belong to a single user, but each dog can only have one user. 

**Park**

Represents a dog park or other venue where the dog play dates or meet-ups occur. It has a one-to-many relationship with the Event model because multiple events can take place in a single park, but a single play date or meet-up can only occur in one park.

**Event**

Represents a specific play date or meet-up event. It has a many-to-one relationship with both the User and Park models. Each event is associated with a single user that created or organised the event, and takes places in a specific park. 

**Event User**

While the event creator user would have a one-to-many relationship with the Event model, the attendee users would have a many-to-many relationship with the Event model. A user can attend multiple events, and an event can have multiple attendees. By introducing the 'events_users' join table, we allow for the many-to-many relationship betwen attendee users and events.

# R9 Discuss the database relations to be implemented in your application

![ERD relationships](./docs/DogDateAPI_ERD_relationships.png)


foreign keys etc

# R10 Describe the way tasks are allocated and tracked in your project

