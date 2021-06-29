def greet(*names):
    """This function greets all the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


a = "This is just to check accessibility from some other file on import"

"""
Now since this is inside main only this wont be called when 
imported from any other file
"""
if __name__ == "__main__":
    greet("Monica", "Luke", "Steve", "John")
