# Declare characters with name colors
define n = Character("Nitro", color="#ffffff")
define i = Character("Isabella", color="#f48fb1")
define p = Character("Peter", color="#90caf9")
define m = Character("Max", color="#aed581")
define s = Character("Serena", color="#ffcc80")
define y = Character("Yong", color="#ce93d8")
define j = Character("Jordan", color="#80cbc4")

# Image declarations

# Nitro (3 expressions)
image nitro neutral = "images/Characters/Nitro_neutral.png"
image nitro talk = "images/Characters/Nitro_talk.png"
image nitro thinking = "images/Characters/Nitro_thinking.png"

# Isabella
image isabella smile = "images/Characters/Isabella_smile.png"
image isabella serious = "images/Characters/Isabella_serious.png"

# Peter
image peter neutral = "images/Characters/Peter_neutral.png"
image peter concerned = "images/Characters/Peter_concerned.png"

# Max
image max grin = "images/Characters/Max_grin.png"
image max sketching = "images/Characters/Max_sketching.png"

# Serena
image serena smile = "images/Characters/Serena_smile.png"
image serena focused = "images/Characters/Serena_focused.png"

# Yong
image yong calm = "images/Characters/Yong_calm.png"
image yong shrug = "images/Characters/Yong_shrug.png"

# Jordan
image jordan chill = "images/Characters/Jordan_chill.png"
image jordan intense = "images/Characters/Jordan_intense.png"

# Backgrounds
image bg studio = "images/Backgrounds/bg_studio.jpg"
image bg meeting = "images/Backgrounds/bg_meeting.jpg"
image bg white = "#ffffff"

image bg salon morning = "images/Backgrounds/bg_salon 1.png"
image bg salon midday = "images/Backgrounds/bg_salon 2.png"
image bg salon night = "images/Backgrounds/bg_salon 3.png"
image bg bunker = "images/Backgrounds/bg_bunker.jpg"
image bg empty school = "images/Backgrounds/bg_emptyschool.png"

#Music

define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.7
define config.default_voice_volume = 0.7

define bad_words = ["fuck", "shit", "bitch", "asshole", "cunt", "bastard", "dick", "slut", "faggot", "ligma", "cum", "pussy", "stupid", "idiot",]

# Start of the game
label start:

    play music "audio/Echoes.wav" loop fadein 1.5

    $ player_name = ""
    $ attempts = 0
    $ valid_name = False

    while not valid_name:
        $ player_name = renpy.input("What's your name?").strip()
        $ attempts += 1

        if any(bad_word in player_name.lower() for bad_word in bad_words) or player_name == "":
            if attempts >= 3:
                $ player_name = "Basic Player"
                "Fine. We'll call you [player_name]."
                $ valid_name = True
            else:
                "Be serious here, what is your name?"
        else:
            $ valid_name = True

    $ player = Character("[player_name]", color="#a0e7e5")

    scene bg white
    with fade

    show nitro thinking at center
    with dissolve

    n "Alright... this is it."

    scene bg studio
    with fade

    show nitro neutral at center
    with dissolve

    n "Welcome to the Tree of Life project [player_name]."
    n "This is a tech demo to showcase the start of our visual novel."

    show nitro talk at center
    n "I'm Nitro — the producer, director, and one of the writers."

    n "Let me introduce the people bringing this to life."

    scene bg meeting
    with dissolve

    # Isabella
    show isabella smile at left
    i "Hey! I'm Isabella, co-producer and rigger. I make sure our characters don’t fall apart."

    show isabella serious
    i "Unless Max hands me another 80-joint tentacle rig related to a cosmic horror since lamby exists in our DND campaign..."

    hide isabella

    # Peter
    show peter neutral at center
    p "Peter here. I’m the co-writer. My job? Kick ass and eat bubblegum and help make sense of Nitro’s madness."

    show peter concerned
    p "Seriously though, the lore is getting bloody deep."

    hide peter

    # Max
    show max grin at left
    m "Max, reporting in. I storyboard the project faster than (Insert Actor's recommendation here). You want angles? Eye of a Beholder, a rad soundtrack giving Disco Elysium? I got you."

    show max sketching
    m "Unless you change the script again. Please. Stop."

    hide max

    # Serena
    show serena smile at right
    s "Hi! I’m Serena, the animator. I bring the sketches to life."

    show serena focused
    s "Also: I may not sleep until this opening sequence is done as I don’t want the team to abandon me."

    hide serena

    # Yong
    show yong calm at left
    y "Hi I build everything. Props, characters, sets... and even the glitchy vending machine."

    show yong shrug
    y "Maya and I are in a love-hate relationship, and don’t ask me whether Mari or Substance — I'm still getting over it."

    hide yong

    # Jordan
    show jordan chill at right
    j "Well I’m a lighter but I also can code, troubleshoot, I cry in Python."

    show jordan intense
    j "Also… if it’s broken, it probably worked before you touched it."

    hide jordan

    scene bg studio
    show nitro thinking at center
    with fade

    n "And together, we’re building something special."

    n "Hopefully we’ll expand the art team soon, Hopefully showing this tech demo can help explain the process easier to Sarah and Charlotte, and would love to have Daniel hop onboard story unless we find a way to involve Houdini."

    # Cycle through Salon background times
    scene bg salon morning
    with fade
    show nitro talk at center
    n "This Tech demo is to practice and look back on how Renpy works."

    scene bg salon midday
    with dissolve
    n "From characters, transitions, expressions, scenes even day to night cycles — though just ignore the time here, couldn’t find a midday image :P."

    scene bg salon night
    with dissolve
    n "At night? Well, we are all active at night playing League of Legends, watching anime, and most of our crew have DND nights."

    # Bunker scene with new music
    scene bg bunker
    show nitro neutral at center
    with fade

    play music "audio/Nomad.wav" loop fadein 0.2

    n "And of course, don’t forget this game will have a ton of secrets — military thriller, medical thriller, and psychological thriller. So this project aims to go dark and to evoke emotions and pull reactions out of the player."

    # Whisper scene
    scene bg empty school
    show nitro thinking at center
    with dissolve

    stop music fadeout 1.0
    play music "audio/whispers.wav"

    n "{font=fonts/whisper.ttf}...and we can whisper secrets to not get caught and die — this was a great way to learn how fonts work.{/font}"

    stop sound
    $ renpy.pause(0.5)  # Optional: smooth audio transition
    play music "audio/Echoes.wav" loop fadein 2.0

    # Player choice
    menu:
        "Meet the People.":
            jump meet_artists

        "or Meet the people.":
            jump meet_tech

label meet_artists:

    scene bg meeting
    with dissolve

    show max grin at left
    show serena focused at center
    show yong calm at right

    n "This trio crafts our visuals from sketch to screen."

    m "Fuck Yeah."

    s "Dont Abandon me."

    y "Bye Guys."

    return

label meet_tech:

    scene bg meeting
    with dissolve

    show isabella serious at left
    show jordan chill at center
    show peter neutral at right

    n "These three write a lot along side myself."

    i "From rigging to schedules, I make sure it runs."

    j "And if not, I rewrite it."

    p "And I write stuff as well."

    return