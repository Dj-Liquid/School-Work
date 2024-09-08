import mysql.connector

class CaptureDatabase:
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
        create_table_query = """
            CREATE TABLE IF NOT EXISTS Capture (
                ID INT PRIMARY KEY,
                Score DECIMAL(5,2),
                Critical BOOLEAN,
                Time INT
            );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print("Capture table created successfully")

    def manipulate_database(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def get_ids(self):
        get_id_query = """
            SELECT ID FROM Capture;
        """
        self.cursor.execute(get_id_query)
        ids = [row[0] for row in self.cursor.fetchall()]
        return ids
    
    def get_score(self, info):

        get_score_query = """
        SELECT Score FROM Capture
        WHERE ID = %s
        """
        self.cursor.execute(get_score_query, (info[0],))
        row = self.cursor.fetchone()  # Fetch only the first row
        if row:
            score = row[0]
        else:
        # If no row is found, return a default value (or handle it as needed)
            score = None
        return score
    
    def get_time(self, info):

        get_time_query = """
        SELECT Time FROM Capture
        WHERE ID = %s
        """
        self.cursor.execute(get_time_query, (info[0],))
        row = self.cursor.fetchone()  # Fetch only the first row
        if row:
            time = row[0]
        else:
        # If no row is found, return a default value (or handle it as needed)
            time = None
        return time

    def empty_table(self):
        empty_query = """
        DELETE FROM Capture;
        """
        self.cursor.execute(empty_query)
        self.connection.commit()

    def insert_info(self, info):
        insert_query = """
        INSERT INTO Capture (ID, Score, Critical, Time)
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_query, info)
        self.connection.commit()

    def update_time(self, info):
        time_query = """
        UPDATE Capture
        SET Time = %s
        WHERE ID = %s
        """
        self.cursor.execute(time_query, (info[0], info[1]))
        self.connection.commit()


    def update_threat(self, info):
        update_query = """
        UPDATE Capture 
        SET Score = %s
        WHERE ID = %s
        """
        self.cursor.execute(update_query, (info[0], info[1]))
        self.connection.commit()


    def close_connection(self):
        self.cursor.close()
        self.connection.close()



