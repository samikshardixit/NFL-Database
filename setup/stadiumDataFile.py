import psycopg2

# Data to be inserted into the stadiums table
stadium_data = [
    ("Arizona Cardinals", "State Farm Stadium", "Glendale, Arizona", "63,400", "2006"),
    ("Atlanta Falcons", "Mercedes-Benz Stadium", "Atlanta, Georgia", "71,000", "2017"),
    ("Baltimore Ravens", "M&T Bank Stadium", "Baltimore, Maryland", "71,008", "1998"),
    ("Buffalo Bills", "Highmark Stadium", "Orchard Park, New York", "71,608", "1973"),
    ("Carolina Panthers", "Bank of America Stadium", "Charlotte, North Carolina", "75,523", "1996"),
    ("Chicago Bears", "Soldier Field", "Chicago, Illinois", "61,500", "1924"),
    ("Cincinnati Bengals", "Paycor Stadium", "Cincinnati, Ohio", "65,515", "2000"),
    ("Cleveland Browns", "Cleveland Browns Stadium", "Cleveland, Ohio", "67,895", "1999"),
    ("Dallas Cowboys", "AT&T Stadium", "Arlington, Texas", "80,000", "2009"),
    ("Denver Broncos", "Empower Field at Mile High", "Denver, Colorado", "76,125", "2001"),
    ("Detroit Lions", "Ford Field", "Detroit, Michigan", "65,000", "2002"),
    ("Green Bay Packers", "Lambeau Field", "Green Bay, Wisconsin", "81,441", "1957"),
    ("Houston Texans", "NRG Stadium", "Houston, Texas", "72,220", "2002"),
    ("Indianapolis Colts", "Lucas Oil Stadium", "Indianapolis, Indiana", "67,000", "2008"),
    ("Jacksonville Jaguars", "TIAA Bank Field", "Jacksonville, Florida", "69,132", "2008"),
    ("Kansas City Chiefs", "GEHA Field at Arrowhead Stadium", "Kansas City, Missouri", "76,416", "1972"),
    ("Las Vegas Raiders", "Allegiant Stadium", "Paradise, Nevada", "65,000", "2020"),
    ("Los Angeles Chargers", "SoFi Stadium", "Inglewood, California", "70,240", "2020"),
    ("Los Angeles Rams", "SoFi Stadium", "Inglewood, California", "70,240", "2020"),
    ("Miami Dolphins", "Hard Rock Stadium", "Miami Gardens, Florida", "65,326", "1987"),
    ("Minnesota Vikings", "U.S. Bank Stadium", "Minneapolis, Minnesota", "66,655", "2016"),
    ("New England Patriots", "Gillette Stadium", "Foxborough, Massachusetts", "66,829", "2002"),
    ("New Orleans Saints", "Ceasars Superdome", "New Orleans, Louisiana", "73,208", "1975"),
    ("New York Giants", "MetLife Stadium", "East Rutherford, New Jersey", "82,500", "2010"),
    ("New York Jets", "MetLife Stadium", "East Rutherford, New Jersey", "82,500", "2010"),
    ("Philadelphia Eagles", "Lincoln Financial Field", "Philadelphia, Pennsylvania", "69,596", "2003"),
    ("Pittsburgh Steelers", "Acrisure Stadium", "Pittsburgh, Pennsylvania", "68,400", "2001"),
    ("San Francisco 49ers", "Levi's Stadium", "Santa Clara, California", "68,500", "2014"),
    ("Seattle Seahawks", "Lumen Field", "Seattle, Washington", "69,000", "2002"),
    ("Tampa Bay Buccaneers", "Raymond James Stadium", "Tampa, Florida", "65,890", "1998"),
    ("Tennessee Titans", "Nissan Stadium", "Nashville, Tennessee", "69,143", "1999"),
    ("Washington Commanders", "Commanders Field", "Landover, Maryland", "82,000", "1997")
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
cur.execute("""
    CREATE TABLE IF NOT EXISTS nfldb.stadiums (
        Team_Name VARCHAR(255),
        Arena_Name VARCHAR(255),
        Arena_Location VARCHAR(255),
        Seating_Capacity VARCHAR(255),
        Opening_Year VARCHAR(255)
    );
""")

# Commit the table creation
conn.commit()

# Insert the stadium data into the stadiums table
for data in stadium_data:
    cur.execute("""
        INSERT INTO nfldb.stadiums (Team_Name, Arena_Name, Arena_Location, Seating_Capacity, Opening_Year)
        VALUES (%s, %s, %s, %s, %s);
    """, data)

# Commit the insertions
conn.commit()
        

# Close the cursor and connection
cur.close()
conn.close()
