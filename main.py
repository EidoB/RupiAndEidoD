import random
import funcs
 
#TO DO:
#Create a file once the code is runnning, and re-creating it every run.

tf = open('tresurefile.txt','w')
for i in range(10):
    random_number=random.randint(1,20)
    tf.write(str(i) * random_number)

tf.write('TREASURE')    

for i in range(9,0,-1):
    random_number=random.randint(1,20)
    tf.write(str(i) * random_number)

# funcs.create_treasue_file()

