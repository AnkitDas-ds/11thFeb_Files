import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))



# from course import course_details

def payment():
    print("This is my payment details")
 
# course_details.course()
# if we import both modules in both the files 
# then there will be circular import 
# so it is better that we import only only file
# at a time  