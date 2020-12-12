import matchup_stats as ms
import random as rand

cat_data = []
game_projections = []
for i in range(32):
    thirty_game_cat_stats = []
    for j in range(30):
        thirty_game_cat_stats.append(i * j)
    cat_data.append(thirty_game_cat_stats)
    game_projections.append(ms.GameProjected(cat_data[i]))

alex_weekp = []
michael_weekp = []
for i in range(0, 32, 2):
    if i < 16:
        alex_weekp.append(ms.WeekProjected([game_projections[i], game_projections[i + 1]], 0))
    else:
        michael_weekp.append(ms.WeekProjected([game_projections[i], game_projections[i + 1]], 0))

prob_points = alex_weekp[0].prob_greater_than_distribution(michael_weekp[0])
prob_asts = alex_weekp[1].prob_greater_than_distribution(michael_weekp[1])
prob_rebs = alex_weekp[2].prob_greater_than_distribution(michael_weekp[2])
prob_steals = alex_weekp[3].prob_greater_than_distribution(michael_weekp[3])
prob_blks = alex_weekp[4].prob_greater_than_distribution(michael_weekp[4])
prob_3pm = alex_weekp[5].prob_greater_than_distribution(michael_weekp[5])
prob_fg = alex_weekp[6].prob_greater_than_distribution(michael_weekp[6])
prob_ft = alex_weekp[7].prob_greater_than_distribution(michael_weekp[7])

dict = {"points": prob_points,
        "assists": prob_asts,
        "rebounds": prob_rebs,
        "steals": prob_steals,
        "blocks": prob_blks,
        "3pm": prob_3pm,
        "fg": prob_fg,
        "ft": prob_ft}

wL = ms.WinLossProjected(dict)
print(wL.win_probability)
#
#
# obi_toppin_per_game_blocks = GameProjected(sample_one)
# immanuel_per_game_blocks = GameProjected(sample_two)
# jayson_per_game_blocks = GameProjected(sample_three)
# jaylen_per_game_blocks = GameProjected(sample_four)
# owner_alex_projected = WeekProjected([obi_toppin_per_game_blocks, immanuel_per_game_blocks], 3)
# owner_michael_projected = WeekProjected([jayson_per_game_blocks, jayson_per_game_blocks], 0)
# print(Gaussian.prob_greater_than_distribution(owner_alex_projected, owner_michael_projected))