﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg forest = "img/bg_forest.png"

# The game starts here.
label start:
    $ romance_snowWhite = 0
    $ romance_redRidingHood = 0
    $ romance_shrek = 0

    play music "bgm/bg.ogg"
    
    $ player_name = renpy.input("My lady, what is your name?").strip()
    if player_name == "":
        $ player_name = "Default"

    player "My name is %(player_name)s! Who are you?"
    unknown "Don't mind me. Please enjoy your stay here."
    jump scene1
    
label end:
    "Game over, you died."
