#= SCENE 3 Stad
#Je komt in de stad Snow White tegen, ze is verdrietig want Prince Charming
#heeft het uitgemaakt met haar. Je kan haar troosten, negeren of je kan haar
#proberen te versieren. Hierbij moet je de correcte keuzes maken als je dit
#succesvol wil doen, zodat je romance points krijgt bij haar.
#
#Als het niet goed gaat met snow white, dan koop je bloemen en ga je terug naar
#het bos, naar Red Riding Hood
#
#Als het goed gaat met snow white, ga je met haar lunchen. Daar heb je nog wat
#keuzes waarbij je jezelf niet voor gek moet zetten en haar niet moet beledigen.
#
#Als het goed gaat, krijg je veel romance points bij haar, en na het lunchen
#moet ze weer weg gaan
#als het heel slecht gaat, stuurt ze je weg,
#
#uiteindelijk kun je kiezen of je naar het moeras gaat of naar het bos van Red
#Riding Hood

image city_background = "img/citybackground.jpg"
image snowWhite smile = "img/snowwhite_smile.jpg"
image snowWhite angry = "img/snowwhite_angry.jpg"
image snowWhite sad = "img/snowwhite_sad.jpg"

label scene3:
    show city_background
    show snowWhite sad
    unknown "*sniff* *sniff* How could he :'( *sniff* *sniff*"
    menu: 
        "???? is crying what will you do?"
        "Try to comfort her":
            jump scene3_comfort
        "Ignore her":
            jump scene3_ignore
        "Try to adorn her":
            jump scene3_adorn
label scene3_comfort:
    player "Hi, I'm %(player_name)s what is wrong? Why are you so upsad?"
    menu: 
        unknown "Prince Charming he... he... broke up with me :'("
        "Hug ????":
            "You hugged ????"
            player "It will be alright, don't be sad"
            snowWhite "Thank you *sniff* I'm Snow White"
            show snowWhite smile
            play sound "snd/plus.mp3"
            "romance +5"
            $ romance_snowWhite += 5
            player "So what happend? Why did he broke up?"
            show snowWhite sad
            menu:
                snowWhite "He wanted a real princess and choosed a filthy female Ogre above me :'("
                "Ohh please grow up how old are you?! 5 ?":
                    show snowWhite angry
                    snowWhite "How dare you to speak to me like that! If you are here to bully someone then you picked the wrong woman!"
                    play sound "snd/minus.mp3"
                    "romance -5"
                    $ romance_snowWhite -= 5
                    player "Ohh you want to fight me?!"
                    snowWhite "Leave me alone NOW!!"
                    player "Fine go die in your corner!"
                    play sound "snd/minus.mp3"
                    "romance -10"
                    $ romance_snowWhite -= 10
                    jump scene3_ignore
                "What a asshole! How can he choose a Ogre above you? You look pretty :)":
                    show snowWhite smile
                    menu:
                        snowWhite "Really? Do you really think I'm pretty ? :$"
                        "Yea I-I do ;)":
                            snowWhite "Thank you :) You look pretty too :$"
                            play sound "snd/plus.mp3"
                            "romance +10"
                            $ romance_snowWhite += 10
                            player "Thanks!"
                            menu:
                                snowWhite "Do you want to perhaps have a lunch thogeter ?"
                                "Sure that sounds good! :)":
                                    jump scene3_restaurant
                                "Sorry I can't I got to do something else":
                                    snowWhite "Aww okay :) Well thank you for making me feel good and making me smile. Bye bye!"
                                    player "Bye bye!"
                                    jump scene3_flowers
                                    
                        "No, you are ugly!":
                            show snowWhite sad
                            snowWhite "You are mean :'( Go away! Leave me alone!"
                            play sound "snd/minus.mp3"
                            "romance -10"
                            $ romance_snowWhite -= 10
                            "The player left Snow White alone"
                            jump scene3_flowers
                            
        "Leave her alone and get flowers":
            play sound "snd/minus.mp3"
            "romance -5"
            $ romance_snowWhite -= 5
            jump scene3_flowers
    
    
label scene3_restaurant:
    "%(player_name)s and Snow White went to a restaurant thogeter ..."
    menu:
        unknown "So what do you both want to order?"
        "Order for both you and Snow White":
            player "We would like to have some medium rare steak with tommato ketchup"
            unknown "Okay 2 medium rare steak with tommato ketchup will be on your way soon"
            "The ober walked away"
            show snowWhite angry
            snowWhite "I can order something for myself too you know..."
            play sound "snd/minus.mp3"
            "romance -5"
            $ romance_snowWhite -= 5
            "After a silent and uncomfortable lunch..."
            menu:
                snowWhite "Well this didn't went well... but thank you for the lunch and trying to cheer me up"
                "No problem, I'm sorry that I ordered for you, I meant it good":
                    show snowWhite smile
                    snowWhite "It is fine, well I have to go now. I will see you around?"
                    play sound "snd/minus.mp3"
                    "romance +5"
                    $ romance_snowWhite += 5
                    player "Ofcourse we will :) Next time it will go better!"
                    snowWhite "good :) Bye bye"
                    player "Bye bye"
                    jump scene3_flowers
                "Ohh well I didn't enjoy it either. It was a waste of time really...":
                    show snowWhite sad
                    snowWhite "Ohh... I'm sorry to waste you time :'( Well I have to go bye!"
                    play sound "snd/minus.mp3"
                    "romance -5"
                    $ romance_snowWhite -= 5
                    player "..."
                    jump scene3_flowers
            
        "Order somethig for yourself and let Snow White order aswell":
            player "I would like to have a medium rare steak with tommato ketchup"
            unknown "Okay 1 medium rare steak with tommato ketchup and what do you want my lady?"
            snowWhite "I would love to have a raw snail with extra salt and sugar"
            unknown "So that is 1 medium rare steak with tommato ketchup and 1 raw snail with extra salt and sugar?"
            snowWhite "Yes :)"
            player "Yes"
            unknown "It will be there soon"
            "The ober walked away"
            snowWhite "Thanks that you made me order, Prince Charming normaly orders for me"
            play sound "snd/minus.mp3"
            "romance +5"
            $ romance_snowWhite += 5
            "After a nice lunch with Snow White"
            snowWhite "Thank you for this fantastic lunch and cheering me up I had a great time thogeter with you :$"
            player "No, thank you I had a great time as well :)"
            menu:
                snowWhite "I have to go now will I see you again?"
                "Ofcourse you will!":
                    play sound "snd/minus.mp3"
                    "romance +5"
                    $ romance_snowWhite += 5
                    player "I have no reason not to see you again"
                    snowWhite "That is great :) Well Bye bye I cya around!"
                    player "Bye bye :)"
                    jump scene3_flowers
                "No you are boring":
                    show snowWhite sad
                    snowWhite "... Well that isn't nice :'( Bye!"
                    player "..."
                    play sound "snd/minus.mp3"
                    "romance -10"
                    $ romance_snowWhite -= 10
                    jump scene3_flowers

label scene3_flowers:
    hide snowWhite
    "You walked around town to find a place to buy flowers."
    unknown "Flowers Flowers! Get here your flowers!"
    player  "I do want some flowers, can I have a bouquet with many roses"
    unknown  "That will be 50 gold pieces!"
    player  "Wow that is a lot of gold pieces. But sure!"
    "The player grabs 50 gold pieces from the money bag"
    player  "Here you go :)"
    unknown  "Thanks, here you have your bouquet. Goodluck with your goal"
    player "Thanks. Bye bye!"
    jump scene4

label scene3_ignore:
    "You decided to ignore Snow White and went to get some flowers."
    jump scene3_flowers
    
label scene3_adorn:
    player "Hey baby ;) What is wrong with you pretty girl?"
    unknown "Leave me alone! :'( Don't you see I got enough on my mind right now?"
    play sound "snd/minus.mp3"
    "romance -5"
    $ romance_snowWhite -= 5
    menu:
        "Will you leave here alone?"
        "Yes":
            "You left Snow White alone and went to get some flower"
            jump scene3_flowers
        "No":
            player "I'm sorry I thought that you looked pretty. A pretty girl shouldn't cry"
            show snowWhite smile
            unknown "That is nice of you, you don't look bad either"
            play sound "snd/minus.mp3"
            "romance +5"
            $ romance_snowWhite += 5
            player "Thank you :) we should have lunch thogeter"
            snowWhite "That sounds like a good idea! I know a great place, I'm Snow White by the way and you are?"
            player "I'm %(player_name)s lets go! :)"
            jump scene3_restaurant