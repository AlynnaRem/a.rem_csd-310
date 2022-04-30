""" Name Alynna Rem 
    Date: 4/30/2022
    Assignment: Module 9.3 PySports: Update & Deletes
    File name: pysports_update_and_delete.py
    Details: 
    1. Connect to the pysports database.
    2. Insert a new record into the player table for Team Gandalf. team_id = 1
    3. Execute a select query to display the player records (verification of inserted record) Include Inner join
    4. Update the newly inserted record by changing the players team to Team Sauron. team_id = 2
    5. Execute a select query to display the updated record. Include Inner join
    6. Execute a delete query to remove the updated record.
    7. Execute a select query to display all the records in the player table. Include Inner join
"""


""" Connect to the pysports database """
""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


# Create method to execute an inner join on player and team table, iterate over the dataset, and output results
def show_players(cursor, title):

    # execute inner join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id ASC;")

    # get the results from the cursor object 
    players = cursor.fetchall()

    # print the title of the results
    print("\n  -- {} --".format(title))
    
    # iterate over the player data set and display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    # get the cursor object
    cursor = db.cursor()

    # insert player
    add_player = ("INSERT INTO player(player_id, first_name, last_name, team_id)"
                       "VALUES(%s, %s, %s, %s);")

    # create player_data variable to store new record for Team Gandalf. player_id =21, first_name = Smeagol, last_name = Shire Folk, and team_id = 1
    player_data = (21, "Smeagol", "Shire Folk", 1)

    # execute insert query
    cursor.execute(add_player, player_data)

    # commit the insert to the database 
    db.commit()

    # execute the show_players method to show all records in the player table after insert
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # update the newly inserted record 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

    # execute the update query
    cursor.execute(update_player)

    # show all records in the player table after update
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # delete the recently updated player
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum';")

    # execute the delete query
    cursor.execute(delete_player)

    # commit the delete to the databse
    db.commit()

    # execute the show_players method to show all records in the player table after delete
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    # display a message for the user to press any key to continue
    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()


""" Reference:

https://github.com/AlynnaRem/Course_csd-310/blob/master/module_9/pysports_update_and_delete.py

"""

