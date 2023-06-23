#Introduces the setting
print("""Having spent the last several years safely ensconced in the towers of 
Dwarrow Castle focused on the study and practical applications of Magic, you 
have learned all you can here. The Archmage, lightly placing a proud hand on 
your shoulder, presents you with a choice: “It is, as you know, not as safe out
there on the road and Wilderlands as it has been here. What will you take with
you?” He gestures with his other hand to three scattered piles of equipment.
\n""")

#sets up choice of equipment and creates loop back for invalid data
while True:
    first_choice = input("""First, to your left you see a long STAFF topped with a 
    shard of crystal you cannot quite identify, a simple pack filled with sundry 
    foodstuffs magically preserved against the jostling of traveland a map. 
    Aside the staff you see a wide brimmed hat and a good stout traveling cloak.
    Second, you see a good stout set of leather armor seasoned well and you catch
    a glimpse of the aural glimmer that denotes enchantments. A brightsteel DAGGER
    lays in front of the similarly outfitted pack next to it.
    Third you see a brightsteel suit of plated armor and matching LONGSWORD,pommel
    bright with enchanted gems and a roundshield bordered with similar gems.
    Another pack of provisions leaning against it.
    \nWhich set of arms will you take up for your first adventure?\n""")
#displays unique story start per user input 
    if first_choice.lower() == 'staff':
        print("""You take up the sturdy staff and feel the magic it houses 
        reacting favorably to you greeting you as it would an old friend. Sweeping
        the hat and cloak on, you take up the pack and nod to the Archmage who waves
        grinning. “Fair weather, and godspeed!” He shouts merrily over his shoulder as
        he turns to usher some younger students off to their respective destinations.
        \n""")
        break
    elif first_choice.lower() == 'dagger':
        print("""The dagger greets you as you pick it up and sings as you twirl it
        testing the balance. You get the feeling as you test it that it also is
        testing you. Reaching out with your magic you feel sentience and a weighing 
        of you, then a cautious opening and conjoining as the dagger accepts you,
        becoming almost a an extension of yourself. As you buckle into the armor
        you feel a surge of well being and you notice, you seem to blend with the
        shadows, the sparkling eyes of the Archmage, the only ones that do not
        slide past or seem to look through you he nods, winks and waves you on
        your way.\n""")
        break  
    elif first_choice.lower() == 'longsword':
        print("""Longsword: The armor clinks and clangs as you get it buckled
        snugly on. You feel a surge of strength as it embraces you and take up the
        shield placing it safely on your back then you turn, pick up the sword, and
        buckle it on, take up the pack and turn to nod to the Archmage. He grins 
        in his infuriatingly knowing way saying. “You will do very well indeed I 
        should think. We shall expect word of great things from you, I have no 
        doubt.” Then, over his should as he ushers a group of younger students away
        you only just catch it, “Well it looks like Agnost has found a friend
        though little they know it yet.” He waves you off still grinning and
        marches away robes flowing around him like the great fountain, as you turn
        your feet to the road.\n""")
        break
    else:
        print('Please select your equipment from the capitolized items offered.')
        continue
exit
       
#offers choice of direction 
while True:
    direction_choice = input("""You feel excited and perhaps just a little nervous as 
    you step outside the massive castle gate, and the crush of people going about their 
    day envelops you. You stop a moment taking in the scent of the city, and check your 
    map. You have a choice to make, which of the cardinal direction gates will you use 
    to leave Dwarrow: NORTH, SOUTH, EAST, or WEST?\n""")
#describes the region per user input looping back for invalid data
    if direction_choice.lower() == 'north':
        print("""You Set out through the Northern Gate to the road and set off to
        find the great Valdoth mountains. Stretching the length of the northern border,
        so tall and jagged as to be impassable overground, they house the Urd 
        Tharakh (mountain road), garrisons, and mystical Gates of Karkindur, 
        kingdom of the Dwarves.\n""")
        break
    elif  direction_choice.lower() == 'south':
        print("""You set out through the Southern Gate and along the path toward
        the billowing sands of the southern desserts, harsh but passible if you
        have access to a good guide or can find one. Mundane maps would avail you
        little there, as it is largely unexplored and as such contains dangers yet
        unknown by most men, though the elves have been said to send an expedition 
        every few centuries.\n""")
        break
    elif direction_choice.lower() == 'east':
        print("""You venture through Eastern gate, making your way toward the
        coast. Abounding in exotic people and tales, where men have built their 
        great cities and from which they set out on fabled longships, exploring
        the Infinite isles so named for the fact that they have not yet been able
        to explore so far that there is not some island (or a few) dotting the 
        horizon and beconing them ever onward.""")
        break
    elif direction_choice.lower() == 'west':
        print("""Leaving the Western gate behind, you set forth past the farms
        surrounding the outer wall, toward the setting sun where lie the ancient
        forests of the elves. Their living abroreal cities and wonderous gardens 
        legendary since time out of mind, rarely visited by the younger races. Very
        few had yet ventured beyond the fabled watchtowers of the Westenbrea,
        westernmost outpost of the Elves, and fewer still returned.""")
        break
    else:
        print('Please choose one of the captiolized directions offered.')
        continue
exit

#sets up first obstacle choice
obstacle = input("""The first week of your journey having been uneventful,
you\'re searching for a spot to set up camp for the evening, when you note an
odd looking stump. Flat as a table, and set on it are three items: an unlit
torch, a cloudy black GEM, and a note. The note, neatly written, reads
"Take only one, consider well." The note is signed simply "A friend" which
do you you pick up, the TORCH or the GEM?\n""")

#Creates lists for data validation and loops for invalid data on nested choices
obstacle_list = ['torch','gem']
torch_actions = ['run','throw']
gem_actions = ['right','left']
while obstacle.lower() not in obstacle_list:
    obstacle = input("""The first week of your journey having been uneventful,
    you\'re searching for a spot to set up camp for the evening, when you note an
    odd looking stump. Flat as a table, and set on it are three items: an unlit
    torch, a cloudy black GEM, and a note. The note, neatly written, reads
    "Take only one, consider well." The note is signed simply "A friend" which
    do you you pick up, the TORCH or the GEM? Please select one of the capitolized items to pick up.\n""")
if obstacle.lower() == 'torch':
    fate_action_torch = input(""" You pick up the torch and it flares so brightly stars dance in
    your vision briefly and as they clear you hear a monsterous roar and the
    crashing of trees coming your way. Do you THROW the torch, or RUN and try
    to put it out?\n""")
    while fate_action_torch not in torch_actions:
        fate_action_torch = input(""" You pick up the torch and it flares so brightly stars dance in
        your vision briefly and as they clear you hear a monsterous roar and the
        crashing of trees coming your way. Do you THROW the torch, or RUN and try
        to put it out? Please select one of the capitolized options.\n""") 
    if fate_action_torch.lower() == 'throw':
        print("""Thinking fast you throw the torch pushed along by a Word of
        power far to your left, and watch the gleaming light fade, listening
        intently. Whatever it was the light summoned, it barrelled off after
        the torch the crashing of broken trees panctuated with the intermittent
        roar of something impressively large, and audibly angry. Breathing a
        sigh of releif you set up camp and pass a peaceful evening under the
        stars.""")
        exit
    elif fate_action_torch.lower() == 'run':
        print("""You turn and run muttering incantations to identify the Word of Power 
        that will douse the light of the torch as you go. The deep roar of whatever 
        creature was summoned and the audible protests of the trees at it's intrusion 
        following close behind you. Just as you feel the persuer closing the distance 
        you hit upon the phrase. " Escal calad!" you shout in victory and as the 
        darkness folds back in around you the cacohpony of the beast is utterly silenced.""")
        exit
else:
    fate_action_gem = input("""You pick up the gem and swirls of grey smoke envelope you for a
        moment, as the smoke clears you notice you are standing at a crossroads in
        a place you've never seen before that is not marked on your magical map.
        Do you choose RIGHT or LEFT?\n""")
    while fate_action_gem not in gem_actions:
        fate_action_gem = input("""You pick up the gem and swirls of grey smoke envelope you for a
        moment, as the smoke clears you notice you are standing at a crossroads in
        a place you've never seen before that is not marked on your magical map.
        Do you choose RIGHT or LEFT?\n""")
    if fate_action_gem.lower() == 'left':
        print("""You take the left hand path, and come to a door. Walking through the
        door you see you've been sent back to the gate of Dwarrow from whence you first set out.
        You sigh, shake your head and start off again.\n""")
        exit
    else:
        print("""You turn cautiously to the right walking for a few minutes leads you to an odd
        door. You step through it and see you been transported a week's journey closer to your goal! "A friend
        indeed, you say as you make camp for the night.\n""")
        exit


