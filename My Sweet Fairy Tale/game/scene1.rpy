#scene 1
#	== BEGIN
#	Je speelt een vrouw
#	Je kunt ja naam kiezen
#	Je wordt wakker in Shreks moeras; een gesprek met Shrek volgt met keuzes waarin
#	je hem blij me je kan maken of kan beledigen
#	
#	= SCENE 1 Moeras
#	Shrek laat je weten dat je in fairy tale land bent gestrand, en verteld je van
#	een stad dichtbij waar je hulp kan zoeken en geeft je wat geld, hierna ga je
#	hierheen, en begint het verhaal
#	
#	Als je hem boos maakte, gooit hij het geld naar je
#	
#	Je motivatie is eerst om terug te komen naar de gewone wereld,
#	maar nadat je de hete chicks van de fairy tale wereld vind, verandert je
#	motivatie

label scene1:
    shrek "Hey YOU! What are you doing in my swamp? And who are you?"
    player " I'm %(player_name)s and I don't know, last thing I remember is that I was in my bed sleeping and now I'm here. Where am I?"
    jump scene1_choose

        
label scene1_choose:

    menu: 
        shrek "Like I said before you are in MY swamp. Is there anything I can help you with? Else get out my SWAMP!"
        "Yes, how can I go back home? And why does it look weird around here? Am I in a Fairy Tale?":
            jump scene1_good
        "No, you look ugly, disquisting and you are mean. I will go find someone else.":
            jump scene1_bad

    
label scene1_good:
    shrek "A Fairy tale? This is Fairy world, so where are you from?"
    player "I'm from Earth, how do I go back to earth?"
    shrek "I don't know, I didn't even know it was possible to come here from another world, maybe someone in the city north of here can help you?"
    player "Thanks!, so what is your name ?"
    shrek "I'm Shrek I eat people and live in the swamp."
    player "Well then you are too nice for being what you said you are"
    shrek "Thanks, well shouldn't you head out to town? I will give you some money"
    "Shreks gives %(player_name)s a bag of money"
    player "Thank you Shrek :) I will go now bye bye I will cya around!"
    shrek "Goodbye %(player_name)s have a nice journy!"
    "You are walking in the forest and there....."
    jump scene2
label scene1_bad:
    shrek "Fine!, ROARRRRR! GET OUT MY SWAMP NOW BEFORE I EAT YOU!"
    player "You won't eat me you are fat and will never able to get me!"
    shrek "ROARRRRRRRR! GET OUT! -Throws with a money bag-"
    "Shrek throws a bag of money to %(player_name)s"
    player "Thanks sucker!"
    "The player runs into the forest and there....."
    jump scene2

label scene_1_shrek:
    menu:
        shrek "Hey %(player_name)s. Wanna see what's under all my layers?"
        "Yes":
            jump scene_1_Yes_Layers
        "No":
            jump scene_1_No_Layers
#end

label scene_1_Yes_Layers:
    player "Ohh sure! I would love to see that ;)"
    shrek "here it goes!"
    player "Ugh........"
jump end

label scene_1_No_Layers:
    player "I rather die then see what is under your layers"
    shrek "I will help you and eat you!"
jump end