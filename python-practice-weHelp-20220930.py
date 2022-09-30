def calculate(min, max, step):
    sum = 0
    for i in range(min, max, step):
        sum += i
    print(sum)


calculate(2, 3, 4)


import json
def avg(data):
    employees = data["employees"]
    notManager = 0
    allSalary = 0
    for onePerson in employees:
        if bool(onePerson["isManager"]) == False:
            notManager += 1
            allSalary += int(onePerson["salary"])

    print(allSalary/notManager)




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

def funct(a):
    def funcInner(b, c):
        return  a+b*c
    return  funcInner

print(funct(2)(3, 4))
print(funct(5)(1, -5))