from collections import deque

players_number = 468
number_of_rounds = 7101000
circle = deque([0])
players = {x : 0 for x in range(1, players_number + 1)}
current_marble_index = 0
iter = 1
while iter <= number_of_rounds:
    marble = iter
    if marble % 23 == 0:
        circle.rotate(7)
        players[( (marble - 1) % players_number) + 1] += marble + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)
    # print("P: ", ( (marble - 1) % players_number) + 1, circle)
    iter += 1

# print(players)
print(players[max(players, key=lambda k : players[k])])