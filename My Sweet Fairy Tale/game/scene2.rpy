# = SCENE 2 Bos
# Onderweg naar de stad kom je in het bos Red Riding Hood tegen
# Je vertelt haar dat je terug wil naar je eigen wereld
# Zij zegt dat ze dat jammer vindt *wink*, ze vindt je duidelijk hot
# Je kunt in dit gesprek weer keuzes maken waarbij je haar blij kan maken of
# kan beledigen
# Hierna ga je door naar de stad om bloemen te halen voor haar

label scene2:
    $ redRidingHoodIsExpectingFlowers = False
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
        player "(What should I do?)"
        
        "Tell her you want to go back to your own world":
            jump scene2_own_world
        "Go on to the town Shrek told you about":
            jump scene2_to_town
        "I-I'm a girl you know":
            jump scene2_grill

label scene2_own_world:
    "You tell her your odd tale and that you want to get back to your own world..."
    redRidingHood "Aww that's too bad ;-)"
    player "Do you know a way to get back?"
    redRidingHood "I never heard such a strange story."
    redRidingHood "Maybe someone in town can help you."
    player "Actually, I was on the way there now."
    redRidingHood "Well good luck with trying to get out of here."
    redRidingHood "I'll miss having such a cutie around though."
    jump scene2_bring_flowers

label scene2_to_town:
    player "S-sorry I have to go..."
    menu:
        redRidingHood "Where are you going?"
        "Tell her":
            player "I was going to the town."
            redRidingHood "Oh. Have fun."
            jump scene2_bring_flowers
        "Just leave":
            play sound "snd/minus.mp3"
            "romance -20"
            $ romance_redRidingHood -= 20
            jump scene3

label scene2_grill:
    player "I-I'm a girl you know"
    redRidingHood "Yes, and such a cute one ;-)"
    play sound "snd/plus.mp3"
    "romance +10"
    $ romance_redRidingHood += 10
    menu:
        player "(Is she hitting on me?)"
        "Tell her you want to go back to your own world":
            jump scene2_own_world
        "Go on to the town Shrek told you about":
            jump scene2_to_town

label scene2_bring_flowers:
    redRidingHood "Hey, bring me some flowers while you're there."
    player "S-sure"
    $ redRidingHoodIsExpectingFlowers = True
    "You quickly move to the town..."
    jump scene3

