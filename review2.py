# Declare variables up top
age = 100

# This is a comment
# if blocks
#if age < 18:
    #print("not an adult")
   
#if age < 25:
    #print("You cant rent a car")

#elif age < 35:
    #print("Cant run for president")

#else:
    #if age >= 100:
        #print("wow congrats")
i = 0
total = 0






while i <= 1000:
    # This line
    total += i
    i += 1
    
#print(total)

nums = [2,5,24,776,234,65,23]
j = 0
total = 0
while j < len(nums):
    total += nums[j]
    j += 1
print ("avg:" + str(total / len(nums)))
