
# Mutable default parameter bug
def add_item_buggy(item, order=[]):
    order.append(item)
    return order


# Corrected function
def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


print("Buggy Function:")
print(add_item_buggy("Tea"), add_item_buggy("Vada"))

print("\nCorrected Function:")
print(add_item("Tea"), add_item("Vada"))

print("\nDefault Values:")
print(add_item_buggy.__defaults__)


# Positional, keyword and default parameters
def customer(name, item="Coffee"):
    print(name, "ordered", item)


print("\nParameter Types:")
customer("Ravi")
customer(name="Priya", item="Tea")


# Returning multiple values
def calculate(price):
    gst = price * 0.05
    total = price + gst
    return total, gst


total, gst = calculate(100)
print("\nTotal:", total)
print("GST:", gst)


# Local and global scope
x = 10

def scope_example():
    y = 20
    print("Local variable:", y)
    print("Global variable:", x)


scope_example()


# Nonlocal scope
def outer():
    value = 10

    def inner():
        nonlocal value
        value = 20

    inner()
    print("Nonlocal variable:", value)


outer()
