#from sys import argv
#script, filename = argv

rest_file = open("scores.txt")
rest_file_content = rest_file.read()


rest_file_content_list = rest_file_content.split("\n")


for item in sorted(rest_file_content_list):
    print "Restaurant '%s' is rated at %s." % (item.split(":")[0], item.split(":")[1])

