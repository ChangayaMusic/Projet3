import random
from tournament import Tournament
from enum import IntEnum

class ResultMatch(IntEnum):
    PLAYER_1_WINS = 0
    PLAYER_2_WINS = 1
    EQUALITY = 2

class Match:
    
    match_player_1 = ''
    match_player_2 = ''
    match_player_1_score = 0
    match_player_2_score = 0
    is_equality = False 
    winner = ''
    
    @property
    def is_equality(self):
        return self.match_player_1_score != 0 and self.match_player_2_score != 0 \
               and self.match_player_1_score == self.match_player_2_score

    def set_result(self, result):
        if result == ResultMatch.PLAYER_1_WINS:
            self.match_player_1_score = 1
        elif result == ResultMatch.PLAYER_2_WINS:
            self.match_player_2_score = 1
        elif result == ResultMatch.EQUALITY:
            self.match_player_1_score = self.match_player_2_score = 0.5
        else:
            raise ValueError("Unknown result match value")
 
def __init__(self, match_player_1, match_player_2, match_player_1_score, match_player_2_score, equality, winner, player_1_list, player_2_list):
    self.match_player_1 = match_player_1
    self.match_player_2 = match_player_2
    self.match_player_1_score = match_player_1_score
    self.match_player_2_score = match_player_2_score
    self.equality = equality  
    self.winner = winner
    self.player_1_list = player_1_list
    self.player_2_list = player_2_list
    
def attribute_players(self, player_list, match_player_1, match_player_2,player_1_list, player_2_list):
    player_list = Tournament.player_list
    match_player_1 = random.choice(player_list)
    player_1_list.append(match_player_1)
    player_list.remove(match_player_1)
    match_player_2 = random.choice(player_list)
    player_2_list.append()


if __name__ == "__main__":
    # We are in controller Match
    match = Match()
    print(match.match_player_1_score, match.match_player_2_score, match.is_equality)
    # MatchMenuView.Display_input_result
    result = input(
        "Which is the result of the match ?\n"
        "0: Player 1 wins\n"
        "1: Player 2 wins\n"
        "2: Equality\n"
    )
    # Call Match model modification
    match.set_result(int(result))
    print(match.match_player_1_score, match.match_player_2_score, match.is_equality)