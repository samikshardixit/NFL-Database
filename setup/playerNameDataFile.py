import sportsipy.nfl.roster as roster
import psycopg2
import time

# Define the team list
team_list = ["DAL", "MIA", "SFO", "RAV", "DET", "BUF", "PHI", "RAM", "NOR", "CLT", "CLE", "GNB", "HTX", "JAX", "KAN", "CIN", "SEA", "CHI", "DEN", "SDG", "MIN", "RAI", "CRD", "WAS", "ATL", "OTI", "NYJ", "NWE"]

# PostgreSQL connection parameters
conn_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Sidh@1509",
    "host": "localhost",
    "port": "5432"
}

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(**conn_params)

# Create a cursor object
cur = conn.cursor()

# Create the playerName table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS nfldb.playerName (
        Player_id VARCHAR(50),
        Player_name VARCHAR(255)
    );
""")

# Commit the table creation
conn.commit()

# Iterate through each team in the team list
for team in team_list:
    # Retrieve the roster for the current team
    r = roster.Roster(team, year=2023, slim=True)
    
    # Iterate through each player in the roster
    for player_id, player_name in r.players.items():
        # Insert the player ID and name into the playerName table
        cur.execute("""
            INSERT INTO nfldb.playerName (Player_id, Player_name)
            VALUES (%s, %s);
        """, (player_id, player_name))
        
        # Commit the insertion
        conn.commit()
        
    # Pause execution for 10 seconds between teams
    time.sleep(10)

# Close the cursor and connection
cur.close()
conn.close()
