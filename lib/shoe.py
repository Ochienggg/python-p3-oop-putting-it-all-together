#!/usr/bin/env python3

# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = None  # Optional: initialize condition in __init__

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")









    
        








        
   








