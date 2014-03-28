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
    jump scene4_dont_give_flowers

label scene4_contemplate_flowers:
    menu:
        player "(Should I give her my flowers?)"
        "Yes":
            jump scene4_give_flowers
        "No":
            jump scene4_dont_give_flowers

label scene4_give_flowers:
    show redRidingHood happy
    player "Here, I bought you flowers."
    $ bought_flowers = False
    play sound "snd/plus.mp3"
    "romance +20"
    $ romance_redRidingHood += 20
    redRidingHood "Thanks, you're so nice ;-)"
    jump scene4_show_romance

label scene4_dont_give_flowers:
    if (redRidingHoodIsExpectingFlowers):
        play sound "snd/minus.mp3"
        "romance -20"
        $ romance_redRidingHood -= 10
        redRidingHood "You didn't bring me flowers..."
    jump scene4_show_romance

label scene4_show_romance:
    if romance_redRidingHood >= 20:
        jump scene4_hunt_invite
    elif romance_redRidingHood <= -10:
        jump scene4_why_leave
    else:
        jump scene4_neutral

label scene4_hunt_invite:
    redRidingHood "Hey sweetie."
    show redRidingHood seductive
    redRidingHood "Do you wanna go hunting with me?"
    menu:
        player "(Hunting?)"
        "Okay":
            jump scene4_hunting
        "I'd rather not":
            jump scene4_nohunt

label scene4_hunting:
    show redRidingHood happy
    redRidingHood "Yay!"
    redRidingHood "Let's go! It'll be fun."
    scene bg deepforest
    show redRidingHood neutral at left
    with fade
    redRidingHood "shh, I hear something..."
    "You hear a growling sound in the bushes."
    redRidingHood "It's a wolf..."
    player "A-a wolf!?"
    redRidingHood "Shh! you'll give us away."
    redRidingHood "Let's hunt it."
    menu:
        player "(Hunt the wolf?)"
        "I'm not sure if this is safe.":
            jump scene4_hunting_unsafe
        "O-okay.":
            jump scene4_hunting_okay
        "Let me do it.":
            jump scene4_hunting_doit

label scene4_hunting_unsafe:
    redRidingHood "Aw, trust me. We're not gonna get hurt."
    redRidingHood "I'm a pro, you know."
    redRidingHood "Okay, let's do this"
    show redRidingHood happy
    jump scene4_hunting_shedoesit

label scene4_hunting_okay:
    redRidingHood "Don't be shy. Let's have fun."
    show redRidingHood happy
    redRidingHood "Hey... Why don't you shoot him?"
    menu:
        player "(M-me?)"
        "Sure":
            jump scene4_hunting_doit
        "No, you do it. I'll watch and learn.":
            play sound "snd/minus.mp3"
            "romance -5"
            $ romance_redRidingHood -= 5
            redRidingHood "Oh, well. Okay!"
            jump scene4_hunting_shedoesit
        

label scene4_hunting_shedoesit:
    show redRidingHood neutral
    "Red riding hood takes out her gun..."
    "..."
    "She spots the wolf..."
    show redRidingHood angry
    "She aims the gun at the wolf..."
    "*BOOM*!"
    show redRidingHood neutral
    "..."
    "The wolf gets unstable"
    "The wolf falls to sleep"
    show redRidingHood happy
    redRidingHood "Yay! I got him"
    player "Nice shot!"
    redRidingHood "That was fun."
    jump scene4_hunting_end

label scene4_hunting_doit:
    show redRidingHood seductive
    redRidingHood "Ohh, I hadn't expected you to be this... gutsy."
    play sound "snd/plus.mp3"
    "romance +10"
    $ romance_redRidingHood += 10
    show redRidingHood happy
    redRidingHood "Let's do this!"
    "Red riding hood gives you her gun"
    show redRidingHood neutral
    player "(I've got to impress her now...)"
    "..."
    "You spot the wolf..."
    "You aim the gun at the wolf..."
    "*BOOM*!"
    show redRidingHood happy
    redRidingHood "Oops, you missed!"
    "The wolf runs away."
    player "Oh... sorry."
    redRidingHood "Hey, nice try anyway. I hadn't expected you to actually try to shoot it yourself"
    jump scene4_hunting_end

label scene4_nohunt:
    show redRidingHood neutral
    redRidingHood "Aww. Why not?"
    menu:
        player "(Why not?)"
        "I don't like to hurt animals":
            redRidingHood "Oh, that's no problem."
            redRidingHood "I only use anesthetic shots. They'll just go to sleep."
            player "I guess that's okay then."
            jump scene4_hunting
        "I've got stuff to do":
            play sound "snd/minus.mp3"
            "romance -10"
            $ romance_redRidingHood -= 10
            redRidingHood "Aww. Well, have fun doing whatever you have to do."

label scene4_hunting_end:
    scene bg forest
    show redRidingHood seductive at right
    with fade
    redRidingHood "Let's do that again sometime."
    player "Goodbye!"
    redRidingHood "Goodbye!"
    play sound "snd/plus.mp3"
    "romance +10"
    $ romance_redRidingHood += 10
    jump scene5

label scene4_why_leave:
    show redRidingHood neutral
    redRidingHood "Why did you leave so suddenly back there?"
    menu:
        player "(Why?...)"
        "Sorry, I was late to something.":
            redRidingHood "Oh. Well please don't do that again"
            show redRidingHood happy
            redRidingHood "It's so rude"
            jump scene4_neutral
        "(Leave)":
            show redRidingHood angry
            play sound "snd/plus.mp3"
            "romance -30"
            $ romance_redRidingHood -= 30
            "You leave awkwardly to Shrek's swamp..."
            jump scene5

label scene4_neutral:
    redRidingHood "Hey."
    redRidingHood "Good luck getting back to your world."
    redRidingHood "I've got to do something"
    redRidingHood "Bye!"
    hide redRidingHood with fade
    player "I guess I can see what that Shrek is up to"
    jump scene5
