# = SCENE 2 Bos
# Onderweg naar de stad kom je in het bos Red Riding Hood tegen
# Je vertelt haar dat je terug wil naar je eigen wereld
# Zij zegt dat ze dat jammer vindt *wink*, ze vindt je duidelijk hot
# Je kunt in dit gesprek weer keuzes maken waarbij je haar blij kan maken of
# kan beledigen
# Hierna ga je door naar de stad om bloemen te halen voor haar

label scene2:
    scene bg forest
    unknown "Hey there ;-)"
    player "Who said that?"
    show redRidingHood neutral at right
    with fade
    redRidingHood "Hello, hottie."
    player "H-hi?"
    redRidingHood "I'm red riding hood, what's your name? ;-)"
    player "My name is %(player_name)s."
    redRidingHood "%(player_name)s? What a funny name for such a cutie."
    player "Eh..."
    menu:
        player "What should I do?"
        
        "Tell her you want to go back to your own world":
            jump scene2_own_world
        "Go on to the town Shrek told you about":
            jump scene2_to_town
        "I-I'm a girl you know":
            jump scene2_grill

label scene2_own_world:
    redRidingHood "Aww that's too bad ;-)"

label scene2_to_town:
    player "S-sorry I have to go..."
    redRidingHood "Where are you going?"
    player "There is a town nearby here, right? I want to go there."

label scene2_grill:
    player "I-I'm a girl you know"
    redRidingHood "Yes, and such a cute one ;-)"
