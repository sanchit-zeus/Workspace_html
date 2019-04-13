#problem 1
arraycheck1=[1,1,2,3,1]
arraycheck2=[1,1,2,4,1]
arraycheck3=[1,1,2,1,2,3]

def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+2]==2 and nums[i+2]==3:
            return True
    return False


#Problem 2

def stringBits(str):
    result=""

    for i in range(len(mystring)):
        if i%2==0:
            result=result+mystring[i]
    return result


#problem 3

a=a.lower()
b=b.lower()

#return(b.endswith(a)or a.endswith(b))
return a[-(len(b)):]==b or a==b[-len(a):]


#problem 4
result=" "
for char in mystring:
    result += char*2
return result


#problem 5
def no_teen_sum(a,b,c):
    return fix_teen(a)+fix_teen(b)+fix_teen(c)

def fix_teen(n):
    if n[13,14,17,18,19]:
        return 0
    return n

#problem 6

count =0

for element in nums:
    if element%2==0:
        count +=1
    return count    
