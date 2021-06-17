## setup path
import sys
import os
basePath = os.path.dirname(os.path.abspath(__file__)) + "\.."
sys.path.append(basePath)
## end setup path


import myMod.greeting as greeting
greeting.greet_in_english()