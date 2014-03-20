# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# The game starts here.
label start:
    
    $ player_name = renpy.input("What is your name?").strip()
    if player_name == "":
        $ player_name = "Default"
    
    player "My name is %(player_name)s!"
    snowWhite ";_;"
    femaleWolf "You look... tasty"
    redRidingHood "Hey hottie"
    cinderella "Be gentle..."
    shrek "Hey %(player_name)s. Wanna see what's under all my layers?"
    princeCharming "*wink*"