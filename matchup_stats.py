import statistics as stats
from scipy.stats import norm
import random


class Distribution:

    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev

    @staticmethod
    def determine_mean(data):
        return sum(data)/len(data) if len(data) != 0 else None

    @staticmethod
    def determine_std_dev(data):
        return stats.stdev(data) if len(data) != 0 else None


class Gaussian(Distribution):

    def __init__(self, mean, std_dev):
        super.__init__(mean, std_dev)

    @staticmethod
    def prob_greater(x, y):
        # w refers to x - y
        w_mu = x.mean - y.mean
        w_sigma_squared = x.std_dev**2 + y.std_dev**2
        w_sigma = w_sigma_squared**(1/2)
        z_score = (0 - w_mu)/w_sigma
        probability = 1 - norm.cdf(z_score)
        return probability

    @staticmethod
    def sum_random_variables(random_variables):
        gaussian_sum_variable = Gaussian(0, 1)
        for random_variable in random_variables:
            gaussian_sum_variable.mean += random_variable.mean

        sum_variances = 0
        for random_variable in random_variables:
            sum_variances += random_variable.std_dev**2
        gaussian_sum_variable.std_dev = sum_variances**(1/2)
        return gaussian_sum_variable


class GameProjected(Gaussian):

    def __init__(self, past_games):
        super().__init__(0, 1)
        self.past_games = past_games
        self.get_stats()

    def get_stats(self):
        self.x_bar()
        self.s()

    def x_bar(self):
        self.mean = Distribution.determine_mean(self.past_games) # may return None

    def s(self):
        self.std_dev = Distribution.determine_std_dev(self.past_games) # may return None


class WeekProjected(Gaussian):

    def __init__(self, games_to_be_played, week_to_date):
        super().__init__(0, 1)
        self.games = games_to_be_played
        self.offset = week_to_date
        self.sum_games()

    def sum_games(self):
        sum_random_variables = Gaussian.sum_random_variables(self.games)
        self.mean = sum_random_variables.mean + self.offset
        self.std_dev = sum_random_variables.std_dev


class WinLossProjected:

    def __init__(self, probs): # probs = {"points": 0.125, ,"assists": 0.125, ..., "ft": 0.125}
        self.probs = probs
        self.event_space = WinLossProjected.all_events()
        self.win_probability = []
        self.all_probabilities()

    def chance_win(self, wins):
        return self.win_probability[wins]

    def all_probabilities(self):
        all_probs = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for event in self.event_space: # event = {"points": True, "assists": False, ..., "ft" : False} -> (0.125)*(1-0.125)*....*(1-0.125) = event probabilty
            event_wins = 0
            event_prob = 1
            for key in self.probs:
                if event[key]:
                    event_prob *= self.probs[key]
                    event_wins += 1
                else:
                    event_prob *= 1 - self.probs[key]
            all_probs[event_wins] += event_prob
        self.win_probability = all_probs

    @staticmethod
    def all_events():
        sample_space = []
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        for m in range(2):
                            for n in range(2):
                                for o in range(2):
                                    for p in range(2):
                                        event = {"points": bool(i),
                                                 "assists": bool(j),
                                                 "rebounds": bool(k),
                                                 "blocks": bool(l),
                                                 "steals": bool(m),
                                                 "3pm": bool(n),
                                                 "fg": bool(o),
                                                 "ft": bool(p)}
                                        sample_space.append(event)
        return sample_space

