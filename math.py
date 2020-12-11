import statistics as stats
from scipy.stats import norm
import random


class Gaussian:

    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev

    @staticmethod
    def prob_greater(x, y):
        # w refers to x - y
        w_mu = x.mean - y.mean
        w_sigma_squared = x.std_dev**2 + y.std_dev**2
        w_sigma = w_sigma_squared**(1/2)
        z_score = (0 - w_mu)/w_sigma
        probability = 1 - norm.cdf(z_score)
        return probability


class GameProjected(Gaussian):

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


class WeekProjected(Gaussian):

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


# sample_one = []
# sample_two = []
# sample_three = []
# sample_four = []
# for i in range(30):
#     sample_one.append(i * random.random())
#     sample_two.append(i * random.random())
#     sample_three.append(i * random.random())
#     sample_four.append(i * random.random())
#
#
# obi_toppin_per_game_blocks = GameProjected(sample_one)
# immanuel_per_game_blocks = GameProjected(sample_two)
# jayson_per_game_blocks = GameProjected(sample_three)
# jaylen_per_game_blocks = GameProjected(sample_four)
# owner_alex_projected = WeekProjected([obi_toppin_per_game_blocks, immanuel_per_game_blocks], 3)
# owner_michael_projected = WeekProjected([jayson_per_game_blocks, jayson_per_game_blocks], 0)
# print(Gaussian.prob_greater(owner_alex_projected, owner_michael_projected))
