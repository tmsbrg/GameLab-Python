#Shrek scene!

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