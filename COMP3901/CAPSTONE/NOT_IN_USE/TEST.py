import MySQLdb
import sshtunnel

class DatabaseManager:
    def __init__(self):
        sshtunnel.SSH_TIMEOUT = 500.0
        sshtunnel.TUNNEL_TIMEOUT = 500.0

        with sshtunnel.SSHTunnelForwarder(
            ('ssh.pythonanywhere.com'),
            ssh_username='Starmite', ssh_password='Destructiveprince21',
            remote_bind_address=('Starmite.mysql.pythonanywhere-services.com', 3306)
        ) as self.tunnel:
            self.connection = MySQLdb.connect(
                user='Starmite',
                passwd='Starmitianwarlord23',
                host='127.0.0.1', port=self.tunnel.local_bind_port,
                db='Starmite$Capstone',
            )
            self.cursor = self.connection.cursor()

            # create_table_query = """
            #     CREATE TABLE Capture (
            #         ID INT PRIMARY KEY,
            #         Car_ID INT,
            #         Score DECIMAL(5,2),
            #         Critical BOOLEAN,
            #         Threat VARCHAR(255)
            #     );
            # """
            # self.cursor.execute(create_table_query)
            # print("Capture table created successfully")
                
            print("Connected")

    def manipulate_database(self, query):
        return self.cursor.execute(query)

    def get_ids(self):
        get_id_query = """
            SELECT ID FROM Capture;
            """
        self.cursor.execute(get_id_query)
        self.connection.commit()
        ids = [row[0] for row in self.cursor.fetchall()]
        return ids

    def insert_info(self, info):
        insert_query = f"""
            INSERT INTO Capture (ID, Car_ID, Score, Critical, Threat) 
            VALUES ({info[0]}, {info[1]}, {info[2]}, {info[3]}, {info[4]});
            """
        self.cursor.execute(insert_query)
        self.connection.commit()

    def update_threat(self, info):
        update_query = f"""
            UPDATE Capture 
            SET Score = {info[0]}
            WHERE ID = {info[1]}
            """
        self.cursor.execute(update_query)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

#if __name__ == "__main__":
#    pass
    # Example usage:
    # db_manager = DatabaseManager()
    # ids = db_manager.get_ids()
    # print(ids)
    # db_manager.close_connection()
