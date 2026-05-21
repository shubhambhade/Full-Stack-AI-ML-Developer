console.log("1) Airthmetic Operators : ");
console.log(10 + 5);
console.log(10 - 5);
console.log(10 * 5);
console.log(10 / 5);
console.log(10 % 5);
console.log(10 ** 2);

//On a shopping website, calculate the total cost of a product when given the price per item (price = 150) and the quantity (quantity = 3).Also, calculate a 10% discount on the total cost and display the discounted price.

let pricePerItem = 150;
let quantity = 3;

let totalCost = pricePerItem * quantity;
let discount = totalCost * 0.1;
let discountedPrice = totalCost - discount;
console.log("Total Price : ", totalCost);
console.log("Discount : ", discount);
console.log("After discount final amount : ", discountedPrice);

console.log("2) Assignment Operators : ");
let number = 5;
console.log(number);
number += 5;
console.log(number);
number -= 2;
console.log(number);
number *= 3;
console.log(number);
number /= 2;
console.log(number);
number %= 3;
console.log(number);
number += 2;
console.log(number ** 2);

console.log("3) comparision Operators : ");
console.log(5 == "5"); // check only values
console.log(5 === "5"); // check datatype and values
console.log(5 > 3);
console.log(5 < 3);
console.log(5 <= 5);
console.log(5 >= 5);
console.log(5 != "5");
console.log(5 !== "5");

console.log("4) Logical Operators : ");
console.log(true && true);
console.log(true || false);
console.log(!true);

console.log("Increment and Decrement Operators : ");
let num = 4;
console.log(num++);
console.log(++num);
console.log(num--);
console.log(--num);

console.log("Ternary Operator : ");
let age = 18;
let result = age >= 18 ? "eligible for driving" : "not eligible for driving";
console.log(result);

//On a booking website, check if the user's age is valid for booking:Age should be at least 18.Write a condition to check and display a message: "Eligible for booking" if the user is 18 or older. "Not eligible for booking" otherwise.

let userAge = 19;
let eligibilityCheck =
  userAge >= 18 ? "Eligible for booking" : "Not eligible for booking";
console.log(eligibilityCheck);

//On a login page, verify the user's credentials: Check if username is not empty AND password is not empty (&& operator).If either is empty, display an error message: "Both fields are required."

let userName = "";
let password = "";

let message =
userName && password ? "Login Successful" : "Both fields are required";
console.log(message);

// find the largest number from given 3 numbers.
let num1 = 10;
let num2 = 34;
let num3 = 23;

let largestNumber = num1 > num2
    ? (num1 > num3 ? "num1 is greater" : "num3 is greater")
    : (num2 > num3 ? "num2 is greater" : "num3 is greater");

console.log(largestNumber);

console.log("Bitwise Operator : ");
console.log(5&3);
console.log(26|15);
console.log(~3);
