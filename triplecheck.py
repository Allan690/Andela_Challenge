def Validator(arr):
    message ='Elements should not have a count greater than 3'
    message2 = 'List cannot be empty'
    message3 ='Elements must have a count of either 3 or 1'
    for i in set(arr):
        if arr.count(i)>3:
            return message
        elif arr.count(i)==2:
            return message3        
        elif arr.count(i)==1:
            return i*1
    if len(arr)==0:
        return message2

if __name__=='__main__':
    Validator([5, 3, 4, 3, 5, 5, 3])




