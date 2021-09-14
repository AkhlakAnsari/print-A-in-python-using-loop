#PRINT "A" LETTER IN PYTHON USING LOOP
string= " "
for row in range(7):
    for column in range(5):
        if (column==0 or column==4) or ((row==0 or row==3) and (column>0 and column<4) ):
            string= string+"*"


        else:
            string=string+" "
    string=string+"\n"
print(string)
#THANKS akhlakansari94@gmail.com