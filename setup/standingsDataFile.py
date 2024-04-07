import psycopg2

# Data to be inserted into the stadiums table
standing_data = [
    ('Baltimore Ravens', 13, 4, 0.765),
    ('Dallas Cowboys', 12, 5, 0.706),
    ('Detroit Lions', 12, 5, 0.706),
    ('San Francisco 49ers', 12, 5, 0.706),
    ('Buffalo Bills', 11, 6, 0.647),
    ('Cleveland Browns', 11, 6, 0.647),
    ('Kansas City Chiefs', 11, 6, 0.647),
    ('Miami Dolphins', 11, 6, 0.647),
    ('Philadelphia Eagles', 11, 6, 0.647),
    ('Houston Texans', 10, 7, 0.588),
    ('Los Angeles Rams', 10, 7, 0.588),
    ('Pittsburgh Steelers', 10, 7, 0.588),
    ('Cincinnati Bengals', 9, 8, 0.529),
    ('Green Bay Packers', 9, 8, 0.529),
    ('Indianapolis Colts', 9, 8, 0.529),
    ('Jacksonville Jaguars', 9, 8, 0.529),
    ('New Orleans Saints', 9, 8, 0.529),
    ('Seattle Seahawks', 9, 8, 0.529),
    ('Tampa Bay Buccaneers', 9, 8, 0.529),
    ('Denver Broncos', 8, 9, 0.471),
    ('Las Vegas Raiders', 8, 9, 0.471),
    ('Atlanta Falcons', 7, 10, 0.412),
    ('Chicago Bears', 7, 10, 0.412),
    ('Minnesota Vikings', 7, 10, 0.412),
    ('New York Jets', 7, 10, 0.412),
    ('New York Giants', 6, 11, 0.353),
    ('Tennessee Titans', 6, 11, 0.353),
    ('Los Angeles Chargers', 5, 12, 0.294),
    ('Arizona Cardinals', 4, 13, 0.235),
    ('New England Patriots', 4, 13, 0.235),
    ('Washington Commanders', 4, 13, 0.235),
    ('Carolina Panthers', 2, 15, 0.118)
]

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

# Create the stadiums table in the nfldb schema if it doesn't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS nfldb.standings (
    Name VARCHAR(250),
    Wins INTEGER,
    Losses INTEGER,
    Pct FLOAT
);
''')

# Commit the table creation
conn.commit()

# Insert the stadium data into the stadiums table
for data in standing_data:
    cur.execute("""
        INSERT INTO nfldb.standings (Name, Wins, Losses, Pct)
        VALUES (%s, %s, %s, %s);
    """, data)

# Commit the insertions
conn.commit()
        

# Close the cursor and connection
cur.close()
conn.close()
