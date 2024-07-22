import tkinter as tk        # jo kisi ko nahi aata...🤣


class NPC:                  # Base Class for angels and demons
    side=0

    def __init__(self):
        self.side=0         # 0 represents left and 1 represents right. The initial position is left for any race 

class Angel(NPC):           # TODO: implement Angel
    pass

class Demon(NPC):           # TODO: implement Demon
    pass

class Boat:
    side=0
    left=None
    right=None

    def __init__(self):
        self.side=0         # 0 represents left and 1 represents right. The initial position for the boat is left
        self.left : NPC =None     # representing left seat , initially empty
        self.right : NPC =None    # representing right seat, initially empty

    def sail(self): # function to make the boat switch sides
        # if the boat is empty, don't sail
        if self.left==None and self.right==None:
            print("There is no one on the boat to ride it")
            return
        # otherwise just change the side
        self.side= 1-self.side
        self.left.side = 1 - self.left.side
        # ignore if the second seat is empty
        if self.right != "NULL":
            self.right.side = 1 - self.right.side

    def load_NPC(self, selectedNPC : NPC):
        if self.left != None and self.right != None:
            print("The boat is at full capacity")
            return
        elif self.left != "NULL":
            self.right = selectedNPC
        else:
            self.left = selectedNPC

    def unload_NPC(self, selectedNPC : NPC):
        if self.left == selectedNPC:
            self.left = self.right
            self.right = None
        elif self.right == selectedNPC:
            self.right = None
        else:
            print("Selected person not on board")
