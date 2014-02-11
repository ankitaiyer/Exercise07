rest_file = open("scores.txt")
rest_file_content = rest_file.readlines()
print "readlines() output:", rest_file_content
print "\n"
rest_file.close()



rest_file = open("scores.txt")
rest_file_content = rest_file.read()
print "read() output:\n", rest_file_content
print "\n"
rest_file.close()




rest_file = open("scores.txt")
rest_file_content = rest_file.readline()
print "readline() output:", rest_file_content
rest_file_content = rest_file.readline()
print "readline() output:", rest_file_content
rest_file.close()
