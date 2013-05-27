
import string

class NewsStory(object):
    def __init__(self,guid, title, subject, summary, link):
        self.guid=guid
        self.title=title
        self.subject=subject
        self.summary=summary
        self.link=link

    def getGuid(self):
        return self.guid
    def getTitle(self):
        return self.title
    def getSubject(self):
        return self.subject
    def getSummary(self):
        return self.summary
    def getLink(self):
        return self.link


class Trigger(object):

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word=word
    def isWordIn(self,text):
        word=self.word
        text = text.lower()
        word=word.lower()
        for c in string.punctuation:
            text=text.replace(c,' ')
        return word in text.split(' ')


class TitleTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getTitle())
class SubjectTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSubject())
class SummaryTrigger(WordTrigger):
    def evaluate(self,story):
        return self.isWordIn(story.getSummary())


class NotTrigger(Trigger):
    def __init__(self, trig):
        self.trig=trig
    def evaluate(self,text):
        return not self.trig.evaluate(text)


class AndTrigger(Trigger):
    def __init__(self, trig1,trig2):
        self.trig1=trig1
        self.trig2=trig2
    def evaluate(self,text):
        return self.trig1.evaluate(text) and self.trig2.evaluate(text)

class OrTrigger(Trigger):
    def __init__(self, trig1,trig2):
        self.trig1=trig1
        self.trig2=trig2
    def evaluate(self,text):
        return self.trig1.evaluate(text) or self.trig2.evaluate(text)

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase=phrase
    def evaluate(self,story):
        a=self.phrase in story.getGuid()
        a=self.phrase in story.getTitle() or a
        a=self.phrase in story.getSubject() or a
        a=self.phrase in story.getSummary() or a
        a=self.phrase in story.getLink() or a

        return a
def filterStories(stories, triggerlist):
    filteredStories=[]
    for story in stories:
        for tr in triggerlist:
            if tr.evaluate(story):
                filteredStories.append(story)
                break
    return filteredStories



















