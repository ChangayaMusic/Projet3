import datetime


class Tournament:
    def __init__(self, tournament_name, nb_rounds=4, **kwargs):
        self.tournament_name = tournament_name
        self.place = kwargs.get("place", "")
        self.description = kwargs.get("description", "")
        self.nb_rounds = nb_rounds
        self.current_round = 0
        self.rounds = []
        self.players = []
        
    

    @property
    def start_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def end_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
