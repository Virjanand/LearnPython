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

