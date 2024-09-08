import MySQLdb
import sshtunnel

sshtunnel.SSH_TIMEOUT = 100.0
sshtunnel.TUNNEL_TIMEOUT = 100.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='Starmite', ssh_password='Destructiveprince21',
    remote_bind_address=('Starmite.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user='Starmite',
        passwd='Starmitianwarlord23',
        host='127.0.0.1', port=tunnel.local_bind_port,
        db='Starmite$Capstone',
    )
    # Do stuff
    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE Capture (
            ID INT PRIMARY KEY,
            Car_ID INT,
            Score DECIMAL(5,2),
            Critical BOOLEAN,
            Threat VARCHAR(255)
        );
        """
    #cursor.execute(create_table_query)
    #print("Capture table created successfully")
        
    print("Connected")
    

def manipulate_database(query):
    return cursor.execute(query)

def get_ids():
    get_id_query = """
        SELECT ID FROM Capture;
        """
    cursor = connection.cursor()
    cursor.execute(get_id_query)
    connection.commit()
    ids = [row[0] for row in cursor.fetchall()]
    return ids

def insert_info(info):
    insert_query = f"""
        INSERT INTO Capture (ID,Car_ID, Score, Critical, Threat) VALUES ({info[0]}, {info[1]}, {info[2]}, {info[3]},{info[4]});
        """
    cursor = connection.cursor()
    cursor.execute(insert_query)
    connection.commit()

def update_threat(info):
    update_query = f"""
            UPDATE Capture 
            SET Score = {info[0]}
            WHERE ID = {info[1]}
        """
    cursor = connection.cursor()
    cursor.execute(update_query)
    connection.commit()


#cursor.close()
#connection.close()

if __name__ == "__main__":
    pass
    #connect_to_database()

