import tkinter as tk  # jo kisi ko nahi aata...🤣
from tkinter import messagebox #tried something let's see if it works


class NPC:                  # Base Class for angels and demons
    side=0

    def __init__(self):
        self.name = name
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

# Main Game class to manage the game logic and GUI
class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Angels and Demons Game")
        
        self.boat = Boat()
        self.angels = [Angel(f"Angel {i+1}") for i in range(3)]
        self.demons = [Demon(f"Demon {i+1}") for i in range(3)]
        
        self.create_widgets()

    def create_widgets(self):
        # Labels for sides and boat
        self.left_side_label = tk.Label(self.root, text="Left Side")
        self.left_side_label.grid(row=0, column=0)

        self.right_side_label = tk.Label(self.root, text="Right Side")
        self.right_side_label.grid(row=0, column=2)
        
        self.boat_label = tk.Label(self.root, text="Boat")
        self.boat_label.grid(row=0, column=1)
        
        self.update_view()

        # Sail button to move the boat
        self.sail_button = tk.Button(self.root, text="Sail", command=self.sail_boat)
        self.sail_button.grid(row=3, column=1)

    def update_view(self):
        self.clear_view()
        
        # Display NPCs on the left side
        for i, angel in enumerate([npc for npc in self.angels if npc.side == 0]):
            tk.Button(self.root, text=angel.name, command=lambda a=angel: self.load_unload_npc(a)).grid(row=1, column=0, sticky='W')
        
        for i, demon in enumerate([npc for npc in self.demons if npc.side == 0]):
            tk.Button(self.root, text=demon.name, command=lambda d=demon: self.load_unload_npc(d)).grid(row=2, column=0, sticky='W')

        # Display NPCs on the right side
        for i, angel in enumerate([npc for npc in self.angels if npc.side == 1]):
            tk.Button(self.root, text=angel.name, command=lambda a=angel: self.load_unload_npc(a)).grid(row=1, column=2, sticky='E')
        
        for i, demon in enumerate([npc for npc in self.demons if npc.side == 1]):
            tk.Button(self.root, text=demon.name, command=lambda d=demon: self.load_unload_npc(d)).grid(row=2, column=2, sticky='E')

        # Display NPCs on the boat
        if self.boat.left:
            tk.Button(self.root, text=self.boat.left.name, command=lambda: self.unload_npc(self.boat.left)).grid(row=1, column=1)
        
        if self.boat.right:
            tk.Button(self.root, text=self.boat.right.name, command=lambda: self.unload_npc(self.boat.right)).grid(row=2, column=1)

    def clear_view(self):
        # Clear previous widgets from the grid
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.grid_forget()

    def load_unload_npc(self, npc):
        # Load or unload NPCs based on their current position
        if npc.side == self.boat.side:
            if npc == self.boat.left or npc == self.boat.right:
                self.boat.unload_NPC(npc)
            else:
                self.boat.load_NPC(npc)
            self.update_view()

    def unload_npc(self, npc):
        # Unload the NPC from the boat
        self.boat.unload_NPC(npc)
        self.update_view()

    def sail_boat(self):
        # Sail the boat to the other side
        self.boat.sail()
        self.update_view()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
