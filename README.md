# Monopoly EBank Manual
Written by plz4x

### (UNFINISHED, USE THE `manual` COMMAND FOR A GUIDE TO HOW TO USE THE PROGRAM)

# Part I: Introductory Chapters

## Chapter 1: Introduction
### About The Program
The Monopoly EBank is a command line interface that closely resembles the Monopoly Bank. The difference between the physical Bank and this program is that the EBank is entirely cashless and also has an infinite amount of money.

### Why This Program?
Whenever I play Monopoly, I have to turn off the fans and close the windows in the room so as to avoid the money flying around, making it sweltering hot inside. As for the air conditioner, I usually don't turn it on becuase it kind of was unnecessary i guess :/

It's also such a pain to count the money manually and give change and you know, stuff like that.

So I've created this program as a solution to these problems. Sure, other people obviously **have** created these sorts of programs before, but well I love programming and I want to try to make one myself.

And so there you have it. The purpose of this program, i guess.

### Why This Manual?
And by that I mean, why put the manual *here* instead of *in* the program itself?

The answer is simple: Readability.

There used to be a `manual` command in the CLI showing how to use the program, and a `help` command giving you a quick reference to the commands. However, they were a bit hard to read.

The manual looked something like this:

```
--snip--
1. COMMANDS FOR MANAGING MONEY
reset: Resets all player money to M1500.
add: Adds money to the stated player from the bank.
EXAMPLE: add p1 50 -- Gives M50 to p1
subt: Subtracts money to the stated plater. That money goes to the bank.
EXAMPLE: subt p1 50 -- Subtracts M50 from p1
go: Gives M200 to the stated player. Used as a shortcut from "add p1 200".
EXAMPLE: go p1 -- Gives M200 to p1
set: Sets the stated player's money to the stated amount.
EXAMPLE: set p1 300 -- Sets p1's amount to M300.
Press enter to continue or type "quit" to return to the CLI.
--snip--
```

It *is* rather readable, but I felt that it would be better to put the manual in a `.md` file, as these types of files present their text like a Wikipedia article.

So here you have it.

`manual.md`.

## Chapter 2: Downloading

You may skip this chapter if you have already downloaded the program.

To download the program:

1. Go to https://github.com/plz4x/monopoly_EBank.
2. Click the green "<> Code" button.
3. In the menu that appears, click "Download ZIP" at the bottom of the menu.
4. In your file explorer, right click on the ZIP file called `monopoly_EBank-main.zip` (it will most likely be in the "Downloads" folder) and click "Extract All".
5. If you see a window asking you where to put the extracted folder, just ignore it and click "Extract". 
6. The ZIP file will turn into a folder which will automatically open in another window. In it will be another folder called `monopoly_EBank-main`. Double-click the folder.
7. In the folder should be five files: `LICENSE.md`, `README.md`, `manual.md`, `Monopoly-EBank.py` and `pdata.json`. Double-click `Monopoly-EBank.py`.
8. If it appears in a terminal window and you see the following text:
```
(insert prompt here)
```
then you are good to go! You can start using the program.
9. But if it opens in a coding app, like VS Code or IDLE, click the "Run" button in the app. Then you can start using the program!

# Part II: Commands

## Chapter 3: Quick Reference

If you already know the commands, and you only need a quick reference, refer to this chapter.

*Insert quick reference here*

## Chapter 4: Commands for Managing Money



## Version history

v1.0 (26/10/2025): Initial release, can only handle money.

v1.1 (29/10/2025): Added player renaming and fixed a minor spelling error. Also did a bugfix.

v1.2 (31/10/2025): Did a bugfix.

v1.3 (07/11/2025): Added ltax and itax commands and did a bugfix. <-- CURRENT VERSION

v2.0 (FUTURE): Add property management.
