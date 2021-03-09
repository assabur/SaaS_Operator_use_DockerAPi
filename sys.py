import os
import sys
#understand how can i retrieve the differents argument pass on comman line us sys.argv
print("This is the name of the program:", sys.argv[0])
print("Argument List:", str(sys.argv))
print("This is the name of the program:"+sys.argv[1])
print("This is the name of the program:"+sys.argv[2])
#fin the location of my docker installation path
for d in sys.path:
    if os.path.exists(os.path.join(d, "docker")):
        print("docker is at %r" % d)

#operateur lien github name



#try
