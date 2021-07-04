list1=["cycle","bike","car","train","jet"]
# i=1
# for item in list1:
#     if i%2 is not 0:
#         print("hey, plzz buy ",item)
#     i=i+1


#same thing can be done by enumerator function

i=0
for index,item in enumerate(list1):
    if i%2==0:
        print("hey , plzz buy the ",item)
    i=i+1    