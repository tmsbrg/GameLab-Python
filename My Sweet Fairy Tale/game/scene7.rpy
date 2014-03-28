#== EINDE
#Op het einde van de dag wil je gaan slapen in kasteel in de Fairy Tale
#wereld.
#
#Als je geen karakter blij met jou hebt gemaakt, wordt je na het slapen wakker in
#je eigen wereld
#Anders komt het karakter waarbij je de meeste romance points bij je hotelkamer
#aankloppen
#Dit karakter laat zien dat hij of zij interesse heeft in je
#Hierna moet je de goede keuzes maken zodat ze niet ongeinteresseerd raken,
#als het slecht gaat gaan ze weg en slaap je alleen,
#als het goed gaat slaap je niet alleen en is het happily ever after

#$ romance_snowWhite = 0
#$ romance_redRidingHood = 0
#$ romance_shrek = 0

#image shrek smile = "img/shrek_smile.png"
#image shrek confused = "img/shrek_confused.png"
#image shrek mad = "img/shrek_mad.png"

#image snowWhite smile = "img/snowwhite_smile.png"
#image snowWhite neutral = "img/snowwhite_neutral.png"
#image snowWhite angry = "img/snowwhite_angry.png"
#image snowWhite shy = "img/snowwhite_shy.png"

label scene7:
    scene bg
    "The player went to the castle after a long long day and prepared to sleep"
    if romance_snowWhite > romance_redRidingHood && romance_snowWhite > romance_shrek:
        jump scene7_snowWhite
    if romance_shrek > romance_redRidingHood && romance_shrek > romance_snowWhite:   
        jump scene7_shrek
    if romance_redRidingHood > romance_shrek && romance_redRidingHood > romance_snowWhite:   
        jump scene7_redRidingHood   
        
    jump scene7_alone
 
label scene7_redRidingHood:
    
    
label scene7_shrek:
    "*BOEM* *BOEM*"
    "Shrek came into the room"
    show shrek smile
    with fade
    shrek "Hello"
    player "Hi Shrek"
    menu:
        shrek "I had a great day with you. I couldn't keep my human eating Ogre mind off you"
        "You want to eat me?! You should go away!": 
            show shrek angry
            with fade
            shrek "Well then I was wrong about you! Next time I see you I will eat you! I'm gone! Bye filthy human! "
            player "Yea go away! Stupid ogre!"
            jump scene7_alone
        "Ohh that is so sweet Shrek":
            shrek "You really think so ?"
            player "Yes, I couldn't take my mind of you either Shrek... I had a great time with you"
            shrek "Ohh %(player_name)s I love you!"
            player "I love you too Shrek!, would you want to spend the night with me?"
            shrek "Ofcourse I would want that, wanna see what's under all my layers? ;)"
            player "Ohh...:$ I would love to see that"
            shrek "Here it goes!"
            player "Ugh...."
            "And so Shrek never met another Ogre and lived happily ever after with %(player_name)s"
            jump scene7_end

label scene7_snowWhite:
    "*knock* *knock*"
    "Snow White came into the room"
    show snowWhite smile
    with fade
    snowWhite "Hi"
    player "Hello"
    menu:
        snowWhite "I was thinking about you while you were gone..." 
        "I was also thinking about you":
            snowWhite "Really? That is good. I love you %(player_name)s"
            player "I love you too Snow White, w-would you want to spend the night with me?"
            show snowWhite shy
            with fade
            snowWhite "Ohh... I would love that."
            "And so Snow White forgot about Prince Charming and lived happily ever after with %(player_name)s"
            jump scene7_end
        "Okay what is wrong?":
            show snowWhite angry
            with fade
            snowWhite "Nothing, nevermind... I should leave"
            jump scene7_alone
    
label scene7_alone:
    "After a while thinking and crying for wanting to go home you fell asleep."
    jump scene7_end
            
label scene7_end:
    "The End"