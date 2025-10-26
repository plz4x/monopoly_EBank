print("""Monopoly E-Bank v0.1, a Python program by plz4x
Type "help" to get a quick command reference, or "manual" for how to use this program.""")

money = {
	"p1": 1500,
	"p2": 1500,
	"p3": 1500,
	"p4": 1500
}

while True:
	cmd = input(">>> ")
	cmd_split = cmd.split(" ") # Splits the command into multiple list items
	if cmd.startswith("reset"):
		# reset money (to 1500), properties
		money = {
		"p1": 1500,
		"p2": 1500,
		"p3": 1500,
		"p4": 1500
	}
		print("All player money has been reset to M1500.")
		continue
	
	elif cmd.startswith("manual"):
		manual = [
			"""Welcome to the Monopoly E-Bank Manual.
This manual will teach you all of this CLI's commands.
If you only need a quick overview, type "quit", an then "help".""",

			"""1. COMMANDS FOR MANAGING MONEY
reset: Resets all player money to M1500.
add: Adds money to the stated player from the bank.
EXAMPLE: add p1 50 -- Gives M50 to player 1
subt: Subtracts money to the stated plater. That money goes to the bank.
EXAMPLE: subt p1 50 -- Sibtracts M50 from player 1
go: Gives M200 to the stated player. Used as a shortcut from "add p1 200".
EXAMPLE: go p1 -- Gives M200 to player 1
set: Sets the stated player's money to the stated amount.
EXAMPLE: set p1 300 -- Sets player 1's amount to M300.""",
			"""trans: Transfers money from one player to another.
EXAMPLE: trans p2 p4 10 -- Transfers M10 from player 2 to player 4.
vm: Short for "View Money", lets you see the amount of money one player has.
EXAMPLE: vm p1 -- Shows the amount of money player 1 has.
EXAMPLE: vm all -- Shows the amount of money everyone has.""",
			"""2. OTHER MISCELLANEOUS COMMANDS
help: Shows a quick overview of the commands.
manual: Shows a tutorial on how to use the program.
changelog: Shows the program changelog.
exit: Stops the program."""

		]
		for paragraph in manual:
			print(paragraph)
			print("Press enter to continue or type \"quit\" to return to the CLI.")
			mcmd = input(">>> ")
			if mcmd == "quit":
				break
		print("""You are now leaving the manual and returning to the CLI.
If at any time you need a quick review of the commands, type "help".""")
		continue
		
	elif cmd.startswith("changelog"):
		print("""PROGRAM CHANGELOG
v1.0 (26/10/2025): Initial release <-- CURRENT VERSION
v1.1 (FUTURE): Add player renaming.
v2.0 (FUTURE): Add property management""")
		continue
		
	elif cmd.startswith("help"):
		print("""QUICK COMMAND HELP
reset: Resets all money and properties.
add p1 100: Adds M100 to player 1.
subt p1 100: Subtracts M100 from player 1.
go p1: Gives M200 to player 1.
set p1 2000: Sets player 1's money to M2000.
trans p1 p2 10: Transfers M10 from player 1 to player 2.
vm p1: Shows player 1's money.
vm all: Shows every player's money.
exit: Quits the program.""")
		continue
		
	elif cmd.startswith("exit"):
		quit()
	
	try:
		if cmd.startswith("add"):
			money[cmd_split[1]] += int(cmd_split[2]) # Adds money
			print(f"""M{cmd_split[2]} added to {cmd_split[1]}.
{cmd_split[1]}'s current total money: M{money[cmd_split[1]]}""") # This print line displays command data; how much money was added, etc.
		
		elif cmd.startswith("subt"):
			money[cmd_split[1]] -= int(cmd_split[2])
			print(f"""M{cmd_split[2]} subtracted from {cmd_split[1]}.
{cmd_split[1]}'s current total money: M{money[cmd_split[1]]}""")
			
		elif cmd.startswith("trans"):
			money[cmd_split[1]] -= int(cmd_split[3])
			money[cmd_split[2]] += int(cmd_split[3])
			print(f"""M{cmd_split[3]} transferred from {cmd_split[1]} to {cmd_split[2]}.
{cmd_split[1]}'s current total money: M{money[cmd_split[1]]}
{cmd_split[2]}'s current total money: M{money[cmd_split[2]]}""")
		
		elif cmd.startswith("go"):
			money[cmd_split[1]] += 200
			print(f"M200 added to {cmd_split[1]}")
		
		elif cmd.startswith("set"):
			money[cmd_split[1]] = int(cmd_split[2])
			print(f"""{cmd_split[1]}'s money set to M{cmd_split[2]}.""")
	
		elif cmd.startswith("vm"):
			if cmd_split[1] == "all":
				print(f"""ALL PLAYER CURRENT TOTAL MONEY:

p1: M{money["p1"]}
p2: M{money["p2"]}
p3: M{money["p3"]}
p4: M{money["p4"]}""")
			else:
				print(f"""{cmd_split[1]}'s current total money: M{money[cmd_split[1]]}""")

		else:
			print(f"ERROR: Unknown command \"{cmd_split[0]}\"")
			
	except KeyError:
		if cmd.startswith("trans"):
			print(f"ERROR: Invalid transfer origin/destination \"{cmd_split[1]} {cmd_split[2]}\"")
		else:
			print(f"ERROR: Nonexistent player \"{cmd_split[1]}\"")

	except ValueError:
		if cmd.startswith("trans"):
			print(f"ERROR: Invalid money value \"{cmd_split[3]}\"")
		else:
			print(f"ERROR: Invalid money value \"{cmd_split[2]}\"")