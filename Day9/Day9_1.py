players_number = 468
number_of_rounds = 71010
circle = [0]
players = {x : 0 for x in range(1, players_number + 1)}
current_marble_index = 0
iter = 1
while iter <= number_of_rounds:
    marble = iter
    if marble % 23 == 0:
        current_marble_index = (current_marble_index - 7) % len(circle)
        players[( (marble - 1) % players_number) + 1] += marble + circle[current_marble_index]
        del circle[current_marble_index]
    else:
        index = (current_marble_index + 2)
        if index == len(circle) or len(circle) == 1:
            circle.append(marble)
        else:
            circle.insert(index % len(circle), marble)
        current_marble_index = circle.index(marble)
    if marble % 50000 == 0:
        print(marble)
    # print("P: ", ( (marble - 1) % players_number) + 1, circle)
    iter += 1

# print(players)
print(players[max(players, key=lambda k : players[k])])