#!/usr/bin/env python3
import mps_youtube as my
import actions.action

class Playmusic(actions.action.Action):
    def __init__(self):
        self.items = {"play" : 10, "music" : 5, "youtube" : 1}
        self.base_url = "https://www.youtube.com/watch?v="

    def getWords(self):
        return self.items.keys()

    def getPoints(self):
        return self.items.values()

    def doIt(self,tokens):
        print("Playing... ")
        my.commands.search.search(" ".join(tokens))
        video = my.g.model[0]
        my.commands.play.play_url(self.base_url + video.ytid, 0 )
