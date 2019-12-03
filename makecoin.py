class Pound:
    def __init__(self,rare=False):
        self.rare=rare
        if self.rare:
            self.value=1.25
        else:
            self.value=1.00
        self.color="gold"
        self.diameter=22.5#mm
        self.num_edges=1
        self.thickness=3.15#mm
        self.heads=True
    def rust(self):
        self.color="greenish"
    def clean(self):    
        self.color="gold"
    def flip(self):
        head_option=[True,False]
        choice=random.choice(head_option)
        self.head=choice
        
    def __del__(self):
        print("Coin spent!")
