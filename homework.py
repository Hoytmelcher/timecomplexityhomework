# Remove First and Last Character  O(n)+O(n)=O(n)

def remove_char(s):
    lis = [] #O(1)
    for l in s:  #O(n)
        lis.append(l) #O(1)
    lis.pop(0) #O(1)
    lis.pop(-1) #O(1)
    return "".join(lis) #O(n)



# Number Of Occurrences: O(n)

def number_of_occurrences(element, sample):
        return sample.count(element) #O(n)
    



# Stop gninnipS My sdroW! O(n) * O(n) = O(n^2)

def spin_words(sentence):
    new = sentence.split(' ') #O(n)
    list = [] #O(1)
    for word in new: #O(n)
        if len(word) < 5: 
            list.append(word) #O(1)
        else:
            list.append(word[::-1]) #O(n) 
            
    return ' '.join(list) #O(n)
