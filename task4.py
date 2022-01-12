# Reads a csv file with teams and points and prints a league table
# Also accpet a command line argument to print the heading of the table
 
# Rule1. Teams play each other once.
# Rule2. Teams are awarded three points for winning, one for a draw, and none for losing.
# Rule3. Teams score goals (points) in each game, and the difference between the number scored and the number conceded is calculated.
# Rule4. The final table is based on the number on "win/loss" points, with the "difference" used to separate otherwise equal teams.

import sys

CSV_FILE = "test.csv"

class Team:
     def __init__(self, name):
         self.name = name
         self.points = 0
         self.played = 0
         self.wins = 0
         self.loss = 0
         self.draw = 0
         self.goals_for = 0
         self.goals_against = 0
        
class Match:
     def __init__(self, home_team, away_team, home_goals, away_goals):
         self.home_team = home_team
         self.away_team = away_team
         self.home_goals = home_goals
         self.away_goals = away_goals
 
class League:
     def __init__(self, league_file):
         self.file = league_file
         self.matches = self.read_file()
         self.teams = self.get_teams()
  
     def read_file(self):
         """
         Reads the csv file of two team match results and return list of Match objects
         """
         matches = []
         with open(self.file, "r") as f:
            for line in f:
                 line = line.strip()
                 if line:
                      home_team, home_goals, away_team, away_goals = line.split(",")
                      match = Match(home_team, away_team, int(home_goals), int(away_goals))
                      matches.append(match)
  
         return matches
  
     def get_teams(self):
          """
          Returns a list of team objects
          """
          teams = []
          for match in self.matches:
              # Check if team is already in list
              # Only process home team since all teams play as home team once
              if match.home_team not in [team.name for team in teams]:
                  teams.append(Team(match.home_team))
          return teams
  
     def get_team(self, team_name):
          """
          Returns the team object with the given name
          """
          req_team = Team("")
          for team in self.teams:
              if team.name == team_name:
                  req_team = team
  
          if req_team.name == "":
              raise ValueError("Team not found")
          
          return req_team
                
     def process_matches(self):
          """
          Processes the matches and updates the teams
          """
          for match in self.matches:
              home_team = self.get_team(match.home_team)
              away_team = self.get_team(match.away_team)
              home_team.played += 1
              away_team.played += 1
              if match.home_goals > match.away_goals:
                  home_team.wins += 1
                  home_team.points += 3
                  away_team.loss += 1
              elif match.home_goals < match.away_goals:
                  away_team.wins += 1
                  away_team.points += 3
                  home_team.loss += 1
              else:
                 home_team.draw += 1
                 away_team.draw += 1
                 home_team.points += 1
                 away_team.points += 1
              home_team.goals_for += match.home_goals
              home_team.goals_against += match.away_goals
              away_team.goals_for += match.away_goals
              away_team.goals_against += match.home_goals
 
     def print_table(self, heading=None):
         """
         Prints the league table in descending order of points
         """
         self.process_matches()
         if heading:
             print(heading)
             print("=" * len(heading))
 
         print("Teams                         | P | W | D | L |  F |  A | Diff | Pts")
         print("--------------------------------------------------------------------")
         # sort teams by descending points, then by descending difference and then by goals for and then name
         sorted_teams = sorted(self.teams, key=lambda team: (-team.points, -team.goals_for + team.goals_against, -team.goals_for, team.name))
 
         for team in sorted_teams:
              print(
                 "{:<30}|{:>2} |{:>2} |{:>2} |{:>2} |{:>3} |{:>3} |{:>5} |{:>4}".format(
                     team.name,
                     team.played,
                     team.wins,
                     team.draw,
                     team.loss,
                     team.goals_for,
                     team.goals_against,
                     team.goals_for - team.goals_against,
                     team.points,
                 )
             )
 
 
if __name__ == "__main__":
     cmd_args = sys.argv[1:]
     heading = None
     if len(cmd_args) == 1:
         heading = cmd_args[0]
     league = League(CSV_FILE)
     league.print_table(heading=heading)