
rest_file = open("scores.txt")
rest_file_content = rest_file.readlines()

rest_dict = {}
for line in rest_file_content:
    rest_key = line.strip().split(":")[0]
    rest_value = line.strip().split(":")[1]
    rest_dict[rest_key] = rest_value
    
for item in sorted(rest_dict):
    print "Restaurant '%s' is rated at %s." % (item , rest_dict[item])

