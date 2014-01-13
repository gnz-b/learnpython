from sys import argv

script, filename = argv

item = open(filename,"r+");
print item.read()