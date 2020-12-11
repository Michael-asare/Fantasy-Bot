import statistics as stats


class G:

    def __init__(self, past_games):
        self.past_games = past_games
        self.mean = 0
        self.std_dev = 1

    def mean(self):
        if len(self.past_games) == 0:
            # do something
            self.mean = 0
        else:
            self.mean = sum(self.past_games)/len(self.past_games)
            
    def standard_deviation(self):
        if len(self.past_games) == 0:
            # do something
            self.std_dev = 1
        else:
            self.std_dev = stats.stdev(self.past_games)