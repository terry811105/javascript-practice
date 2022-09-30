console.log("hello");

console.log("1");

function twoSum(nums, target){
    let index = [];
    for ( let i = 0; i < nums.length-1; i++){
        let num = nums[i];
        for ( let j = i+1; j < nums.length; j++){
            if (num + nums[j] == target) {
                index.push(i);
                index.push(j);

            }
        }
    }
    console.log(index)
}

twoSum([7, 28, 1, 9], 16);

function avg(data){

    let employees = data["employees"];
    let count = 0;
    let total = 0;

    data.employees.forEach((onePerson) => {
        if (!onePerson.isManager) {
            
        }
    });

    for (let i = 0; i < employees.length; i++){
        let isManager = employees[i]["isManager"];
        if (!isManager) {
            count++;
            total += employees[i]["salary"];
        }
    }

    let averageSalary = total/count

    console.log(averageSalary);

}

avg({
    "employees": [
        {
            "name": "john",
            "salary": 30000,
            "isManager": false
        },
        {
            "name": "bob",
            "salary": 60000,
            "isManager": true
        },
        {
            "name": "tony",
            "salary": 50000,
            "isManager": false
        },
        {
            "name": "jenny",
            "salary": 40000,
            "isManager": false
        }
    ]
});

// 這個function名字叫做func, 他吃的參數他自己把它叫做a
// ps: a, b, c都只活在他們後面的大括號裡
function func(a) {
    // func會回傳下面這個func2的回傳結果, 這個func2吃的參數取名為b, c
    return function func2 (b, c) {
        // 回傳這個結果
        return(a+b*c);
    }
}

// 所以這個func會丟一個東西出來, 外面要有地方去放這個東西
let a = func(4)(5, 2);
console.log(a);

let b = func(5)(-1, 5);
console.log(b);


function funcTest(a) {
    
    function func2 (b, c) {
        // 在這邊印出結果
        console.log(a+b*c);
    }
    // 但是外面的func似乎一定會回傳一個結果
    return func2;
}

// 因為這個funcTest是在裡面的func2就印東西了, 所以就沒有回傳東西出來了 
funcTest(4)(5, 2);
funcTest(5)(-1, 5);
