# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define player = Character('F-Player', color="#FFFFFF")
define snowWhite = Character('Snow White', color="#FFFFFF")
define femalewolf = Character('Female Wolf', color="#FFFFFF")
define redRidingHood = Character('Red Riding hood', color="#FFFFFF")
define cyndarella = Character('Cyndarella', color="#FFFFFF")
define shrek = Character('Shrek', color="#FFFFFF")
define princeCharming = Character('Prince Charming', color="#FFFFFF")
# The game starts here.
label start:
    player "Ohh hai good looking guy!"
    shrek "GRAAAAAAAAAAAAWRRRRRRR Get out my Swamp!"
    player "... Why are you so mean?"
    menu:

        "Get the fuck out of here":

            jump goAwayFromShrek

        "Look into his eyes":

            jump lookingInShrekEyes
    return

label goAwayFromShrek:
    player "Screw you I'm out of here!"
    shrek "BYE!"
    return
    
    label lookingInShrekEyes:
    "You started to look deeply into Shrek his eyes"
    shrek "I WILL EAT YOU! RAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRRRRRWWW"
    player "NOOOOOOOOOOOOOOO!!!!!!!......."
    "You got eaten by Shrek"
    return