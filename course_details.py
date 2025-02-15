import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))
#0 means inserted at index 0 try to collapse the absolute path
#the absolute path in JOINED and python gets to know which file is available where 

from payment import payment_details


def course():
    print("This is my course details")

payment_details.payment() #<filename>.<methodname>
