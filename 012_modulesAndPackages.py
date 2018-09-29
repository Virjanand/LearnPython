# Modules and packages
# Module has specific functionality and is in separate file
# Write module for ping pong game
# game.py will implement the game and will 
# use function draw_game from draw.py or draw module
# import modules with import command

# game module imports the load module, now it can use
# functions from that module.
# import draw looks first in same directory, if not found
# it looks in built-in modules.

# Importing module objects to current namespace
# use draw_game directly
# from draw import draw_game
# instead of draw.draw_game(result)
# can use draw_game(result) immediately
# import all with from draw import *

# Import under custom namespace
# import draw_visual as draw

# Module initialization
# First time a module is loaded it initializes by executing
# the code in the module once. It will not be imported twice.
# This means local variables in module act as singletons.

# Extending module load path
# Look for modules
# Use environment variable PYTHONPATH
# PYTHONPATH=/foo python game.py
# will execute game.py and enable script to load modules
# from the foo directory as well as local directory.
# Use sys.path.append function before import command
# sys.path.append("/foo")
# This adds foo directory to list of paths to look for
# modules.

# Explore built-in modules
# use dir and help functions:
# import urllib
# dir(urllib) displays all functions in module
# help(urllib.urlopen) gives information on function

# Writing packages
# Packages are namespaces which contain multiple packages and modules
# Each package is a directory which must contain file __init__.py
# import bar module from foo directory: import foo.bar or from foo import bar
# usage for import foo.bar always include foo., else bar in current namespace
# In __init__.py you can specify which modules to export as API
# by overriding the __all__ variable in __init__.py: __all__ = ["bar"]
# this exposes only bar module.

# Exercise: print alphabetically sorted list of all functions in re module
# which contain the word find.
import re

find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))