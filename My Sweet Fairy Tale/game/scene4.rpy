# = SCENE 4 Bos 2
# 
# Als je bloemen hebt gekocht kun je die aan Red Riding Hood geven,
# en krijg je veel romance points
# 
# Red Riding Hood zegt iets gebaseerd op hoeveel romance point je voor haar hebt
# 
# Jullie doen wat dingen samen, je kunt hierbij nog meer romance points krijgen
# 
# Je eindigt in de stad en Red Riding Hood moet dan weer weg

label scene4:
    scene bg forest
    "You go back to the forest"

    show redRidingHood neutral at right
    with fade
    
    if bought_flowers:
        jump scene4_contemplate_flowers

    player "Hi again."
    jump scene4_show_romance

label scene4_contemplate_flowers:
    menu:
        player "(Should I give her my flowers?)"
        "Yes":
            jump scene4_give_flowers
        "No":
            jump scene4_show_romance

label scene4_give_flowers:
    player "Here, I bought you flowers."
    $ bought_flowers = False
    play sound "snd/plus.mp3"
    "romance +20"
    $ romance_redRidingHood += 20
    redRidingHood "Thanks, you're so nice ;-)"
    jump scene4_show_romance

label scene4_show_romance:
    if romance_redRidingHood >= 20:
        jump scene4_hunt_invite
    elif romance_redRidingHood <= 10:
        jump scene4_why_leave
    else:
        redRidingHood "Hey there."

label scene4_hunt_invite:
    redRidingHood "Hey sweetie."
    redRidingHood "Do you wanna go hunting with me?"

label scene4_why_leave:
    redRidingHood "Why did you leave so suddenly back there?"
