"""
Routines for formatting reports.
"""

from __future__ import print_function
import sys
from textwrap import wrap
# ensures that input is working across Python 2.7 and 3+
try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

NORMAL = "\033[0m"
PURPLE = "\033[35m"
RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
CYAN = "\033[36m"
UNDERLINE = "\033[4m"

def warning(message, display=True):
    """Write the provided message, with the text 'warning: ' in front of it, to
    stderr.

    Parameters
    ----------
    message : str
        This is the string you want to print.

    display : bool
        Write this message to stderr, if display is True.

    Returns
    -------
    warning_message : str
        The formatted string which is also printed to stderr.
    """
    warning_message = "{}warning: {}{}".format(PURPLE, NORMAL, message)
    if display:
        print(warning_message, file=sys.stderr)
    return warning_message

def error(message, display=True):
    """Write the provided message, with the text 'error: ', in front of it to
    stderr.

    Parameters
    ----------
    message : str
        This is the string you want to print.

    display : bool
        Write this message to stderr, if display is True.

    Returns
    -------
    error_message : str
        The formatted string which is also printed to stderr.
    """
    error_message = "{}error: {}{}".format(RED, NORMAL, message)
    if display:
        print(error_message, file=sys.stderr)
    return error_message

def tip(message, display=True):
    """Write the provided message, with the text 'tip: ' in front of it, to
    stderr.

    Parameters
    ----------
    message : str
        This is the string you want to print.

    display : bool
        Write this message to stderr, if display is True.

    Returns
    -------
    warning_message : str
        The formatted string which is also printed to stderr.
    """
    tip_message = "{}tip: {}{}".format(GREEN, NORMAL, message)
    if display:
        print(tip_message, file=sys.stderr)
    return tip_message


def yes_or_no(question):
    """Takes a question as an input and prompts the user for a yes or no. Returns
    True if the answer is yes and False if the answer is no.

    Parameters
    ----------
    question : str
        This text is displayed, before asking for a yes or a no.

    Returns
    -------
    True or False
        True if answer is 'y', False if answer is 'n'.
    """
    # make input work the same way in both Python 2 and 3
    answer = input(question + " (y/n): ".lower().rstrip())
    while not (answer == "y" or answer == "n"):
        answer = input(question + " (y/n): ".lower().rstrip())
    if answer[0] == "y":
        return True
    elif answer[0] == "n":
        return False

def progress_bar(message, replace=True, display=True):
    """Takes a text string as an input and prints it to standard error, with
    the text '==>' prepended. Only returns the message itself, if the boolean
    display is set to False (DEFAULT: True). By default, the last line is
    replaced as this function is intended to be used to display a continues
    progress. If you do not wish to overwrite the last line, then set replace
    to False.

    Parameters
    ----------
    message : str
        This is the string you want to print.

    replace : bool
        Overwrite the last line as in a progress bar.

    display : bool
        Write this message to stderr, if display is True.

    Returns
    -------
    progress : str
        Your message with the text '==>' prepended.
    """
    # progress = "{}==> {}{}".format(BLUE, NORMAL, message)
    progress = "{}> {}{}".format(GREEN, NORMAL, message)
    if display and replace:
        sys.stdout.flush()
        print(progress, file=sys.stderr, end="\r")
    elif display:
        print(progress, file=sys.stderr)
    return progress

def print_path(path, display=True):
    """Takes the path to a file as an input and prints the given path in blue.

    Parameters
    ----------
    path : str
      The path you wish to colorize.

    display : bool
      Print the results to stderr if this variable is True. Defaults to True.

    Returns
    -------
    path_in_blue : str
      The provided path in blue.
    """
    path_in_blue = ("{}{}{}".format(BLUE, path, NORMAL))
    if display:
        print(path_in_blue, file=sys.stderr)
    return path_in_blue

def underline(text):
    """Returns the provided text with an underline.

    Parameters
    ----------
    text : str
        The text you wish to underline.

    Returns
    -------
    underlined_text : str
        The provided text, underlined.
    """
    underlined_text = ("{}{}{}".format(UNDERLINE, text, NORMAL))
    return underlined_text

def display_otus(otus):
    """Takes a list of OTUs as an input and returns the OTUs as a string, where
    each OTU, except for the last OTU, is separated by a comma. OTUs are also
    displayed in the color red.

    Parameters
    ----------
    otus : list
      A list of OTUs.

    Returns
    -------
    formatted_otus : str
      A list of the OTUs as a text string.
    """
    formatted_otus = ", ".join(
        ["{}{}{}".format(RED, otu, NORMAL) for otu in otus])
    formatted_otus = "\n    ".join(wrap(formatted_otus, 160))
    return "    " + formatted_otus
