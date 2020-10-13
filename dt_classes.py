all_tags = []
class Daniel:
    def __init__(self, season, episode, jingle):
        self.season = season
        self.episode = episode
        self.jingle = jingle
        self.tags = []

    def __repr__(self):
        return "Daniel Tiger season {} episode {}".format(self.season, self.episode)

    def assign_tag(self, tag):
        self.tags.append(tag)
        if tag not in all_tags:
            all_tags.append(tag)
