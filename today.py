import datetime
import os
import requests
import webbrowser

year, month, day = str(datetime.date.today()).split("-")
address = f"https://adventofcode.com/{year}/day/{day.strip('0')}"
session = ""  # you can paste your session cookie here
if session == "":
    session = input("Please input your session cookie:")

if month != "12":
    print("It's not december my friend.")
    days = datetime.date(int(year), 12, 1) - datetime.date.today()
    print(f"You need to wait {days.days} days until december. :)")
    exit()
else:
    print("It's december. It's codin time!")

if not os.path.exists(f"{year}/"):
    print(f"Creating folder for year {year}.")
    os.makedirs(f"{year}/")
else:
    print(f"Already existing folder for {year}.")

if not os.path.exists(f"{year}/day{day}.py"):
    with open(f"{year}/day{day}.py", mode="w+") as file:
        print(f"Creating python file for day {day}, and opening {address}")
        file.write(f"# Advent of code {year} day {day} have fun.\n# {address}\n")
        webbrowser.get().open_new(address)

else:
    print(f"Already existing python file for day {day}, you may want to open {address}.")

if not os.path.exists(f"{year}/input{day}"):
    puzzle_input = requests.get(f"{address}/input", cookies={'session': f'{session}'})
    if not puzzle_input.text.startswith("Puzzle inputs differ by user."):
        with open(f"{year}/input{day}", mode="w+") as file:
            print(f"Creating input file for day {day}, and writing requested input.")
            file.write(puzzle_input.text)
    else:
        print("Faulty session cookie, could not create input file.")
else:
    print(f"Already existing input file for day {day}.")

print("Have a noice day. :)")
