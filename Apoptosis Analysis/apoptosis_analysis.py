# Import the required libraries .
from random import randint
# Initialise folder variables . Here folder is an arraylist containing
# the names of the three kinds of cells used for the simulation.

folders =["CancerCell_Type1","CancerCell_Type2","HealthyCells"]
# loop_var runs over the 3 folders .
for loop_var in range(3):
    celldeath_array = []
	# List to store the no . of cells dead .
    for outer in range(16):
	# Iterate 16 times.
	    for i in range(16):
		# Iterate over 16 randomly picked files .
		    apoptosis=0
		    survived=0
		    for j in range (16):
			    filenum=randint (1,64)
			    with open (folders[loop_var]+"/output"+str(filenum )) as g:
				    lines=g.readlines ()
				    a=lines[-1].split(" ")
				    # Take last line ’ s 6 th column .
				    if(int(a[5])>50):
					# We take 50 as the caspase3 threshold .
					    apoptosis = apoptosis +1	
		    celldeath_array.append(apoptosis )
    print ("Total cell deaths in "+ folders[loop_var]+":")
    print (celldeath_array)
	# Finally print out the array for a folder .
    print ("\n")


