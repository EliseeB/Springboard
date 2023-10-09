from collections import Counter

"""Python serial number generator."""

call_count = Counter()

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    #Constructor. Initializes the serialGenerator
    def __init__(self, start =0):
        """Makes a generator,  starting at start"""

        self.start = self.next = start
    
    #Representation of the object as a string
    def __repr__(self):
        """Shows representation"""

        return f"< SerialGenerator start= {self.start}> next= {self.next} >"
    

    # Generate Method (generate): Generates the next serial number
    def generate(self):
        """Return next serial."""

        self.next += 1
        return self.next - 1
    
    
    #Reset the value to the original value
    def reset(self):
        """Reset number to original start."""
        
        self.next = self.start

   