sub1 = int(input ("Enter first subject marks\n"))
sub2 = int(input ("Enter first subject marks\n"))
sub3 = int(input ("Enter first subject marks\n"))

if (sub1<33 or sub2<33 or sub3) :
    print("You are fail because you have less than 33% in one of the subjects")
elif (sub1+sub2+sub3)/3 < 40 :
    print (" Your are fail due to total percentage less than 40")
else : 
    print ("Congratulation ! You passed the exam")    