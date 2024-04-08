"""
This is an example script to test auto doc generation
"""

def do_something(text):
    """
    This function just prints a sentence to test that things are working.

    :param text: any text you want to print
    :type text: str
    :return: text
    :rtype: list[str]
    """

    fullstring = 'Here is some text: ' + text
    print(fullstring)

    return fullstring



if __name__ == "__main__":

    printout = do_something('text example!!!')

    print(printout)    # yes I know this will print twice
