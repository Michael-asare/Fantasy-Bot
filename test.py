import matchup_stats as ms

game_data = []
game_projections = []
for i in range(32):
    game = []
    for j in range(30):
        game.append((j - i)**2)
    game_data.append(game)
    game_projections.append(ms.GameProjected(game_data[i]))

alex_weekp = []
michael_weekp = []
for i in range(0, 32, 2):
    if i < 16:
        alex_weekp.append(ms.WeekProjected([game_projections[i], game_projections[i + 1]], 0))
    else:
        michael_weekp.append(ms.WeekProjected([game_projections[i], game_projections[i + 1]], 0))

prob_points = ms.Gaussian.prob_greater(alex_weekp[0], michael_weekp[0])
prob_asts = ms.Gaussian.prob_greater(alex_weekp[1], michael_weekp[1])
prob_rebs = ms.Gaussian.prob_greater(alex_weekp[2], michael_weekp[2])
prob_steals = ms.Gaussian.prob_greater(alex_weekp[3], michael_weekp[3])
prob_blks = ms.Gaussian.prob_greater(alex_weekp[4], michael_weekp[4])
prob_3pm = ms.Gaussian.prob_greater(alex_weekp[5], michael_weekp[5])
prob_fg = ms.Gaussian.prob_greater(alex_weekp[6], michael_weekp[6])
prob_ft = ms.Gaussian.prob_greater(alex_weekp[7], michael_weekp[7])

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
# print(Gaussian.prob_greater(owner_alex_projected, owner_michael_projected))