from random import choice
from os import system
from time import sleep


def match_manitto(participants):
    manitto_matchings = {}
    remain_members = participants

    matched_members = []
    for participant in participants:
        while True:
            manitto = choice(remain_members)
            if manitto != participant and manitto not in matched_members:
                break

        manitto_matchings[participant] = manitto
        matched_members.append(manitto)

    return manitto_matchings


def get_participants():
    participants_file = open("participants.txt", "r")
    participants = participants_file.read().split("\n")
    participants.remove("")
    return participants


if __name__ == "__main__":
    participants = get_participants()
    print(get_participants())
    manitto_matchings = match_manitto(participants)

    while True:
        try:
            name = input("이름을 입력하세요: ")
        except Exception:
            continue

        if name not in manitto_matchings.keys():
            print("참가자 명단에서 이름을 찾을 수 없습니다. 올바른 이름을 다시 입력해 주세요.")
            continue

        print(name + "님의 마니또는 " + manitto_matchings[name] + "입니다.")
        print("3초 뒤에 문구가 사라집니다.")

        sleep(3)
        system("clear")
