import psycopg2

class Database:

    def __init__(self):
        self.conn = psycopg2.connect(dbname='Events_app', user='edmond', password='root', host='localhost')
        self.cur = self.conn.cursor()

    def create_all_tables(self):
        user_tab = """ CREATE TABLE IF NOT EXISTS user_entity_table (user_id SERIAL PRIMARY KEY, first_name VARCHAR(100) NOT NULL, 
        age varchar NOT NULL, last_name VARCHAR(100) NOT NULL, 
        user_email VARCHAR(120) NOT NULL, user_password VARCHAR(100) NOT NULL, 
        created_at varchar(100) NOT NULL) """

        self.cur.execute(user_tab)
        self.conn.commit()
        
        events_table = """ CREATE TABLE IF NOT EXISTS Events(event_id SERIAL PRIMARY KEY, 
        event_name VARCHAR(100) NOT NULL,
        price VARCHAR(20) NOT NULL, 
        location VARCHAR(50) NOT NULL) """

        self.cur.execute(events_table)
        self.conn.commit()


        tickets_table = """ create table if not exists Ticket(ticket_id serial PRIMARY KEY NOT NULL,
                             user_id INT REFERENCES user_entity (user_id),
                             event_id INT REFERENCES Events(event_id),
                             is_valid BOOLEAN,
                             verification_code VARCHAR,
                             created_at TIME)"""

        self.cur.execute(tickets_table)
        self.conn.commit()


class users:
    
    def __init__(self):
            self.conn = psycopg2.connect(dbname='Events_app', user='edmond', password='root', host='localhost')
            self.cur = self.conn.cursor()

    def add_user(self, first_name, age, last_name, user_email, password, created_at):
        user_add = """INSERT INTO user_entity (first_name, age, last_name, 
        user_email, password, 
        created_at) VALUES('{}', '{}', '{}', '{}', 
         '{}', '{}',)""".format(first_name, age, last_name, user_email, password, created_at)

        self.cur.execute(user_add)
        self.conn.commit()

    def get_users(self, user_id):
        user_fetcher = """SELECT * FROM user_entity WHERE user_id={}""".format(user_id)
        
        self.cur.execute(user_fetcher)
        self.conn.commit()


    def update(self, user_id, first_name, last_name): #Updates first_name and last_name
        change = """ UPDATE user_entity SET first_name='{}', last_name='{}' WHERE user_id='{}'""".format(first_name, last_name, user_id)
        
        self.cur.execute(change)
        self.conn.commit()


class ticket():

    def __init__(self):
        self.conn = psycopg2.connect(dbname='Events_app', user='edmond', password='root', host='localhost')
        self.cur = self.conn.cursor()

    def add_ticket(self):
        # ticket_add = """INSERT INTO Ticket ()
        pass

    def get_all_tickets(self):
        see = """SELECT * FROM Tiecket"""

        self.cur.execute(see)
        self.conn.commit()

    def get_ticket_by_id(self, ticket_id):
        get_ticket = """ SELECT * FROM Ticket WHERE ticket_id={}""".format(ticket_id)

        self.cur.execute(get_ticket)
        self.conn.commit()

    def ticket_update(self, ticket_id, is_valid):
        ticket_update = """UPDATE Ticket SET is_valid={} WHERE ticket_id={}""".format(is_valid, ticket_id)

        self.cur.execute(ticket_update)
        self.conn.commit()
        


class event:

    def __init__(self):
        self.conn = psycopg2.connect(dbname='Events_app', user='edmond', password='root', host='localhost')
        self.cur = self.conn.cursor()

    def get_all_events(self):
        ev_get = """ SELECT * FROM Events;"""

        self.cur.execute(ev_get)
        self.conn.commit()

    def get_event_by_id(self, event_id):
        get_id = """SELECT * FROM Events WHERE event_id={}""".format(event_id)

        self.cur.execute(get_id)
        self.conn.commit()

    def add_event(self, event_name, price, location):
        ev_add = """ INSERT INTO Events (event_name, price, location) VALUES ('{}', '{}', '{}')""".format(event_name, price, location)

        self.cur.execute(ev_add)
        self.conn.commit()

    def update_event(self, event_id, event_name, price, location):
        ev_update = """ UPDATE Events SET event_name='{}', price='{}', location='{}' WHERE event_id={}""".format(event_name,
        price, location, event_id)

        self.cur.execute(ev_update)
        self.conn.commit()
