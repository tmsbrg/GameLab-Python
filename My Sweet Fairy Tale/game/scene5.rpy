#= SCENE 5 Moeras 2
#
#Als je bloemen hebt gekocht kun je die aan Shrek geven,
#en verlies je veel romance points omdat hij boos wordt
#Hij stuurt je dan weg, en je kan kiezen of je naar het bos gaat of de stad
#
#Shrek is stenen aan het gooien, hij wil eigenlijk alleen zijn
#Je kunt kiezen om mee te doen of weg te gaan
#
#Als je mee doet kun je kiezen of je je best doet of hem laat winnen
#Als je je best doet, dan win je en krijg je veel romance points bij hem omdat
#hij onder de indruk is
#Anders verlies je romance points en wil hij alleen zijn, en ga je weer weg
#
#Als je wint wil hij niet dat je weg gaat, en ga je meer samen doen en kun je
#meer romance points bij hem verkijgen
#
#Als je de date met shrek hebt gehad, ga je naar de stad om een slaapplek te
#zoeken

#image swamp_background = "img/swampbackground.jpg"
#image shrek smile = "img/shrek_smile.png"
#image shrek confused = "img/shrek_confused.png"
#image shrek mad = "img/shrek_mad.png"


label scene5:
    scene bg swamp
    if romance_shrek < 0:
        show shrek mad
        with fade
        menu:
            shrek "What are you doing in MY SWAMP go away before I EAT you!"
            "Tell Shrek that you are sorry":
                player "I'm sorry for hurting your feelings, I just don't have my day :("
                show shrek smile
                with fade
                shrek "I won't forgive you that easly! If you want to be forgiven you have to beat my with this game!"
                play sound "snd/plus.mp3"
                "romance +10"
                $ romance_shrek += 10
                jump scene5_flowers
                
            "Say mean things to Shrek and run for your life":
                player "You ugly Ogre! With your stupid swamp! You don't belong in this world!"
                shrek "OHH YOU LITTLE! I WILL GET YOU!"
                play sound "snd/minus.mp3"
                "romance -25"
                $ romance_shrek -= 25
                "The player ran away"
                jump scene6
    else:
        show shrek smile
        with fade
        player "Hi Shrek I'm back!"
        menu:
            shrek "Hello, what do you want? Don't you see I'm busy playing a game!"
            "Ask Shrek if you can join the game":
                player "Do you mind if I join you playing the game?"
                shrek "Uhm I rather play alone but if you really want to play then sure."
                jump scene5_flowers
            "Leave Shrek alone":
                player "Alright I will leave you alone, Bye bye"
                shrek "Bye!"
                jump scene6
        
label scene5_flowers:
    if bought_flowers == True:
        menu:
            "You have bought some flowers would you give it to Shrek?"
            "Yes":
                player "I've bought you something, I'm really sorry for being mean to you"
                shrek "Ohh I like supprises what did you get for me? :)"
                "The player gave shrek the flowers"
                $ bought_flowers = False
                player "Here you go some pretty flowers!"
                shrek "ARGH! I'm alergic to roses how dare you! You better run away!"
                play sound "snd/minus.mp3"
                "romance -10"
                $ romance_shrek -= 10
                player "Sorry!"
                "The player ran away into the forest"
                jump scene6
            "No":
                "You decided not to give flowers to shrek"
                jump scene5_rockgame 
    else:
        jump scene5_rockgame

label scene5_rockgame:
    shrek "You will go first"
    "Shrek gives the player a rock"
    shrek "Throw the rock over there, the one who throws the rock the farthest wins the game"
    player "Understood! Lets go!"
    menu:
        "Do you want to do your best and throw the rock as far as you can?"
        "yes":
            "The player turns around and around and around and throws the rock..."
            "Aaand the rock landed 23.1 meters far"
            player "Ha! beat that! :)"
            shrek "Ohh not bad for a human! Now it is my turn."
            "Shrek is throwing the rock with full strength"
            "And the rock landed 22.7 meters far!"
            player "Ohhh! I guess I won!"
            shrek "Yea... I didn't expect a human to be that good."
            play sound "snd/plus.mp3"
            "romance +10"
            $ romance_shrek += 10
            menu:
                shrek "Will you stay with me in my swamp and have dinner thogeter?"
                "Yes":
                    player "Ofcourse I will have dinner with you! That sounds great :)"
                    shrek "Cool! I already have prepared something I hope you like it."
                    play sound "snd/plus.mp3"
                    "romance +10"
                    $ romance_shrek += 10
                    jump scene5_dinner
                "No":
                    player "I'm sorry I've to go."
                    shrek "Aww alright. Thank you for the awesome game"
                    player "No problem it was fun. Bye bye"
                    shrek "Bye!"
                    jump scene6
        "No":
            "The player throws the rock"
            "The rock landed 5 meters behind you"
            player "Was that good?"
            shrek "You threw the rock -5 meters..."
            player "Oh..."
            show shrek mad
            with fade
            shrek "You are no match for me, you should go!"
            player "I'm sorry, I will leave you alone. Bye bye"
            shrek "Bye!"
            play sound "snd/minus.mp3"
            "romance -10"
            $ romance_shrek -= 10
            jump scene6
            
label scene5_dinner:
    "And so shrek prepared the dining table"
    shrek "So I'm done! Lets eat!"
    player "Woohoo!"
    menu:
        "The player looks at the food"
        "Eeeeeuww It looks disgusting":
            player "The food it looks disgusting!"
            shrek "It is my favorite, just try it"
            menu:
                "Try the food shrek made?"
                "Yes":
                    jump scene5_havingdinner
                "No":
                    player "No I won't try to eat something disgusting like that!"
                    show shrek mad
                    with fade
                    shrek "Then you should leave before I eat you!"
                    player "Jeesh! I'm going already bye you stupid fat Ogre!"
                    shrek "Bye filthy human!"
                    play sound "snd/minus.mp3"
                    "romance -10"
                    $ romance_shrek -= 10
                    jump scene6
        "The food looks good":
            player "It looks good Shrek"
            shrek "It is my favorite cooked snail with extra pepper. I hope you will enjoy it."
            play sound "snd/plus.mp3"
            "romance +5"
            $ romance_shrek += 5
            jump scene5_havingdinner

    
label scene5_havingdinner:
    "The player started eating cooked snail with extra pepper."
    menu: 
        shrek "Do you like it?"
        "Yes":
            player "Yea it is quite good I never expected that it will taste this great."
            shrek "That is great I did my best to make it :)"
            "The player and Shrek are enjoying the dinner thogeter and having a great time"
            play sound "snd/plus.mp3"
            "romance +10"
            $ romance_shrek += 10
            jump scene5_end
        "No polite":
            player "It looks beter then it tastes, I don't really like it"
            shrek "Well that is too bad, I will give you something else"
            player "Thank you shrek you are so kind :)"
            shrek "Thanks, you are nice as well. I like you"
            play sound "snd/plus.mp3"
            "romance +2"
            $ romance_shrek += 2
            "Shrek gave the player another dinner that the player enjoy's"
            "And then the player and Shrek are enjoying the dinner thogeter and having a great time"
            play sound "snd/plus.mp3"
            "romance +5"
            $ romance_shrek += 5
            jump scene5_end
        "No rude":
            player "Eeeeuw it is disgusting I should have never accepted dinner with a disgusting creature like you!"
            show shrek mad
            with fade
            shrek "How dare you to talk to me like that in my own swamp! You should leave before I eat you!"
            player "Jeesh! I'm going already bye you stupid fat Ogre!"
            shrek "Bye filthy human!"
            play sound "snd/minus.mp3"
            "romance -10"
            $ romance_shrek -= 10
            jump scene6
    
label scene5_end:
    "After a wonderfull dinner the player had to go."
    player "Well it is getting late I should go to town and find a place to sleep."
    shrek "Alright, I had a great time with you. I hope you also enjoyed spending time with me."
    menu:
        "Did you enjoy spending time with shrek?"
        "No":
            player "I didn't enjoy it. I shouldn't have came back. I'm sorry."
            show shrek confused
            with fadde
            shrek "Ohh well I guess I cya around. Bye."
            player "Goodbye."
            play sound "snd/minus.mp3"
            "romance -10"
            $ romance_shrek -= 10
            jump scene6
            
        "Yes":
            player "I also had a great time with you Shrek ;) It was a lot of fun"
            shrek "That is great, will I see you again tommorow?"
            player "Maybe, I will see I hope so. I like you"
            shrek "That is great!"
            player "I be on my way now, Bye bye Shrek!"
            shrek "Bye bye!"
            play sound "snd/plus.mp3"
            "romance +10"
            $ romance_shrek += 10
            jump scene6
            