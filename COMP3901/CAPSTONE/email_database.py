import mysql.connector

class Emails:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        drop_table_query = "DROP TABLE IF EXISTS Emails;"
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Emails (
            Email varchar(255)
        );"""
        try:
            # Drop table if exists
            self.cursor.execute(drop_table_query)
            # Create table
            self.cursor.execute(create_table_query)
            # Commit changes
            self.connection.commit()
            print("Table 'Emails' created successfully")
        except mysql.connector.Error as error:
            print("Error creating table: {}".format(error))

    def add_email(self, email):
        add_email_query = "INSERT INTO Emails (Email) VALUES (%s);"
        try:
            # Insert email into table
            self.cursor.execute(add_email_query, (email,))
            # Commit changes
            self.connection.commit()
            print("Email added successfully")
        except mysql.connector.Error as error:
            print("Error adding email: {}".format(error))

    def get_emails(self):
        get_emails_query = "SELECT Email FROM Emails;"
        try:
            # Execute query
            self.cursor.execute(get_emails_query)
            # Fetch all emails
            emails = self.cursor.fetchall()
            return [email[0] for email in emails]
        except mysql.connector.Error as error:
            print("Error getting emails: {}".format(error))
            return []

    def close_connection(self):
        # Close cursor and connection
        self.cursor.close()
        self.connection.close()


