# Python program of Binary Search.
# First we will take input of the list from the user.
# Note List contains only in ascending order.
print("list must be in ascendng order") 
lists=list(map(int,input("Enter the list: ").split())) 

# And we will take input of Element(Element which was to search ):
Element=eval(input("Enter the number which you want to search: ")) 
lower=0 
high=0 
length_Of_List=len(lists)-1 
while lower<=length_Of_List: 
    middle=(lower+length_Of_List)//2 
    if lists[middle]==Element:     
        high=1 
        print("Element found in the list") 
        break 
    elif lists[middle]>Element : 
        length_Of_List=middle-1 
    else: 
        lower=middle+1 
if high==0: 
    print("Element not found")

