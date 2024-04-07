getTeams = """
    SELECT DISTINCT Name, TeamAbbr
    FROM {0}.team;
"""

getDivs = """
    SELECT DISTINCT Division
    FROM {0}.team;
"""

getConf = """
    SELECT DISTINCT Conference
    FROM {0}.team;
"""

getYears = """
    SELECT DISTINCT Year
    FROM {0}.TeamSeasonStats
    ORDER BY Year;
"""

teamsWhoBeatUs = """
    SELECT Tm.Name, SUB.HomeScore, SUB.AwayScore
    FROM {0}.Team as TM
    INNER JOIN 
    (SELECT G.Winner as TmAb, G.HomeScore, G.AwayScore
    FROM {0}.Game as G
    NATURAL JOIN {0}.Schedule AS Sc
    NATURAL JOIN {0}.Team as T
    WHERE Sc.TeamAbbr = '{1}' AND Sc.Year=2023 AND G.Winner != '{1}') as SUB
    ON SUB.TmAb = TM.TeamAbbr;
"""

teamWithBestRecordInConference = """
    SELECT Name, Wins, Losses
    FROM {0}.TeamSeasonWithMetadata as TSM
    INNER JOIN
    (SELECT Conference
    FROM {0}.Team
    WHERE TeamAbbr = '{1}') as C 
    ON TSM.Conference = C.Conference
    WHERE TSM.Year = 2023
    ORDER BY TSM.Wins DESC
    LIMIT 1
"""

whichTeamsForPlayer = """
    SELECT T.Name as TeamName, TPR.StartYear as Year
    FROM nfldb.TeamPlayerRel as TPR
    NATURAL JOIN nfldb.Player as P
    INNER JOIN nfldb.Team as T on TPR.TeamAbbr = T.TeamAbbr
    INNER JOIN nfldb.playerName as PN on PN.player_id = P.playerid
    WHERE PN.player_Name = %s;
"""

playerCareerStats = """
    SELECT PCS.playerid, PCS.passattempts, PCS.passcompletions, PCS.passyds, PCS.interceptions, PCS.passtds, PCS.fumbles, PCS.rushattempts, PCS.rushyds, PCS.rushtds, PCS.receptions, PCS.rectds, PCS.recyds, PCS.fgattempts, PCS.fgmade
    FROM nfldb.playerCareerStats as PCS
    INNER JOIN nfldb.Player as P ON P.playerid = PCS.playerid
    INNER JOIN nfldb.PlayerName as PN on PN.player_id = P.playerid
    WHERE PN.player_Name = %s;
"""

playerLastYearStats = """
    SELECT PSS.playerid, PSS.PassAttempts, PSS.PassCompletions, PSS.PassYds, PSS.Interceptions, PSS.PassTds, PSS.Fumbles, PSS.RushAttempts, PSS.RushYds, PSS.RushTds, PSS.Receptions, PSS.RecTds, PSS.RecYds, PSS.FgAttempts, PSS.FgMade  
    FROM nfldb.playerSeasonStats as PSS
    INNER JOIN nfldb.Player as P ON P.playerid = PSS.playerid
    INNER JOIN nfldb.PlayerName as PN on PN.player_id = P.playerid
    WHERE PN.player_Name = %s AND PSS.year = 2023;
"""

playerBestTeamByRec = """
    SELECT DISTINCT T.Name, TSS.Year, TSS.Wins, TSS.Losses
    FROM nflDb.TeamPlayerRel as TPR
    NATURAL JOIN nfldb.Player AS P
    INNER JOIN nfldb.teamSeasonStats as TSS ON TSS.teamAbbr = TPR.TeamAbbr
    INNER JOIN nfldb.team as T ON TSS.teamAbbr = T.TeamAbbr
	INNER JOIN nfldb.playername as PN ON PN.player_Id = P.playerId
    WHERE PN.player_name = %s and TSS.Wins =

    (SELECT MAX(TSS.wins)
    FROM nfldb.TeamPlayerRel as TPR
    NATURAL JOIN nfldb.Player AS P
    INNER JOIN nfldb.teamSeasonStats as TSS ON TSS.teamAbbr = TPR.TeamAbbr
    WHERE PN.player_name = %s);
"""

teamWithBestRecordInDivision = """
    SELECT Name, Wins, Losses
    FROM {0}.TeamSeasonWithMetadata as TSM
    INNER JOIN
    (SELECT Division
    FROM {0}.Team
    WHERE TeamAbbr = '{1}') as C 
    ON TSM.Division = C.Division
    WHERE TSM.Year = 2023
    ORDER BY TSM.Wins DESC
    LIMIT 1 
"""

fiveYearBeatUs = """
    SELECT Sub.WC, T.Name
    FROM 
        (SELECT COUNT(winner) as WC, Winner 
        FROM {0}.fullscheduledata
        where loser = '{1}' AND year > 2018
        GROUP BY Winner
        ORDER BY COUNT(Winner) DESC
        LIMIT 1) as Sub
    Inner Join {0}.Team as T
    ON Sub.Winner = T.TeamAbbr;
"""

fiveYearWeBeat = """
    SELECT Sub.LC, T.Name
    FROM 
        (SELECT COUNT(Loser) as LC, Loser 
        FROM {0}.fullscheduledata
        where winner = '{1}' AND year > 2018
        GROUP BY Loser
        ORDER BY COUNT(Loser) DESC
        LIMIT 1) as Sub
    Inner Join {0}.Team as T
    ON Sub.Loser = T.TeamAbbr;
"""