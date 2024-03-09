a = 33
b = 32

if(a>32 and b>32):
    print("Both 'a' and 'b' are above freezing.")
elif(a<=32 and b<=32):
    print("Both 'a' and 'b' are freezing.")
elif(a<=32 or b<=32):
    print("Only one of 'a' and 'b' are freezing.")