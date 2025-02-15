import numpy as np

def monty_hall(N, switch=True):
    wins = 0
    for _ in range(N):
        doors = [0, 0, 1]  # Randomly shuffle doors, 1 = car, 0 = goat
        np.random.shuffle(doors)

        choice = np.random.randint(0, 3)  # Contestant's initial choice
        available_goats = [i for i in range(3) if doors[i] == 0 and i != choice]  
        monty_opens = np.random.choice(available_goats)  # Monty opens a goat door

        if switch:
            remaining_door = next(i for i in range(3) if i not in {choice, monty_opens})
            choice = remaining_door  # Contestant switches

        if doors[choice] == 1:
            wins += 1

    return wins / N  # Probability of winning

N = 10000
print("Winning probability when switching :", monty_hall(N, switch=True))
print("Winning probability when staying   :", monty_hall(N, switch=False))
