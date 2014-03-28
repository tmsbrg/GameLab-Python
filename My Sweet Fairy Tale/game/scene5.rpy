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
#image shrek smile = "img/shrek_smile.jpg"
#image shrek mad = "img/shrek_mad.jpg"


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
                jump scene5_rockgame
            "Say mean things to Shrek and run for your life":
                player "You ugly Ogre! With your stupid swamp! You don't belong in this world!"
                shrek "OHH YOU LITTLE! I WILL GET YOU!"
                "The player ran away"
                jump scene6
    else:
        show shrek smile
        with fade
        player "Hi Shrek I'm back!"
        shrek "Hello, so what is it that you want?"
        
label scene5_rockgame:

    jump scene6
