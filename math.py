import statistics as stats


class Gaussian:

    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev


class G(Gaussian):

    def __init__(self, past_games):
        super().__init__(0, 1)
        self.past_games = past_games
        self.get_stats()

    def get_stats(self):
        self.x_bar()
        self.s()

    def x_bar(self):
        if len(self.past_games) == 0:
            # do something
            self.mean = 0
        else:
            self.mean = sum(self.past_games)/len(self.past_games)
            
    def s(self):
        if len(self.past_games) == 0:
            # do something
            self.std_dev = 1
        else:
            self.std_dev = stats.stdev(self.past_games)


class W(Gaussian):

    def __init__(self, games_to_be_played, week_to_date):
        super().__init__(0, 1)
        self.games = games_to_be_played
        self.offset = week_to_date
        self.sum_games()

    def sum_games(self):
        for game in self.games:
            self.mean += game.mean
        self.mean += self.offset

        sum_variances = 0
        for game in self.games:
            sum_variances += game.std_dev**2
        self.std_dev = sum_variances**(1/2)
