# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sasha Bennett")
define f = Character("Chad Johnson")
define m = Character("Mr.Smith")
define n = Character("Narrator")
define j = Character("Mrs. Johnson")
define b = Character("Mr. Bennett")
define e = Character("Elizabeth Bennett")

transform bg_fullscreen:
    xysize (1920, 1080)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene hallway at bg_fullscreen with fade
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show mc at center
    show bully at center with moveinleft
    pause 0.2
    show mc at right with move
    

    # These display lines of dialogue.

    f "Out of my way Bennet."

    n "Chad Johnson, the son of the principal, is a very rude and arrogant boy. He is the most popular boy in school and he always gets what he wants, when he wants it."

    s "Hey! You can't just push people around like that! You need to learn some manners."

    f "And who are you to tell me what to do? You're just a nobody."

    hide bully with moveoutleft

    n "Sasha heads to class, then remmebrs she has Mr.Smith's class next. And she hasn't doen her homework yet."

    s "Ugh this day is going terrbly. I wish I could start the day over again."

    scene bedroom at bg_fullscreen with fade

    show mc at center

    n "As soon as the words leave her mouth, Sasha blinks and she's in her bed in her room again. She looks around and sees that it's morning again."

    s "What the... How did I get back here? Did I just go back in time?"

    show little sister at left

    b "Sasha, are you awake yet? It's time to get ready for school."

    e "Sasha! You've been sleeping all day! It's time for school!"

    menu:
        "Snap at Elizabeth":
            s "I'm awake! You don't have to yell at me!"
            e "I was just trying to wake you up."
            n "Elizabeth sniffles, and walks away leaving Sasha alone in her room."
            hide little sister with moveoutleft

        "Go under the blanket":
            s "Just five more minutes..."
            n "Sasha pulls the blanket over her head."
            e "Sasha, you still need to get ready for school!"
            s "Ok fine, just give me a minute."
            hide little sister with moveoutleft
    
    n "Sasha stays under her blanket thinking about why she's back in her room and not at school."

    b "Sasha! Get out of bed! You're going to be late!"

    scene bathroom at bg_fullscreen with fade

    n "Sasha takes a bath and gets ready for school. She then heads down to the kitchen where her dad and little sister are waiting"

    scene kitchen at bg_fullscreen with fade
    show little sister at left
    show mc at right
    show dad at center

    b "Sasha, Elizabeth told me that you yelled at her this morning. Is that true?"

    menu:
        "What's it to you?":
            s "Why do you care? It's not like you were there to see it."
            b "Mind you tone young lady. I am your father and I have a right to know what goes on in this house."
            s "Ever since mom died, you've been acting like a tyrant. You don't care about me, you only care about yourself."
            b "How dare you speak to me like that! You are grounded young lady. No going out with friends, no phone, no computer, and no TV for a month!"
            s "What? That's not fair! You can't do that to me!"
            b "I can and I did. Just get ready for school and don't forget your homework."
            jump bad_ending

        "Yea..? She came into my room without permission.":
            s "She came into my room without permission. I was just trying to get her to leave."
            b "Alright next time, ask her nicely to leave. Now get ready for school and don't forget your homework."


    # This ends the game.

    return

label bad_ending:

    scene black with fade
    n "Sasha's argument with her dad makes things worse. She spends the day grounded, and the distance between them grows."
    n "Bad Ending"

    return
