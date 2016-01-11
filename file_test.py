# argv makes a list from the command line containing script name and anything following as a list.
# # of arguments has to match # of variable names you assign to argv
# python file_test.py test.txt test2.txt will not work
# argv = ['file_test.py', 'test.txt']
# script_name, file_name = argv

from sys import argv
def file_test():
    
    script_name, file_name = argv

    print "Hi"
    print "This is your script filename:", script_name
    print "This is your file name:", file_name
    print len(argv)



file_test() 

