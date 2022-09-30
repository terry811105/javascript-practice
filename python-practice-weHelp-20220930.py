#Q1 --------------------------------------------
def calculate(min, max, step):
    sum = 0
    for i in range(min, max+1, step):
        sum += i
    print(sum)

print("----- Q1:")
calculate(1, 3, 1)
calculate(4, 8, 2)
calculate(-1, 2, 2)

#Q2 --------------------------------------------
def avg(data):
    employees = data["employees"]
    notManager = 0
    allSalary = 0
    for onePerson in employees:
        if bool(onePerson["isManager"]) == False:
            notManager += 1
            allSalary += int(onePerson["salary"])

    print(allSalary/notManager)

print("----- Q2:")
avg({
    "employees": [
        {
            "name": "john",
            "salary": 30000,
            "isManager": False
        },
        {
            "name": "bob",
            "salary": 60000,
            "isManager": True
        },
        {
            "name": "tony",
            "salary": 50000,
            "isManager": False
        },
        {
            "name": "jenny",
            "salary": 40000,
            "isManager": False
        }
    ]
})

#Q3 --------------------------------------------
def funct(a):
    def funcInner(b, c):
        return  a+b*c
    return  funcInner

print("----- Q3:")
print(funct(2)(3, 4))
print(funct(5)(1, -5))
print(funct(-3)(2, 9))

#Q4 --------------------------------------------
def maxProduct(nums):

    max = nums[0]*nums[1]
    
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            num1 = nums[i]
            num2 = nums[j]
            if num1*num2 > max:
                max = num1*num2
    
    print(max)

print("----- Q4:")
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([10, -20, 0, -3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([5, -1, -2, 0])
maxProduct([-5, -2])

#Q5 --------------------------------------------
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]   

print("----- Q5:") 
print(twoSum([2, 11, 7, 15], 9))

#Q6 --------------------------------------------
def maxZeros(nums):
    count = 0
    max = 0
    for i in nums:
        if i == 0:
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)

print("----- Q6:") 
maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])
maxZeros([0, 0, 0, 1, 1])