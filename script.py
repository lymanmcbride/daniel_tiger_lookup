from dt_classes import Daniel, all_tags
from hash import HashMap



#Program Functions:
def main():
    greeting()
    lookup()
    goodbye()

def greeting():
    print("Hello! Welcome to the Daniel Tiger lookup!")

def goodbye():
    print("Enjoy making your child happy!")

def lookup():
    struggle = input("Type in what your child is struggling with. If you would like to see a list of the options in our system, type 'options.'\n").lower()
    if struggle == "options":
        print("\n")
        for tag in all_tags:
            print (tag)
        lookup()
    elif struggle in all_tags:
        retrieve_episodes(struggle)
        lookup_again()
    else:
        print("Sorry, that isn't in our list of options.")
        lookup_again()

def lookup_again():
    again = input("Do you want to look up another episode? y/n\n").lower()
    if again == "y":
        lookup()
    elif again == "n":
        return
    else:
        print("That wasn't a valid input. Please type either the letter 'Y' or 'N'.")
        lookup_again()

#functions
def make_episode(season, episode, real_se, name, jingle):
    episodes[season, episode] = Daniel(season, episode, real_se, name, jingle)

def retrieve_episodes(tag):
    episode_list = tags_lookup.retrieve(tag)
    for item in episode_list:
        print(item)

#episodes
episodes = {}
make_episode(1, 1, (1, 1), 'Daniel\'s Birthday / Daniel\'s Picnic', ["When something seems bad, turn it around, and find something good", "https://www.youtube.com/watch?v=sx1RyNNVK5c"])
make_episode(1, 2, (1, 2), 'Daniel Visits School / Daniel Visits the Doctor', ["When we do something new, let's talk about what we'll do.", "https://youtu.be/I6wofOMbq0M?t=11"])
make_episode(1, 3, (1, 3), 'Daniel\'s Babysitter / Daniel Goes to School', ["Grown-ups come back.", "https://www.youtube.com/watch?v=iVcFOUYIvWs"])
make_episode(1, 4, (1, 4), 'Daniel Gets Mad / Katerina Gets Mad', ["When you feel so mad that you want to roar, take a deep breath, and count to four.", "https://www.youtube.com/watch?v=AD4RGoiTyl4"])
make_episode(1, 5, (1, 5), 'Prince Wednesday Finds a Way to Play / Finding a Way to Play on Backwards Day', ["Find a way to play together.", "https://youtu.be/EU2MVndXKsw?t=16"])
make_episode(1, 6, (1, 6), 'Daniel and Miss Elaina Play Rocketship / Daniel Plays at the Castle', ["A friend just wants to play with you.", "https://youtu.be/izMLXGl4YhI?t=32"])
make_episode(1, 7, (1, 7), 'Friends Help Each Other / Daniel Helps O Tell a Story',["Friends help each other. Yes they do. It's true.", "https://youtu.be/aWLnsXp0dMo?t=23"])
make_episode(1, 8, (1, 8), 'Something Special for Dad / I Love You, Mom', ['Making something is one way to say, "I love you."', "https://youtu.be/exT_ASwA5u8?t=20"])
make_episode(1, 9, (1, 9), 'A Trip to the Enchanted Garden / A Trip to the Crayon Factory', ["You've got to look a little closer to find out what you want to know.", "https://www.youtube.com/watch?v=CGbn5y2K9JM"])
make_episode(1, 10, (1, 10), 'Daniel Shares his Tigertastic Car / Katerina Shares her Tutu', ["You can take a turn, and then I'll get it back.", "https://youtu.be/LkfqHp3hATI?t=9"])
#tags
episodes[(1,1)].assign_tag("disappointment")
episodes[(1,2)].assign_tag("doctor visit")
episodes[(1,2)].assign_tag("new experiences")
episodes[(1,3)].assign_tag("separation")
episodes[(1,4)].assign_tag("mad feelings")
episodes[(1,5)].assign_tag("playing together")
episodes[(1,6)].assign_tag("friendship")
episodes[(1,7)].assign_tag("friendship")
episodes[(1,7)].assign_tag("help")
episodes[(1,7)].assign_tag("serving")
episodes[(1,8)].assign_tag("expressing love")
episodes[(1,8)].assign_tag("giving to loved ones")
episodes[(1,9)].assign_tag("explore")
episodes[(1,9)].assign_tag("keep looking")
episodes[(1,10)].assign_tag("sharing")
episodes[(1,10)].assign_tag("taking turns")





tags_lookup = HashMap(150)
for tag in all_tags:
    for key in episodes.keys():
        if tag in episodes[key].tags:
            tags_lookup.assign(tag, episodes[key])

main()
#for item in tags_lookup.array:
#    if item != None:
#        node = item.get_head_node()
#        while node.get_next_node():
#            print(node.get_value()[1])
#            node = node.get_next_node()
