import numpy as np
#NBA player stats analysis

#Generating synthetic data
def generate_data():
    points = np.random.randint(5,40, size=(5,10))
    print(f'Points:{points}')
    assists = np.random.randint(0,15, size=(5,10))
    print(f'Assists: {assists}')
    rebounds = np.random.randint(0,20, size=(5,10))
    print(f'Rebounds: {rebounds}')
    return points,assists,rebounds

#Analysis
def average(points,assists,rebounds): #Player Averages
    average_points = np.mean(points, axis=1)
    print(f'Average point per player: {average_points}')  

    average_assists = np.mean(assists, axis = 1)
    print(f'Average assist per player: {average_assists}')

    average_rebounds = np.mean(rebounds, axis = 1)
    print(f'Average rebound per player: {average_rebounds}')
points,assists,rebounds = generate_data()
average(points,assists,rebounds)


 #Points in every game
def total(points):
    game_total = np.sum(points, axis=0) 
    print(f'Points in every game: {game_total}')
total(points)


#Best performance
def performance(points):
    highest_single_game_point = np.max(points) 
    print(f'The player with the highest game point has: {highest_single_game_point}')
performance(points)

#Consistency Check
def consistency(points):
    std_per_player = np.std(points, axis=1)
    print(f'The consistency of the players are:{std_per_player}')
    most_consistent_player = np.argmin(std_per_player)
    print(f'The most consistent player has an index of: {most_consistent_player}')
consistency(points)

#Efficiency rating
def avg_efficiency(points,assists,rebounds):
    efficiency = points + 0.7 * rebounds + 0.5 * assists
    avg_efficiency = np.mean(efficiency, axis=1)
    print(f'Average efficiency per player is: {avg_efficiency}')
    return avg_efficiency


#Leaderboard
def leaderboard(avg_efficiency):
    ranking = np.argsort(avg_efficiency)[::-1] #Players are sorted in descending order, results are shown according to their index
    print(f'Average efficiency per player is(according to index): {ranking}') 
avg_eff = avg_efficiency(points,assists,rebounds)
leaderboard(avg_eff)

#Highest scoring team
def highest(points):
    team_totals = np.sum(points, axis=0)
    highest_total = np.max(team_totals)
    game_index = np.argmax(team_totals)
    print(f'Team totals per game: {team_totals}')
    print(f'The highest scoring team is (according to index): {game_index} ')
highest(points)
