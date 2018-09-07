# POSTGRESS QSL IN PYTHON
***In this post we are goint to create the tables as listed below***

### 1. Users.
```
	Users(user_id, first_name, last_name, age, email, password, created_at)) 
```
The values of the table assigned to there respective data types and also properly define the primary key.

### 2. Events.
```
	(event_id, event_name, price, location)
```

### 3. Ticket.
```
	(ticket_id, user_id, event_id, is_valid, verification_code, created_at)
```
***The tables have been listed above with there respective fields.***

## Connecting Postegres to python
This is going to be done using ```psycopg2``` from the psycopg2 library