import random


def match_manitto(participants):
    manitto_matchings = {}
    remain_members = participants

    for participant in participants:
        while True:
            manitto = random.choice(remain_members)
            if manitto != participant:
                break
        manitto_matchings[participant] = manitto

    return manitto_matchings


participants_file = open("participants.txt", "r")
participants = participants_file.read().split("\n")
