import csv
from datetime import datetime

def save_result(player1, player2, winner):
    with open("scores.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([player1, player2, winner, datetime.now().strftime("%Y-%m-%d")])
