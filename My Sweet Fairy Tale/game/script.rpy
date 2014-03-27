# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg forest = "img/bg_forest.png"

# The game starts here.
label start:
    $ romance_snowWhite = 0
    $ romance_redRidingHood = 0
    $ romance_shrek = 0
    
    $ player_name = renpy.input("My lady, what is your name?").strip()
    if player_name == "":
        $ player_name = "Default"

    player "My name is %(player_name)s! Who are you?"
    unknown "Don't mind who I'm please enjoy your stay here."
    jump scene2
#    menu:
#        player "Which character do I like?"
#        "Snow White":
#            jump scene_snow
#        "Shrek":
#            jump scene_1_shrek
#        "Red Riding Hood":
#            jump scene_red


label scene_snow:
    cinderella "Be gentle... %(player_name)s..."
    snowWhite ";_;"
    jump end
    
label scene_red:
    redRidingHood "Hey hottie ;)"
    femaleWolf "You look... tasty"
    jump end
    
label end:
    "Game over, you died."
