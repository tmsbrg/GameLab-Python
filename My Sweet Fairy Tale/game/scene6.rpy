# = SCENE 6 Stad 2
# 
# In de stad kom je snow white weer tegen, je vraag haar om een slaapplek. Ze
# kent een kasteel waar je wel kan slapen. Je krijgt honger en je kunt haar
# vragen of ze samen met jouw zou willen eten. Als je genoeg romance points
# hebt, dan accepteerd ze, anders niet. Als ze niet accepteert of je het haar
# niet vraagt, dan eet je alleen, anders heb je met haar een date.
# 
# Tijdens deze date heb je nog meer keuzes waarbij je jezelf niet voor gek moet
# zetten, en haar niet moet beledigen. Als alles goed gaat krijg je veel extra
# romance points met haar.
# 
# Na het eten ga je alleen naar het kasteel.

label scene6:
    scene bg city
    with fade
    player "(*Yawn*. I'm getting tired. It's time to sleep.)"

    if (romance_snowWhite <= -10):
        jump scene6_unhappy
    else:
        jump scene6_happy

label scene6_happy:
    show snowWhite smile at right
    with fade
    snowWhite "Hey %(player_name)s!"
    player "Hey snow white. Do you know a place to sleep?"
    snowWhite "Hm. You can sleep in the castle."
    player "Thanks. I guess I'll go there."
    snowWhite "Okay. Have fun!"
    jump scene6_tocastle

label scene6_unhappy:
    show snowWhite angry at right
    with fade
    snowWhite "Oh, it's you."
    player "Oh, hi..."
    player "Uhm... Sorry, but do you know where I can sleep?"
    snowWhite "...*sigh*"
    snowWhite "You can go to the castle."
    snowWhite "Just leave me alone."
    "You quickly go to the castle ..."
    jump scene6_tocastle

label scene6_tocastle:
    hide snowWhite
    "You rent a room at the castle. Time to go there for some sleep"
    jump scene7
