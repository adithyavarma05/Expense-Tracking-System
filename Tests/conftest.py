import os
import sys

# Creating the path route for backend for db_helper
path_route=os.path.join(os.path.dirname(__file__),"..")

#appending our path route into our system
sys.path.append(path_route)