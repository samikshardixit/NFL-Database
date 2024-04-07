import psycopg2 as pgre
import schema_hardcoded as setup_sql
import sql_helpers
import data_collection as dc
from os import environ

DB          = "postgres"
USER        = "postgres"
PASS        = "Sidh@1509"
HOST        = "localhost"
PORT        = "5432"
STARTYEAR   = 2018
ENDYEAR     = 2024


# the first time this is run on a local computer, we'll
# need to run some setup
#   Requires a connection to the db (passed as param)
def init_table_setup(conn):
    sql_helpers.transaction(conn, setup_sql.createSchema)
    sql_helpers.transaction(conn, setup_sql.playerTableCreate)
    sql_helpers.transaction(conn, setup_sql.teamTableCreate)
    sql_helpers.transaction(conn, setup_sql.teamPlayerRelTableCreate)
    sql_helpers.transaction(conn, setup_sql.teamSeasonStatsCreate)
    sql_helpers.transaction(conn, setup_sql.gameTableCreate)
    sql_helpers.transaction(conn, setup_sql.scheduleTableCreate)
    #sql_helpers.transaction(conn, setup_sql.playerGameStatsTableCreate)
    sql_helpers.transaction(conn, setup_sql.playerSeasonStatsTableCreate)
    sql_helpers.transaction(conn, setup_sql.playerCareerStatsTableCreate)
    sql_helpers.transaction(conn, setup_sql.addExtraTeamData)
    sql_helpers.transaction(conn, setup_sql.teamSeasonWithMetadataViewCreate)
    sql_helpers.transaction(conn, setup_sql.fullScheduleDataCreate)
    sql_helpers.transaction(conn, setup_sql.customTeamFunction)
    sql_helpers.transaction(conn, setup_sql.customPlayerFunction)
    sql_helpers.transaction(conn, setup_sql.createCoachImprovmentFunction)


def addTeamsToDb(conn):
    teams = dc.addTeams(conn, STARTYEAR, ENDYEAR)
    sql_helpers.transaction(conn, setup_sql.addExtraTeams)
    return teams

def addAllOtherDataToDb(conn, teams):
    dc.addAllData(conn, teams, STARTYEAR, ENDYEAR)

c = pgre.connect(host=HOST, database=DB, user=USER, password=PASS, port=PORT)
init_table_setup(c)
tms = addTeamsToDb(c)
addAllOtherDataToDb(c, tms)
c.close()