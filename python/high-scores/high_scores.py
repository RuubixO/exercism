# use heapq module to make clean code for sorts of top score(s)
import heapq


class HighScores(object):

    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        # Using reverse indexing, get the last item in any given list.
        return self.scores[-1]

    def personal_best(self):
        # returns a list with one item == highest int in self.scores.
        # then, pulls out item using its index and returns the int by itself.
        return heapq.nlargest(1, self.scores)[0]

    def personal_top_three(self):
        # return list with the three highest integers of self.scores.
        return heapq.nlargest(3, self.scores)
