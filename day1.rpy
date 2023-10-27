label day_1:
    $ prism.start_chapter_event("Day1")
    stop music fadeout 1.0 
    scene black
    play sound "Academy_GoodAnswer.ogg" fadein 0.0
    centered """Love Thyself SFX-VO Mod active.{w=2.0} If you don't hear a short sound clip the installation failed (is your device's sound on?)."""
    nvl clear
    play music "sfxmod_intro_v5_final.wav" fadein 0.1 # sfxmod start
    play movie "bg-dust-animated.webm" loop
    scene bgdust with dissolve
    show movie
    
    play sound "LoveThy_SFXMOD_01_sfx7_impossible_master.wav" fadein 0.1
    centered """{w=10.5} IT IS IMPOSSIBLE TO DISSOCIATE MY STORY FROM THAT OF HORATIO, THE FIRST OF OUR NAME."""
    
    play sound "LoveThy_SFXMOD_02_sfx7_first_master.wav" fadein 0.1
    centered """THE FIRST BEINGS TO TRAVEL WIDELY BETWEEN THE STARS WERE KNOWN AS THE ENDLESS; {w=2.5} WE KNOW OF NO EARLIER FORM OF INTELLIGENT LIFE THAT MOVED BETWEEN GALAXIES."""
    
    play sound "LoveThy_SFXMOD_03_sfx7_theirhistory_master.wav" fadein 0.1
    
    centered """THEIR HISTORY IS GLORIOUS BUT ABOVE ALL TRAGIC; THOUGH THEY UNLOCKED THE SECRETS OF TIME-SPACE, THE STARS, AND LIFE ITSELF THEY WERE UNABLE TO MASTER THEIR OWN INTERNAL CONFLICTS."""
    
    play sound "LoveThy_SFXMOD_04_sfx7_whatremains_master.wav" fadein 0.1
    
    centered """WHAT REMAINS NOW OF THE ENDLESS ARE STRANGE, DISJOINTED TRACES IN THE FORMS OF SEEDS, OF OBSERVATORIES, OF EXPERIMENTS, OF CITIES AND WORLDS AND PERHAPS – THOUGH NOT ALL OF THIS IS CLEAR OR VERIFIABLE – IN THE FORMS OF OTHER PEOPLES."""
    
    #scene bgendless with dissolve
    play movie "bg-endless-animated.webm" loop
    show movie with dissolve
    play sound "LoveThy_SFXMOD_05_sfx7_manyciv_master.wav" fadein 0.1
    
    centered """MANY STARFARING CIVILIZATIONS HAVE SINCE RISEN TO THE FORE. SOME HAVE FALLEN AS WELL."""
    
    play sound "LoveThy_SFXMOD_06_sfx7_events_master.wav" fadein 0.1
    
    centered """EVENTS IN RECENT HISTORY HAVE LED TO AN EXPLOSION IN THE NUMBER OF PLAYERS ON THE GALACTIC SCENE."""
    
    play sound "LoveThy_SFXMOD_07b_sfx7_oneofthem_master.wav" fadein 0.1
    
    centered """ONE OF THESE, UNDOUBTEDLY A MAJOR ONE, IS HORATIO."""
    nvl clear
    #scene bg-lab2 with dissolve
    play movie "bg-lab-blurry.webm" loop
    show movie with dissolve
    
    play sound "LoveThy_SFXMOD_07_sfx7_once_master.wav" fadein 0.1
    
    centered """ONCE UPON A TIME, HORATIO WAS JUST A MAN, A SIMPLE TRILLIONAIRE."""
    
    play sound "LoveThy_SFXMOD_08_sfx7_onenight_master.wav" fadein 0.1
    
    centered """ONE NIGHT, A VISION CAME TO HIM IN THE SHAPE OF A DREAM. IT WAS THE VISION OF AN EMPIRE, AND ETERNAL LIFE."""
    
    play sound "LoveThy_SFXMOD_08b_sfx7_venture_master.wav" fadein 0.1
    centered """HE LEFT EVERYTHING BEHIND, VENTURING THROUGH THE STARS."""
    
    play sound "LoveThy_SFXMOD_09_sfx7_overtheages_master.wav" fadein 0.1
    
    centered """{w=1.3}OVER THE AGES, HE DISCOVERED MANY OF THE MYSTERIES LEFT BY THE ENDLESS, AND HIS KNOWLEDGE AND POWER GREW."""
    
    play sound "LoveThy_SFXMOD_10_sfx7_hecreated_master.wav" fadein 0.1
    centered """HE CREATED HIS FIRST SONS, AND WILLED HIS EMPIRE INTO EXISTENCE, A BEACON OF ALL THAT IS BRILLIANT AND BEAUTIFUL."""
    
    play sound "LoveThy_SFXMOD_11_sfx7_now_the_empire_master.wav" fadein 0.1
    centered """NOW THE EMPIRE OF HORATIO FLOURISHES, AND HORATIO HIMSELF IS IMMORTAL, WITH A POWER TO RIVAL THAT OF THE ENDLESS THEMSELVES."""
    
    play sound "LoveThy_SFXMOD_12_sfx7_somesay_master.wav" fadein 0.1
    centered """SOME SAY THAT THEY WERE LIVING GODS."""
    
    play sound "LoveThy_SFXMOD_13_sfx7_horatio_master.wav" fadein 0.1
    centered """THEY’RE DEAD NOW, THOUGH, WHILE WE THRIVE THROUGH {w=0.3}OUR BROTHER, {w=0.3}OUR GOD... {w=2.7}HORATIO."""
    nvl clear
    play music "sfxmod_dream_slice_v5_final.wav" fadein 3.0 # sfxmod start
    pause 11.0 # sfxmod end

label dream:

menu:
    "Go towards the light.":
        stop music fadeout 3.0
        jump light
    "Stay in the dream a bit longer.":
        jump stay
      
label stay:
    "I want to hear this beautiful song... {w=4.5}forever...{w=8.5}and ever..."
    "I don't want to wake up just yet."
    jump dream
    

label light:
    play ambient "CloneLab.ogg" fadein 1.0 fadeout 1.0
    play sound "CloneLab_Footsteps.ogg" fadein 3.0
    "I think I hear someone."
    pause 2.0
    play music "Lab.ogg" fadein 10.0 
    
    show blue closed at left with easeinleft
    show blue at left
    v open "All the clones in this batch are to be decanted today."
    show blue closed
    v "I know this is earlier than the original schedule planned for, but the schedule didn’t plan for two patrol squads in the heartland of the Empire to go missing within a month."
    show blue opensmile
    v "Just follow my lead and the procedure will be fine. If you do well today, you might be promoted to Junior Lab Technician earlier than expected!"
    
    show soratio baseside at right with moveinright:
        xzoom -1
    show soratio at right
    v2 "This would be amazing, Sir."
    show soratio closed
    show blue oneup closed
    v "Don't interrupt."
    show blue neutral open
    hide soratio
    
    v"Most of the process is automated, but contrarily to some of the Clone Hatching sequences you’ve seen in class, the final steps are still done by hand."
    
    v oneup large "There are procedures for which a computer cannot be trusted, and you have to rely on steady Horatio judgement."
    show blue closed
    v"Back to our specimens. You will handle clone berths A through L, I'll do the other row."
    show blue laugh oneup
    v happy "Pick one and get to work!"
    hide blue
    scene bg-lab1 with fade
    play movie "bg-lab-animated.webm" loop
    show movie with dissolve    
    show soratio pad opensmall oneup at right with moveinright:
        xzoom -1

    show soratio closed at right

    v2 "Can you hear me?"
    "One moment I’m asleep, and the next I’m alive."
    "My eyes struggle to adjust to the brightness of the room."
    
       
    "It slowly comes into focus."
    "There’s a man in a white and blue uniform bent over me, with a bald, elongated head, and a look of concern on his face."
    
    show soratio opensmall
    v2 "Hello?"

    "\"... Hrm?\""
    show soratio neutral
    v2 "Ah, you’re awake, great."
    show soratio closed
    v2 "I have a couple of questions for you."
    show soratio closedsmile happy
    "He shoves the small holopad he’s holding in my face." 
    "It’s very bright and I recoil slightly, groaning something." with flash

    
    "He starts flipping through the pages when the other voice calls out."

    v "Come over please, I need your help."
    show soratio baseside at right with dissolve
    show soratio at right
    "The man looks for a place to put down the holopad, then realizes his outfit doesn’t have pockets big enough to accommodate it."

    v "Tergus F07, I’m talking to you. Get moving!"
    hide blue
    show soratio opensmall
    v22 "Yes Sir, coming! Uh…"

    "He looks down at me and ends up putting the tablet down next to me."
    show soratio alt base
    v22 "I’ll be back."
    hide soratio with easeoutright
    "He trots away and out of sight."
    "I struggle to prop myself up on one elbow, so I can keep watching him."   
    "He stops at a platform some distance away, on which lies a naked man. Another uniformed man is standing nearby, looking at a side panel next to the platform."
    "All three of them look exactly alike. {w=0.5}Brothers?"
    show soratio at right:
        xzoom -1
    with moveinright   
    show soratio at right
    v22 "How can I help, Sir?"
    show soratio closedsmile
    show blue closed at left with easeinleft
    "The uniformed man points at the naked form in front of him."
    show blue open
    v "This clone is faulty. The lights are on but it seems nobody’s home."
    show soratio closed neutral
    show blue closed
    "I try to make sense of all this. These people are… clones of one another?"
    show soratio opensmall
    v22 "What do you mean, Sir?"
    show soratio closed
    v """Well, it’s obvious, isn’t it? He can hear us but he can’t respond. 
    
    Something must have gone wrong during the process. On the outside, he’s fine, but his motor or educational imprinting is flawed.""" 
    
    v @opensmall """The result is this useless hulk. What good is it being beautiful if you can’t make everyone proud? 
    
    The cloning vats are near-perfect, but every once in a while, some other part of the pipeline produces a disgusting abnormality."""
       
    v "Let’s take care of him and chalk him up as a total loss."
    play music "Bad_End.ogg" fadein 1.0 fadeout 3.0
    show soratio angry at right:
        xzoom -1
    v22 "What do you need me to do?"

    v @opensmall "Simple. Take his legs."
    
    "The man called Tergus F07 grabs the unmoving clone by the ankles and looks at the other clone."
    "The latter has passed his hands under the clone’s arms and pulls him off the platform with a grunt."
    show soratio angry closed at right:
        xzoom -1

    v "We’ll put the body in the recycling chute, this way we get the nutrients back. Think of it as his way of contributing."

    "Both of them tug and pull haphazardly, and before long they’re panting."

    v @open "We can’t afford to show weakness at this time... or ever. Everything and everyone is perfect... and beautiful... in the Horatio Empire."
    v @oneup "It’s a kindness we’re doing to him... when you think about it."

    "I watch as they come nearer and realize that there are about a dozen other men on the platforms."
    "All of them are in various states of lying down or sitting up, looking at the grotesque scene with mild interest."
    "Every single one of them is a carbon copy of the trio in front of us."
    "I catch my reflection in a surface, and suddenly I realize. I, too, am one of them. {p}A clone. {p}Of them."
    "A Horatio."
    show soratio angry at right:
        xzoom -1
    v open @angry "It is a good thing we caught this now, so we can fix it before the ceremony. Our records need to be perfect."
        
    v @oneup """Otherwise, we’ll end up in a backwater station, decanting only He-knows-what! This is a small blessing, really.
    
    For you and me, I mean. For him, not so much."""
    show blue closed
    "The trio passes in front of me, and for a moment, my eyes lock into those of the faulty clone. Far from being dead inside, I can see fear radiating from him."
    "He knows he’s going to be killed off because he’s imperfect!"
   
    "I sit up and try to figure out what these tests are about. I don’t want to follow this guy in the recycling chute."
    "Every time I think about what a memory test entails, I come up with a blank. I… I think that’s the issue right there."
    "My body’s functional, I can understand what people are saying, and think, but… there’s nothing of the memory implants they mentioned."
    "I’m a blank slate."
    show soratio closed at right:
        xzoom -1
    v "Prop him up while I open the chute."
    hide blue 
    hide soratio with dissolve
    play sound "GenericRoom_TrashMachine.ogg"
    stop music fadeout 3.0
    "I gotta do something about this."
    "I turn around to look at the clone next to me, who is gazing about with an air of studied detachment. Our eyes lock and his expression shifts to a scowl."
    "I haven’t done anything to deserve it, although I’ve been fidgeting on my platform."
    
    v3 "What are you looking at, substrate?"

    "I rummage for a good come back."
    "All of these guys seem to hold perfection in very high regard. I know what’ll shut him right up."

menu:
    "You're ugly.":
        jump ugly
    
    "I'm just wondering whose clone you are... surely you can't be one of us?":
        jump oneofus
        
label ugly:

    "\"You're ugly.\""
    
    "He goes pale with anger and mutters something in response."
    jump test
        
label oneofus:
    "\"I'm just wondering whose clone you are... surely you can't be one of us?\""
    
    """It takes him a moment, but eventually he gets it.
    
    He reddens and mutters under his breath. It definitely doesn't sound friendly."""
    jump test

    
label test:
    """I realize we seem to be easily provoked and causing a scene might just be my way out.

    I pull my legs off the platform to do just that when I catch something about to fall off. It’s the holopad Tergus F07 has left by my side. 
    
    Maybe there’s some information in there that’d help me cheat my way through the test instead? What should I do?"""
    
menu:
    "Provoke a fight as distraction.":
        $ violence_points +=1
        $ fought = True
        jump fight
    
    "Look for information to cheat on the test.":
        $ cheated = True
        jump cheat
        
label fight:
    """No time to investigate.
    
    I put the holopad down on the platform, hop off and throw myself at my neighbor, screaming."""

    "\"WHAT DID YOU JUST SAY TO ME?\""
    play sound "CloneLab_Punch.ogg"
    "He is taken aback by my sudden outburst and I land a beautiful first slap, that almost throws him off the platform." with vpunch
    
    """I try to shove him onto the ground.
    
    He grabs me by the head, which is surprisingly effective, and we both fall to the floor with a crash.
    
    We start swiping at each other with our eyes closed, grimacing and trying to protect our face from the blows.

    The other clones are coming around us and are chanting \"Fight! Fight! Fight!\" Others are saying things like \"Punch his ugly face!\" and \"Show him who’s got the best genes!\"

    We are not hurting each other much, but it gets tiring quickly."""
    
    """Thankfully, the lab technicians arrive and separate us.
    
    We’re both panting and sweaty, which is unpleasant to me but seems to be absolutely awful for the other guy. {w=0.3}I win this round."""
    show blue at right with easeinright

    v """That’s enough, you two!
    
    You’re going to mess up your pretty faces! Who’ll even look at you after that, huh?
    
    What were you even fighting for?"""

    "This is do or die."
    
    "My opponent looks defiantly around and spits out:"

    v3 "He was looking funny at one of his betters."
    v3 "I told him to back off."

    "\"He called me a substrate! I clearly have the better genes!\""
    
    "The lab technician in charge looks at Tergus F07 and snickers:"
    show soratio closed angry at left with easeinleft
    v "Sort these idiots out, I’m going to let Indoctrination know we’ve got a feisty bunch."
    
    "He leaves the room."
    hide blue with easeoutright
    
    "Tergus F07 sighs and pinches the bridge of his nose."
    show soratio opensmall at right:
        xzoom -1
    with easeinleft
    v22 """Ugh… okay.
    
    Everyone, line up against that wall, we’ll do a quick assessment and you’ll be on your way."""
    
    show soratio closed 

    v22 """You two idiots sit in the idiot corner over here until we’re done.
    
    You’re clearly functioning and you seem to have the exact amount of jealousy that you need."""
    show soratio oneup 
    v22 """You should probably be tested for stupidity down the line. I’m sure you’ll make a great first impression in Indoctrination."""
    
    hide soratio with easeoutleft
    
    """My opponent seems annoyed.
    
    I’m doing my best to mimic his expression, but I’m secretly relieved. We passed the test!
    
    I sit in silence, my blood pumping in my ears, waiting until the testing is done and we’re called away."""
    jump orientation

label cheat:

    """I’ll go for the subtle approach.
    
    I sit back down and put the holopad in my lap.
    
    There are a number of tabs open: medical procedures, inventories, the news.
    
    There’s a tab that seems to be a serial called \"Forbidden love.\"
    
    I press the button in front of the image and the show resumes. The sound is off, subtitles are on. I can only guess that Tergus F07 is not as studious as he appears.
    
    The show is taking place in a richly decorated room, with draperies hanging off the walls, pieces of ornate furniture, elongated vases and tall chalices.
    
    Everywhere, portraits, statues, 3D holograms, representing me. Well, the me who’s in charge. {w}We seem really into ourselves.
    
    And right on cue, there’s another me onscreen. He is arguing about something with somebody we can’t see.
    
    Two other Horatios come into view, one dressed as a soldier, the other in civilian clothes.
    
    The soldier is demanding a rebellion on a distant colony be met with force, while the civilian is offering a more measured approach, presenting it as magnanimous.
    
    The argument goes back and forth for a bit, with the main me, whom they call Prime, eventually making the call. He’ll be magnanimous and offer the rebels a chance to redeem themselves.
    
    The soldier stomps off, while the other guy sticks around and shuffles closer to him. They share a quick embrace before he slinks off. {w}I fast forward a bit. 
    
    The soldier comes back in the next scene, in some sort of parlor. Prime and him exchange some oblique remarks and it becomes clear that in the shadows, things are going to get pretty bad for the rebels anyway.
    
    So that’s the way things are done around here? {w=0.3}Okay.
    
    And then the soldier tears off his uniform, revealing a perfectly smooth chest. The two exchange a smoldering look, their lips meet with passion, and they fall to the ground. {w}Oh."""
    play sound "CloneLab_Footsteps.ogg"
    "I hear footsteps approaching and I swiftly put the tablet back down."    
    "Tergus F07 is coming my way."
    show soratio at right with easeinleft:
        xzoom -1
        
    """I rest my hands on the platform and do my best to look detached.
    
    I’m ready to play the part."""
    
    v22 oneup opensmall "Right."
    show soratio pad
    "He picks up the tablet, swipes through it, then looks up at me."

    v22 """... Right.

    Okay, I’ll ask you a couple of questions, just making sure everything’s fine."""

    "\"Let’s get this over with, pal. I’ve got places to be.\""
    show soratio closed 
    v22 """Uh… settle down, please. This’ll only take a moment.
    
    Looks like your motor controls are working fine…"""
    
    v22 """Let’s tick that box and move on to the memory test.
    
    I’ll make it short."""

    show soratio oneup 
    v22 "What is the name of the first and foremost, our god, creator and benevolent leader?"
    
menu:
    "Horatio Prime.":
        $ primo = True
        jump prime
     
    "The big forehead in the sky.":
        $ cheated_forehead = True
        jump forehead
        
    "The man of my dreams.":
        $ dreamboat = True
        jump dreamy
        
label prime:
    "\"Horatio Prime.\""
    "Tergus F07 looks at me and nods in approval."
    show soratio opensmall neutral
    v22 "Okay, you’re officially a fully-functioning Horatio."
    v22 "Sit tight and wait until we’re done processing everyone else."
    show soratio closed
    "With that, he moves on, taking his holopad with him."
    hide soratio with easeoutright
    "Well, that was easy."
    "I lay back on the platform and relax."
    jump orientation

label forehead:
    "\"The big forehead in the sky.\""
    "Tergus F07 looks at me directly in the eyes and for a second I’m afraid that I’ve done something too stupid."
    "Then the edge of his mouth curls up and he breaks into a smile."
    show soratio laugh
    v22 """I mean, you’re not wrong…
    
    If you intend on calling him that to his face though, please let me know in advance so I can be there and watch what happens to you."""
    show soratio neutral opensmile
    v22 "Okay, you’re officially a fully-functioning Horatio."
    
    "Sit tight and wait until we’re done processing everyone else."
    
    "With that, he moves on, taking his holopad with him."
    hide soratio with easeoutright
    "I lay back on the platform and relax."
    jump orientation

label dreamy:
    "Tergus F07 lowers his holopad for a second and swoons:"
    show soratio opensmile happy
    v22 "I know, right? Sooo dreamy!"

    "He inhales sharply and looks into the distance."
    show soratio baseside
    "His gaze loses focus for a moment, and then he comes back."
    
    show soratio base
    v22 """Woops.
    
    Sorry, got caught in the moment.
    
    You’re good to go!"""
    show soratio neutral
    v22 """Well, don’t go anywhere.
    Sit tight and wait until we’re done processing everyone else."""

    "With that, he moves on, taking his holopad with him."
    hide soratio with easeoutright
    "I lay back on the platform and relax."
    jump orientation

label orientation:
    stop music
    play movie "bg-lab-animated.webm" loop
    $ renpy.pause(2)
    show movie with fade
    "Some time later, the assistant comes back."
    show soratio closed neutral at right with easeinright:
        xzoom -1
    v22 """Thank you for waiting.
    
    I’m gonna ask you to please head to Wardrobe in the next room over, where you’ll find your station uniform."""
    
    show soratio oneup opensmall
    v22 "Any one will do, they’re all the same size, obviously."
    show soratio open
    v22 """After that, you’ll be directed towards Indoctrination.
    
    This will be followed by dinner, Orientation, and you’ll be shown to your quarters."""
    show soratio baseside
    v22 "Now, this way please…"
    
    hide soratio with easeoutleft
    
    "The door to the next room opens, and we step inside."
    play sound "GenericRoom_DoorOpen.ogg"
    stop movie
    stop ambient
    
    scene bg-genericroom with dissolve
    play ambient "GenericRoom.ogg" fadein 1.0 fadeout 3.0
    play movie "bg-genericroom-animated.webm" loop
    show movie
    
    if violence_points > 0:
        "I try to put a few people between me and my neighbor from the lab."
        
    """There’s a few tables at the far end of the room. Uniforms are neatly stacked and folded, next to one another. 

    We look at one another uneasily, until someone steps forward and grabs a uniform, looks at it warily and puts it on.
    
    We follow suit. It is some sort of green jumpsuit, with two deep pockets.
    
    It closes with a simple zipper in the front. The uniform is a pretty snug fit, and the fabric seems sturdy, yet comfortable.
    
    I notice there are pairs of light boots under the table, so I take a pair. They’re a bit tight.

    I put my hands in my pockets and look around me, waiting for what’s next.
    
    The wait doesn’t last: after a minute, another door opens. The assistant from before is holding his holopad and peers inside."""
    show soratio neutral opensmall at right with moveinleft:
        xzoom -1
    v22 """Okay, uh… {w=0.3}
    
    Well, normally there’s somebody else to show you the way to Indoctrination."""
    show soratio open
    v22 "We’re a bit short-staffed at the moment, apparently."
    show soratio closed
    "There’s a grumble from my neighbors at this lack of decorum."
    show soratio open
    v22 """I’ve lit up a path on the holoscreens, it will guide you there. Just proceed down that hallway to the concourse and follow instructions.
    
    Sorry about that."""
    hide soratio with moveoutleft
  
    "I shuffle out of the room, and hesitantly walk down the hallway, hoping that I won't get lost."
    stop movie
    scene bg-hallway with dissolve
    play movie "bg-hallway-animated.webm" loop
    show movie 
    play ambient "Hallway.ogg" fadein 1.0 fadeout 2.0
    
    """The others are following me, although at a distance, no one seeming to want to take the initiative. They seem to be familiar with our surroundings, but not with the layout of the station.
    
    At least none of us has to pretend...
    
    I think no one wants to be the one going down the wrong way and making a mistake in front of the others.
    
    I’ve seen crossroads twice and stuck to the path indicated by an arrow on the wall screens. So far, so good.
    
    I keep walking. {p}The others follow."""
    play ambient "Concourse.ogg" fadein 6.0 fadeout 2.0
    play music "Encounters.ogg" fadein 6.0 fadeout 2.0
    "Eventually I hear a murmur in the distance, which grows to a distinct noise as I draw nearer."
    stop movie
    scene bg-concourse1 with dissolve
    
    
    """I see some bright lights in the distance, and a much more colorful environment.
    
    I step out onto a plaza, a cathedral of green and gold.
    
    There are columns and glass everywhere, with manicured trees and shrubs in every corner, and overhead, an immense glass canopy. {w=0.3}\n This must be the concourse.
    
    There are lots of other people here, all wearing the same jumpsuits as we are. Probably fresh new clones, just like us?
    
    Even my jaded brethren around me are all murmuring among themselves in tones of wonder and amazement, as if talking out loud might make the wonders fade away."""

    "\"This way, please!\""
    
    """The voice cuts through the noise effortlessly, and in a moment, the conversations go quiet.
    
    A Horatio has appeared on an immense holoscreen, inviting us to move along.

    There are more holo projections in the hallways leading to… {w=0.3}what was it? {w=0.3}Indoctrination?
    
    That sounds unpleasant.
    
    Nonetheless, I follow the crowd."""
    stop music fadeout 3.0
    play ambient "GenericRoom.ogg" fadein 2.0 fadeout 2.0
    scene bg-classroom-text
    with fade
    
    """We meander through the corridors for a couple of minutes before we reach our destination.
    
    This is a huge room covered in rich materials, from the deep carpeting in the middle of the room, to the paneled walls.

    There are long rows of wide, comfortable-looking seats, all facing a wall covered with an immense holoscreen.
    
    Low columns form arcades and run along the walls of the room. It’s… beautiful."""
    
    show red closed at right 
    play music "Broratio.ogg" fadein 1.0 fadeout 3.0
    """A Horatio in a red suit is standing with arms crossed, on a low podium in front of the holoscreen.

    He has a look of studied annoyance on his face. Once all of us are inside the room, he speaks up."""
    show red open
    v4 "May I have your ATTENTION please!"
    "The crowd falls silent."

    "His voice carries across the room, and even from somewhere near the entrance, I can easily hear him."

    v4 "Please take a seat."
    v4 "Go all the way through the row, don’t just hog the center seats, you’ll hear me just fine from the sides as well."
    show red closed
    "There’s a bit of a rush forward from the new clones to do exactly the opposite of that. "
    
    "Soon enough, a cluster of Horatios are sitting in the \"prime seats\" and preventing the rest of the file from moving along."
    show red open
    v4 "Oh for His sake…" 
    v4 "Go around the audience and find a seat from the other side, and occupy the back and side seats if necessary."
    show red closed
    """I position myself carefully in a spot at the back.
    
    I’d rather watch what’s happening and do my best to blend in.
    
    The Horatio in the red outfit seems about to continue, when another moves in from the shadowy arcades to the side of the room and climbs the steps to the podium."""
    show red open
    show poratio at left with easeinleft
    show red baseside closed
    play music "Poratio.ogg" fadein 1.0 fadeout 1.0
    """His feet echo softly on the green marble tiles. The red Horatio closes his mouth and deflates a bit.

    The other one is moving pretty slowly, and from the envious looks of my closest neighbors, I can only imagine that it’s on purpose. 

    He dismisses red with a casual gesture of the hand and a smile.
    
    Red Horatio leaves the stand."""
    hide red at left with easeoutleft
    show poratio:
        xzoom -1
    show poratio at right with easeinleft
    
    """With a grin, the second Horatio turns to us, his cape flowing in an emphatic demonstration that he’s here, and demands our attention.

    When he speaks, his inflections are slightly different.
    
    I surmise that he probably spends a lot of time speaking in public."""
    show poratio opensmile:
        xzoom -1
    
    v5 """Thank you, Second Rate Master Sergeant Exrus B12. That’ll be all.

    To each and everyme, welcome to Kappa Station, finest in the cluster."""
    show poratio closedsmile
    v5 """Your memory imprints do not cover the last couple of decades, since the last backup was distributed among cloning facilities in this quadrant.
    
    Therefore, a lot of the information you know, and the things you know you know, may be outdated.
    
    This is a crash course in what has happened while you were sleeping."""
    show poratio at left with easeinleft
    scene bg-classroom-horatio
    show poratio opensmile at right:
        xzoom -1
    v5 """Let’s start with the most important thing: etiquette with regards to my person. You may address me as Third Rank Esteemed Grand Headmaster Radchaai Aeternus P02.
    
    In settings that only comprise Initiate-level and above station personnel, you may call me simply Grand Headmaster, or Master Aeternus P02.
    
    In public, you will always address me as Your Likeness.
    
    Provided that the honorifics have been properly given and received, in a small setting, you may subsequently call me Sir."""
    show poratio closedsmile
    "He pauses for a second."
    scene bg-classroom-question
    show poratio opensmile at left:
        xzoom -1
    show poratio at right with easeinright
    v55 """Now that this is covered, let us move on to secondary topics.

    First, your own identity. It is with a great pleasure that I deem you all Initiates.
    
    More specifically, your full name will be First Level Initiate Meghrez, since this is your facility of origin, and then your chosen name, along with your decanting berth and batch number. You are batch 21 of this administration.
    
    There is a holopad on your desk, you may use it now to approve your suggested name or pick another one."""
    hide poratio
    """I look at the holopad resting atop the desk. \nThe screen reads: \"First Level Initiate Meghrez \[Placeholdus\] F21.\"
    
    Is that… Do I really want to be called by that name?"""
    
menu:
    "I guess Placeholdus F21 is my name now.":
        jump Placeholdus
     
    "I’m sure I can find something better.":
        jump bettername
        
label Placeholdus:
    play sound "Academy_GoodAnswer.ogg"

    "First Level Initiate Meghrez Placeholdus F21."
    
    """I look at my reflection in the glass panel of the holoscreen. Yep, that looks like me. Placeholdus F21 for short.
    
    Plus, by picking the default option I’m sure I won’t stick out from the crowd."""
    $ player_name = "Placeholdus"
    
    jump speech_contd
    
label bettername:
    """I rake my mind for an idea. Could I randomly type in letters?
    
    Wait, no, I’ll be stuck with that. Better find something discrete so I blend in.
    
    I press the \"DELETE\" button.
    
    The words \"Enter your name.\" appear instead."""
        
    $ player_name = renpy.input("Enter your name.")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Placeholdus"
    if "horatio" in player_name.lower():
        jump retry
    jump name

label retry:   
    play sound "Academy_BadAnswer.ogg"
    "The words \"You cannot name yourself Horatio for you are not Him\" appear on the screen. \"If no satisfactory name is entered, you will lose naming privileges.\""
    "I guess there {i}is{/i} only one Horatio..."
        
    $ player_name = renpy.input("Enter your name.")
    if "horatio" in player_name.lower():
        $ player_name = "Placeholdus"
        $ cheeky_points +=1
        play sound "Academy_BadAnswer.ogg"
        "The screen flashes red before settling."
        "\"Report submitted to local leadership for attempted impersonation and possible maniacal delusion.\""
        "\"Default name selected. Your name is First Level Initiate Meghrez Placeholdus F21.\""
        "...{w=0.3}\nSo much for blending in."
        $ achievements.unlock("One And Only")    
        jump speech_contd

label name:  
    play sound "Academy_GoodAnswer.ogg"
    "The screen flashes green for a second after I hit the \"Submit\" key."
    "Okay, my name is First Level Initiate Meghrez [player_name] F21 now."
    "Hope it brings me luck."
    jump speech_contd

label speech_contd:    
    "The Horatio onstage must have some way of checking our progress, because after a moment, he continues."
    show poratio opensmile at right
    v55 """As Initiates, you need not address category X personnel or unsightly species you may encounter directly. You may find the closest underling to do that for you.
    
    Be aware that there are many new species that have been added to His Glorious Empire.

    Xenuglies aside, there might be some more aliens around the station. Do not be alarmed, they should all be tame.
        
    Generally, the rough and unwashed masses are kept away from their betters, but several client species are permanent residents aboard Kappa station.
    
    It is entirely possible that you’ll come across some of their representatives over the course of the next few weeks."""
    show poratio oneup
    v55 """Should you need to communicate with them, they are familiar with our speech and will attempt to replicate it… to the best of their ability.
    
    Most of the new species we have encountered have proven to be just as disappointing as we expected."""
    show poratio happy
    "He smirks. He flicks his wrist and pulls his belt buckle free."
    show poratio pad

    "With a wave, the buckle lights up, revealing a small holopad."
    
    "Fancy."

    v55 """Now, for a brief overview of what has happened in the last decades."""
    scene bg-classroom-ue
    show poratio pad at right
    v55"""Relationships with the so-called fledgling United Empire remain very cold.
    
    Representatives from their young leader, a male human called Zelevas, have refused vassalage under the auspicious leadership of Horatio himself.
    
    Similarly, they have repelled violently several attempts at claiming outer planets for our Empire. Proceed with caution."""
    scene bg-classroom-cravers

    show poratio pad neutral bottom at right
    v55 """Relationships with the robotic insectoid hive known as the Cravers are still at an all-time low."""
    
    show poratio opensmile
    v55 """They have eaten the last dozen envoys, as well as the ships they came on.
    
    The colony of Heka was deemed lost after we had to vitrify the surface in the year… 10191 After Him?
    
    Their strength would make a great addition to the Empire, but at this time we are not pursuing efforts any further."""
    scene bg-classroom-sophons
    show poratio pad at right
    show poratio base at left with easeinright
    show poratio at left
    v55 "Similarly, we are currently not in speaking terms with the Sophon Republic."
    show poratio bottom

    v55 "The diminutive know-it-alls have recently jumped the gun and seized the system of Ingris and… {w=0.3}wait, this happened centuries ago!"
    show poratio closed

    "He flicks through several screens on his holoscreen in rapid succession."
    show poratio large angry
    v55 "All this information is completely out of date!"
    v55 "Who messed with the geopolitics database?!"
    show poratio oneup base
    v55 "I am surrounded by complete idiots, I swear… {w=0.3}Nevermind this."
    show poratio closed neutral alt
    "He turns off the holoscreen, sighs, then continues."
    show poratio opensmile

    v55 """I guess I will be doing this from memory.
    
    It might be a bit patchy, something that your own memories will definitely encounter too once you start living in your body for a while.
    
    Something to do with having millenia of memories of Him..."""
    scene bg-classroom-academy
    show poratio happy at left
    v55 """Moving on, you might be wondering why so many of you are being decanted at this time, and for what purpose.
    
    This station is home to Horatio Academy, where the best and brightest of His siblings come from all across the Empire for further education."""
    show poratio opensmile

    v55"The best of these, in turn, get a shot at joining the other Academy, led by a Vodyani male called Isyander."
    
    show poratio baseside
    
    v55"""Ah, the Vodyani.
    
    Life-sucking ghouls who live in gigantic space arks and prey on the defenseless souls of our brethren."""
    show poratio base
    v55 "Except this Isyander fellow, who fled them and founded the Academy, a place that has grown into immense power."
    
    show poratio neutral 
    v55 "They have knowledge and mastery of Dust."
    show poratio opensmile
    v55 "Your purpose, if you end up among the chosen few, is to go there and... ‘acquire’ some of this knowledge and power, and bring it back for the glory of His Empire."
    show poratio base
    v55 "Finally, the why so many of you at once."
    show poratio open angry
    v55 "Well, two of our exploration vessels disappeared recently. They contained the brightest minds of this generation, our best shot at getting the knowledge we’re seeking."
    show poratio large
    v55 "They are gone now, and just a few very short weeks before Horatio Prime Himself is due to review our Academy cadets!"
    show poratio open
    v55 "Horatio Prime Himself is coming to Kappa station.{w=0.3} And we have no cadets."
    v55 "The shame this would bring to me, and to the whole station, would be unbearable."
    show poratio baseside
    v55 "Anyway you have got about, mmh, three weeks to become these cadets."
    show poratio opensmile neutral base
    v55 """There will be extensive training.
    
    There will be classes.
    
    There will be etiquette courses, and lessons of the latest courtly dances."""
    show poratio angry
    v55"There will be no failure{w=1}—{i}or else{/i}."
    
    if cheeky_points > 0 or violence_points > 1:
        jump warning
    else:
        jump speech_end

label warning:
    show poratio open
    v55 """I know some of you here have already looked for ways of distinguishing yourselves.
    
    You do not want me remembering your name."""

    "He looks at each of us individually, but his gaze seems to linger on me for just a beat."
    "Oh, so this is what shame feels like."

label speech_end:
    show poratio neutral
    v55 """Now, if you have questions, keep them for your instructors tomorrow.
    
    Time for you to get sustenance and retire to your personal quarters."""
    show poratio closed
    "He turns away and walks out the same way he came, under the arcades and out of sight."
    hide poratio with easeoutleft
    "This Aeternus P02 guy is something else."

menu:
    "What a jackass.":
        $ cheeky_points +=1
        $ jackass = True
        jump dinner_time
    "Guess that’s how people are around here...":
        $ itislikeitbe = True
        jump dinner_time
    "He has a certain allure.":
        $ allure = True
        $ koolaid_points +=1 
        jump dinner_time

        
label dinner_time:
    stop music fadeout 3.0
    "If I understand him correctly, I have three weeks to not only pass for a normal Horatio, but to become an outstanding specimen, worthy of sending on to steal secrets from a powerful alien entity."
    "Gotcha."
    "People have already started getting up when the other one comes back."
    
    show red closed at left with easeinleft
    play music "Broratio.ogg" fadein 1.0
    "Master Sergeant Something Something, I believe?"
    show red open
    v44 "Attention please!"
    v44 "You are now going to be provided with dinner."
    v44 "Follow me to the mess hall."
    show red closed 
    "Without waiting, he turns around, walks down the podium and off into the direction opposite the one we came."
    hide red at left with easeoutleft
    stop music fadeout 2.0
    "My brethren and I quickly follow."
    scene bg-mess1 with fade
    play movie "bg-mess-animated.webm" loop
    show movie 
    play ambient "MessHall.ogg" fadein 4.0
    """Finally we get there.
    
    Compared to the concourse and the room we were just in, this is a rather drab place. Somehow halfway between a spaceport and a hospital.
    
    It doesn’t look like a place to enjoy dinner as much as a place to eat… a place to feed oneself.
    
    Some of my… I guess classmates are already in line, and a few have already sat down to eat something I can’t quite identify yet.
    
    I have decided to say \"classmates\" since I can’t settle on whether we should be feeling any kinship towards one another.
    
    It does feel strange to hear “brethren” every other sentence, and I guess calling us cadets might be getting ahead of myself yet.
    
    The Headmaster’s speech didn’t really help normalize the situation, really.

    Someone bumps into me and I realize I’m holding up the crowd. {w=0.3}I get in line.

    I grab a tray and slide it on the rail.
    
    There are some odd kitchen utensils available, but I’m not sure what purpose they serve, so I compromise by taking a spoon from the lot.
    
    Upon closer inspection, I realize it’s a spork.{w=0.3}\n
    The future looks amazing.
    
    I look up at the people serving us food.
    
    They’re all Horatios too, wearing some sort of jumpsuit and looking pretty upset to be here."""
    play music "Doratio.ogg" fadein 1.0 fadeout 1.0
    show gray angry at right
    
    """One hands me a bowl of something I don’t quite recognize, serving me a mean look at the same time.

    I’m surprised by the direct eye contact and before I know it I’m saying:"""

    "\"Hello. Thank... you?\""

    "The Horatio lunch person is as surprised as I am, and frowns before saying back:"
    show gray opensmall
    v6 "Hello, enjoy your food."
    show gray closed
    """I’ve never before seen anyone be so begrudging in saying thank you.  
    
    But then again... {w=0.3}I've not seen many people.
    
    Take it easy, friend."""
    stop music fadeout 2.0
    hide gray with dissolve
    play music "Mess_Hall.ogg" fadein 3.0 fadeout 1.0

    """I shuffle along and look at the contents of my bowl.
    
    It’s… slop. {w=0.3} Definitely slop.
    
    I don’t know what it’s made of or what animal it came out of.
    
    Oh well, at least it seems hot. I grab some water and a piece of bread.
    
    No dessert options.
    
    Princely.

    I look around for a place to sit next to someone, hoping for a bit of… well, any kind of interaction.
    
    I sit down next to a bored-looking classmate, but after a few overtures and encouraging smiles, I give up.
    
    Everyme’s a bit on edge, and at other tables, it looks like people are focusing on the contents of their tray.

    The slop proves to taste just as awful as it looks.

    Once I’m done pushing about the last bits of food left, I stand up and go put my tray back where I’ve seen others do so.
    
    A fair bunch of people have left already, and looking at their trays, it seems like I’m not the only one for whom enjoyment of our dinner was minimal.
    
    Off to the side, there’s a guard ticking people off a long list and sending them down a hallway. It’s… that Master Sergeant dude again, I think?
    
    Some of us it seems have different face markings and uniforms, although I’m not sure what their meanings are.

    We lock eyes and he barks up."""
    play music "Broratio.ogg" fadein 1.0 fadeout 1.0

    show red at right
    v44 "What’s your name, First-Level Initiate?"
    show red closed
    "I enunciate clearly:"

    "\"I am [player_name] F21. First Level Initiate Meghrez [player_name] F21.\""

    "He searches for a few moments, then finds it."
    show red open
    v44 """Yes, [player_name] F21.
    
    Your living quarters are in Section B8, Level 9, Hallway 47, Door 32.
    
    It’s down this way. Just follow the signs. You can’t miss it."""
    show red baseside
    v44 "And if you do… you’ll figure it out eventually."
    stop music fadeout 1.0
    hide red with dissolve

    """I look the way he’s pointing at, a nondescript hallway off to the side, leading away from the concourse.
    
    I look back at the guard, but he’s turned his attention to someone else.

    Hesitantly, I set out to find Door 32."""
    play movie "bg-hallway-animated.webm" loop
    show movie with dissolve
    play ambient "hallway.ogg" fadein 1.0 fadeout 1.0

    """My footsteps echo softly down long, empty hallways.
    
    It takes me some time to realize I don’t see anyone else, although I sometimes hear voices echoing from afar."""
    play music "Solitude.ogg" fadein 1.0 fadeout 1.0
    play movie "bg-hallway-animated.webm" loop
    show movie with fade
    
    """I eventually find my way to Level 9, Hallway 47.
    
    It’s an even quieter area of the station, which is saying something.
    
    There are small doors there, tiny affairs compared to the ones on the main concourse.
    
    Even the ceiling is much lower, about two meters high.
    
    The lighting is a mix of neon glare and the ever-oppressive flicker of a tube that just refuses to give up the ghost.

    I look around me to get my bearings. It seems I’m nearly at the end of the hallway, where a bend leads to some sort of control system for life support.
    
    I guess I’m getting the finest air in the area then?
    
    With one last look towards the map, I start down the hall. 

    Door one… Two…"""
    
    play movie "bg-hallway-animated.webm" loop
    show movie with fade
    
    """... Thirty-one… Thirty-two. This should be it.
    
    I look around.
    
    Might be the finest air in the area, but boy oh boy, this end of the hallway looks like it hasn’t seen a mop in weeks.
    
    There are strange sounds coming from the next door over, which must be the life support control room. Ominous.
    
    Is this the right place?

    Section B8, Level 9, Hallway 47, Door 32. {w=0.3}Yup. No doubt, this is me."""
    stop music fadeout 3.0
    """I pull the heavy metallic door open with a groan and step inside."""
    play sound "PersonalQuarter_DoorOpen.ogg"

    play ambient "PersonalQuarters.ogg" fadein 1.0 
    play movie "bg-home1-animated.webm" loop
    show movie with dissolve
    play music "Home.ogg" fadein 3.0 fadeout 1.0

    """From my vantage point, I survey my new kingdom.
    
    From left to right: there’s a tiny sink for my ablutions, a mirror that doubles as a holoscreen, a toilet with no lid, a closet, a narrow bunk with a blanket and a pillow, some almost empty shelves... and we’re back to the door.
    
    All in a cylinder, about two by four meters. {w=0.3}Cosy. 

    Well, this may not be the warm embrace of a cloning berth, but it will do. At least I have the place to myself.
    
    I pull the door closed behind me.
    
    There’s a distracting buzzing coming from an overhead fan. \"The finest air,\" huh.
    
    I sit down on the bed and look about. It’s a bit too hot in here now that the door is closed.
    
    There are actual physical controls in a panel by the entrance, so I turn the temperature down a notch."""
    play sound "PersonalQuarter_AirVentFailure.ogg" 
    queue sound "PersonalQuarter_AirVentFailureLoop.ogg"

    "The buzzing increases to a screech. Is something scraping on metal?{w=0.3} There is no way I can sleep with this thing on!"
    stop sound fadeout 3.0
    "I turn the knob back up to its original level, and the metal screech subsides."
    
    """Ugh.{w=0.3} Screw it, that’ll do it for tonight.
    
    I plop myself down on the bed, turn off the light and pull the blanket over my head. 

    There’s a sinister rumble in my belly. {w}That doesn’t bode well…"""
    stop music fadeout 3.0

    $ prism.ending_selected_event("Day1")
       
    jump day_2