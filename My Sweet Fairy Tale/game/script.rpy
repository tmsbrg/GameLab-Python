# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# The game starts here.
label start:
    
    $ player_name = renpy.input("What is your name?").strip()
    if player_name == "":
        $ player_name = "Default"
        
    player "My name is %(player_name)s!"
    
    "Which character do you like"
    menu:
        "Snow White":
            jump scene_snow
        "Shrek":
            jump scene_1_shrek
        "Red Riding Hood":
            jump scene_red


label scene_snow:
    cinderella "Be gentle... %(player_name)s..."
    snowWhite ";_;"
    jump scene_end
    
label scene_red:
    redRidingHood "Hey hottie ;)"
    femaleWolf "You look... tasty"
    jump scene_end
    
label end:
    "Game over, you died."