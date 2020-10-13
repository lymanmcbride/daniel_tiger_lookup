from hash import HashMap
episodes = {}
class Daniel:
    def __init__(self, season, episode, jingle):
        self.season = season
        self.episode = episode
        self.jingle = jingle
        self.tags = []

    def __repr__(self):
        return "Daniel Tiger season {} episode {}. Its tags are {}.".format(self.season, self.episode, self.tags)

    def assign_tag(self, tag):
        self.tags.append(tag)
