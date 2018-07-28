def kojo_at_cmh(name):
    """
    str -> str
    Takes a string and returns a string customized with the input string
    """

    # I wanted to use an f-string here, but I forgot how. But they're faster than the str.format method
    print("Hi {}, Kojo is at PyOhio 2018".format(name))
