# Declare characters used by this game
define e = Character("Yuno")

# Declare images
image bg room = "images/Backgrounds/bg_room.png"
image yuno smile = "images/Characters/Yuno_smile.png"

label start:

    # Show the room background
    scene bg room

    # Show Yuno smiling at center
    show yuno smile at center

    # Dialogue lines
    e "I hope this test works. Still getting used to... everything."

    e "Sup Izy, Sup Jojo, Sup Max. This Tree of Life thing is bussin."

    # End the game
    return
