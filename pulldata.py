#pull data
import requests
import csv
#Setup
api_key = "19f8fbedf0bd425081706a7d35d54fde"

sql = """
INSERT INTO games (StatID, TeamID, SeasonType, Season, Name, Team, GlobalTeamID, GameID, OpponentID, Opponent, Day, DateTime, HomeOrAway, IsGameOver, GlobalGameID, GlobalOpponentID, Updated, Games, FantasyPoints, AtBats, Runs, Hits, Singles, Doubles, Triples, HomeRuns, RunsBattedIn, BattingAverage, Outs, Strikeouts, Walks, HitByPitch, Sacrifices, SacrificeFlies, GroundIntoDoublePlay, StolenBases, CaughtStealing, PitchesSeen, OnBasePercentage, SluggingPercentage, OnBasePlusSlugging, Errors, Wins, Losses, Saves, InningsPitchedDecimal, TotalOutsPitched, InningsPitchedFull, InningsPitchedOuts, EarnedRunAverage, PitchingHits, PitchingRuns, PitchingEarnedRuns, PitchingWalks, PitchingStrikeouts, PitchingHomeRuns, PitchesThrown, PitchesThrownStrikes, WalksHitsPerInningsPitched, PitchingBattingAverageAgainst, GrandSlams, FantasyPointsFanDuel, FantasyPointsDraftKings, FantasyPointsYahoo, PlateAppearances, TotalBases, FlyOuts, GroundOuts, LineOuts, PopOuts, IntentionalWalks, ReachedOnError, BallsInPlay, BattingAverageOnBallsInPlay, WeightedOnBasePercentage, PitchingSingles, PitchingDoubles, PitchingTriples, PitchingGrandSlams, PitchingHitByPitch, PitchingSacrifices, PitchingSacrificeFlies, PitchingGroundIntoDoublePlay, PitchingCompleteGames, PitchingShutOuts, PitchingNoHitters, PitchingPerfectGames, PitchingPlateAppearances, PitchingTotalBases, PitchingFlyOuts, PitchingGroundOuts, PitchingLineOuts, PitchingPopOuts, PitchingIntentionalWalks, PitchingReachedOnError)
VALUES (%s, %s, ..., %s);
"""

team_data = {1: 'Dodgers', 2: 'Reds', 3: 'Blue Jays', 4: 'Pirates', 5: 'Royals', 9: 'Cubs', 10: 'Guardians', 11: 'Rays', 12: 'Phillies', 13: 'Mariners', 14: 'Diamondbacks', 15: 'Giants', 16: 'White Sox', 17: 'Tigers', 18: 'Mets', 19: 'Orioles', 20: 'Twins', 21: 'Angels', 22: 'Marlins', 23: 'Rockies', 24: 'Athletics', 25: 'Red Sox', 26: 'Braves', 28: 'Rangers', 29: 'Yankees', 30: 'Astros', 31: 'Cardinals', 32: 'Brewers', 33: 'Padres', 35: 'Nationals'}
team_ids = list(team_data.keys())

all_data = [dictionary for team_id in team_ids 
            for dictionary in requests.get(f"https://api.sportsdata.io/v3/mlb/scores/json/TeamGameStatsBySeason/2024/{team_id}/all?key={api_key}").json()]

        
csv_file = 'games.csv'

with open(csv_file, mode = 'w', newline = '') as file:
    writer = csv.DictWriter(file,fieldnames = all_data[0].keys())
    writer.writeheader()
    writer.writerows(all_data)
print('done')
