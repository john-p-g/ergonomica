# pylint: disable=W0603
"""
[verbs.py]
Contains all the native commands for ergonomica
"""

import os
import fnmatch

run = True
directory = "/"

def Quit(*args, **kwargs):
    """What do you think?"""
    global run
    run = False

def Help(*args):
    """Display all commands"""
    if len(args[0]) == 0:
        print "test"
    else:
        print args

def cd(*args, **kwargs):
    directory += args[0]
    return directory

def find(args, kwargs):
    pattern = kwargs["name"]
    path = args[0]
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def echo(args, kwargs):
    return args[0]

def clear(args, kwargs):
    """Clears the screen"""
    os.system('clear')

verbs = {
         "quit": Quit,
         "exit": Quit,

         "help": Help,

         "cd":cd,

         "echo":echo,

         "find": find,
         "clear":clear,
        }
