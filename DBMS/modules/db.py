import psycopg2

class Db:

    def __init__(self):
        self.conn = psycopg2.connect(dbname='Events_app', user='edmond', password='root', host='localhost')
        self.cur = self.conn.cursor()

    def create_all_tables(self):
        user_tab = """ CREATE TABLE IF NOT EXISTS user_entity (user_id SERIAL PRIMARY KEY, first_name VARCHAR(100) NOT NULL, 
        age SMALLINT NOT NULL, last_name VARCHAR(100) NOT NULL, 
        user_email VARCHAR(120) NOT NULL, user_password VARCHAR(100) NOT NULL, 
        created_at TIME) """

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
