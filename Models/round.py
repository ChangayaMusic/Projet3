import datetime
import random
from match import Match
from tournament import Tournament
from player import Player


class Round:
    match_list = []
    round_date_hour_start = ''
    round_date_hour_end = ''
    round_score = [] 
    round_player_list = []
    

def __init__(self, match_list, round_date_hour_start, round_date_hour_end, round_score, round_player_list):
    self.match_list = match_list
    self.round_date_hour_start = round_date_hour_start
    self.round_date_hour_end = round_date_hour_end 
    self.round_score = round_score
    self.round_player_list = round_player_list
  
    
def start_time(self, round_date_hour_start):
    now = datetime.datetime.now()
    round_date_hour_start = now.strftime("%Y-%m-%d %H:%M:%S")

def end_time(self, round_date_hour_end):
    now = datetime.datetime.now()
    round_date_hour_end = now.strftime("%Y-%m-%d %H:%M:%S")
    
def first_round_mix(self, round_player_list):
    round_player_list = random.shuffle(Tournament.player_list)
    
def generate_round_matches(self, round_player_list, match_list):
    
    while len(round_player_list) > 0:
        
        player_1 = round_player_list[0]
        player_2 = round_player_list[1]
        match_list.append([player_1,player_2])
        round_player_list.remove(player_1, player_2)

def player_by_points_mix(self, round_player_list):
    round_player_list = Tournament.player_list.sort(key=lambda x: Player.points)
    
    


        
        
    
    
    
    
        
    
    
    
    
    
        
    
    
    
    