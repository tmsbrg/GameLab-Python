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
            player "So what happend? Why did he broke up?"
            show snowWhite sad
            menu:
                snowWhite "He wanted a real princess and choosed a filthy female Ogre above me :'("
                "Ohh please grow up how old are you?! 5 ?":
                    show snowWhite angry
                    snowWhite "How dare you to speak to me like that! If you are here to bully someone then you picked the wrong woman!"
                    player "Ohh you want to fight me?!"
                    snowWhite "Leave me alone NOW!!"
                    player "Fine go die in your corner!"
                    jump scene3_ignore
                "What a asshole! How can he choose a Ogre above you? You look pretty :)":
                    show snowWhite smile
                    menu:
                        snowWhite "Really? Do you really think I'm pretty ? :$"
                        "Yea I-I do ;)":
                            snowWhite "Thank you :) You look pretty too :$"
                            player "Thanks!"
                            menu:
                                snowWhite "Do you want to perhaps have a lunch thogeter ?"
                                "Sure that sounds good! :)":
                                    jump scene3_restaurant
                                "Sorry I can't I got to do something else":
                                    snowWhite "Aww okay :) Well thank you for making me feel good and making me smile. Bye bye!"
                                    plater "Bye bye!"
                                    jump scene4
                                    
                        "No, you are ugly!":
                            show snowWhite sad
                            snowWhite "You are mean :'( Go away! Leave me alone!"
                            "The player left Snow White alone"
                            jump scene4
                            
        "Leave her alone and get flowers":
            jump scene3_ignore
    
    
label scene3_restaurant:
    
    
label scene3_ignore:
    show shrek smile
    shrek "A Fairy tale? This is Fairy world, so where are you from?"
    player "I'm from Earth, how do I go back to earth?"
    shrek "I don't know, I didn't even know it was possible to come here from another world, maybe someone in the city north of here can help you?"
    player "Thanks!, so what are you doing here?"
    show shrek mad
    shrek "I live here because I eat people!"
    player "Well then you are too nice for being what you said you are"
    show shrek smile
    shrek "Thanks, well shouldn't you head out to town? I will give you some money"
    "Shreks gives %(player_name)s a bag of money"
    player "Thank you Shrek :) I will go now bye bye I will cya around!"
    shrek "Goodbye %(player_name)s have a nice journey!"
    "You are walking in the forest and there....."
    jump scene4
label scene3_adorn:
    shrek "Fine!, ROARRRRR! GET OUT MY SWAMP NOW BEFORE I EAT YOU!"
    player "You won't eat me you are fat and will never able to get me!"
    shrek "ROARRRRRRRR! GET OUT!"
    "Shrek throws a bag of money to %(player_name)s"
    player "Thanks sucker!"
    "The player runs into the forest and there....."
    jump scene4