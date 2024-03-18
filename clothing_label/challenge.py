"""
Suppose we’re writing software for a clothing manufacturer. 
Our code accepts an array of newly produced clothing items (stored as strings),
and creates text for every possible label we'll need.
Specifically, our labels should contain the item name plus its size, ranging
from 1 to 5. 
For example, if we have the array, ["Purple Shirt", "Green Shirt"], we
want to produce label text for those shirts like this:

[
"Purple Shirt Size: 1",
"Purple Shirt Size: 2",
"Purple Shirt Size: 3",
"Purple Shirt Size: 4",
"Purple Shirt Size: 5",
"Green Shirt Size: 1",
"Green Shirt Size: 2",
"Green Shirt Size: 3",
"Green Shirt Size: 4",
"Green Shirt Size: 5"
]
"""


def make_inventory(shirts):
    inventory = []
    for shirt in shirts:
        for i in range(1, 6):
            inventory.append(f"{shirt} Size: {i}")
    return inventory
