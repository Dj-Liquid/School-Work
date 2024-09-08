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
        drop_table_query = "DROP TABLE IF EXISTS Capture;"
        create_table_query = """
        CREATE TABLE Capture (
            ID INT PRIMARY KEY,
            Zone BOOLEAN,
            Time INT,
            Count INT
        );
    """
        # Execute the drop table query
        self.cursor.execute(drop_table_query)
    # Execute the create table query
        self.cursor.execute(create_table_query)
    # Commit the changes
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

    def insert_info(self, info):#DONE
        insert_query = """
        INSERT INTO Capture (ID, Zone, Time, Count)
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_query, info)
        self.connection.commit()

    def update_time(self, info):#DONE
        time_query = """
        UPDATE Capture
        SET Time = %s
        WHERE ID = %s
        """
        self.cursor.execute(time_query, (info[0], info[1]))
        self.connection.commit()


    def update_zone(self, info):#DONE
        update_query = """
        UPDATE Capture 
        SET Zone = %s
        WHERE ID = %s
        """
        self.cursor.execute(update_query, (info[0], info[1]))
        self.connection.commit()

    def get_zone(self, info):

        get_score_query = """
        SELECT Zone FROM Capture
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
    
    def update_count(self, info):
        # Fetch current count value
        select_query = "SELECT Count FROM Capture WHERE ID = %s;"
        self.cursor.execute(select_query, (info[0],))
        current_count = self.cursor.fetchone()[0]  # Assuming only one row is fetched

        # Increment count value by 1
        new_count = current_count + 1

        # Update count value in the database
        update_query = """
        UPDATE Capture
        SET Count = %s
        WHERE ID = %s;
        """
        self.cursor.execute(update_query, (new_count, info[0]))
        self.connection.commit()

    def reset_count(self, info):
        # Fetch current count value
        new_count=0
        update_query = """
        UPDATE Capture
        SET Count = %s
        WHERE ID = %s;
        """
        self.cursor.execute(update_query, (new_count, info[0]))
        self.connection.commit()

    def get_count(self, info):

        get_count_query = """
        SELECT Count FROM Capture
        WHERE ID = %s
        """
        self.cursor.execute(get_count_query, (info[0],))
        row = self.cursor.fetchone()  # Fetch only the first row
        if row:
            count = row[0]
        else:
        # If no row is found, return a default value (or handle it as needed)
            count = None
        return count


    def close_connection(self):
        self.cursor.close()
        self.connection.close()



