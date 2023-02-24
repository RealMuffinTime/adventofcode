import datetime
import os
import requests
import webbrowser


def setup(input_date):
    year, month, day = input_date
    address = f"https://adventofcode.com/{year}/day/{str(int(day))}"
    session = ""  # you can paste your session cookie here
    if session == "":
        session = input("Please input your session cookie:")

    if not os.path.exists(f"{year}/"):
        print(f"Creating folder for year {year}.")
        os.makedirs(f"{year}/")
    else:
        print(f"Already existing folder for {year}.")

    if not os.path.exists(f"{year}/day{day}.py"):
        with open(f"{year}/day{day}.py", mode="w+") as file:
            print(f"Creating python file for day {day}, and opening {address}")
            file.write(f"# Advent of code {year} day {day} have fun.\n"
                       f"# {address}\n"
                       f"\n"
                       f'with open("input{day}") as file:\n'
                       f'    for line in file.readlines():\n')
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


date = str(datetime.date.today()).split("-")

if date[1] != "12":
    print("It's not december my friend.")
    days = datetime.date(int(date[0]), 12, 1) - datetime.date.today()
    print(f"You need to wait {days.days} days until december!")
    print("Or do you want to make some older puzzles?")
    date = None
    while date is None:
        temp_date = input("Please provide the date: ")
        try:
            date = str(datetime.datetime.strptime(temp_date, '%Y-%m-%d').date()).split("-")
            if date[1] != "12" or int(date[2]) < 1 or int(date[2]) > 25:
                print("This not a day for a AdventOfCode Puzzle. Please try again.")
                date = None
        except ValueError:
            print("Date recognition failed. Please try again. Format: yyyy-mm-dd")
            date = None
else:
    print("It's december. It's codin time!")

setup(date)

print("Have a noice day. :)")
