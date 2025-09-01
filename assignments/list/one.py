#mutable

student_scores = []
student_scores.extend([85,90,78,92,88]) # appending values
print("list after appending values is :",student_scores)
student_scores.insert(2,80) # inserting a certain value at certain index
print("list after inserting 80 at index 2 is :",student_scores)
student_scores.remove(92) # removing an element
print("list after removing 92  is :",student_scores)
student_scores.sort() # sorting the list
print("list  after sortingis :",student_scores)
student_scores.reverse() # reversing the list
print("list after reversing is :",student_scores)
print("Maxm score is :",max(student_scores)) # maxm element of a list
print("Minm score is :",min(student_scores)) # minm element of a list
# to check whether 90 is there in the list or not
flag=False
for i in student_scores:
    if i==90:
        flag=True
        break
if flag:
    print("90 is in the list")
else:
    print("90 is absent from the list")
print("Total Number of scores ", len(student_scores)) # printing total number of scores
# slice and print the first 3 elements of the list
print("first 3 scores :")
for i in range(3):
    print(student_scores[i] )
print("last element of the list is :",student_scores[-1]) # printing the last element
student_scores[2] = 95 # replacing 2nd index
print("after replacing 95 at index 2 new list is ",student_scores)
copied_student_scores = student_scores.copy() #copying the list into another 
print("copied list ",copied_student_scores)