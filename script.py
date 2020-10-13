from dt_classes import Daniel, all_tags
from hash import HashMap

episodes = {}

#functions
def make_episode(season, episode, jingle):
    episodes[season, episode] = Daniel(season, episode, jingle)

def retrieve_episodes(tag):
    episode_list = tags_lookup.retrieve(tag)
    for item in episode_list:
        print(item)

#episodes
make_episode(1, 1, ["When something seems bad, turn it around, and find something good", "https://www.youtube.com/watch?v=sx1RyNNVK5c"])
make_episode(1, 2, ["When we do something new, let's talk about what we'll do.", "https://youtu.be/I6wofOMbq0M?t=11"])
make_episode(1, 3, ["Grown-ups come back.", "https://www.youtube.com/watch?v=iVcFOUYIvWs"])
#tags
episodes[(1,1)].assign_tag("disappointment")
episodes[(1,2)].assign_tag("doctor visit")
episodes[(1,2)].assign_tag("new experiences")
episodes[(1,3)].assign_tag("separation anxiety")
episodes[(1,3)].assign_tag("disappointment")


tags_lookup = HashMap(1000)
for tag in all_tags:
    for key in episodes.keys():
        if tag in episodes[key].tags:
            tags_lookup.assign(tag, episodes[key])

retrieve_episodes("disappointment")
