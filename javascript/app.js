// Type of Data

// // Примитивные данные
// console.log(2021, 1.5);  // Integer
// console.log(20 * 'String'); // NaN
// console.log("String");  // String
// console.log(1 / 0);  // Infinity
// console.log("Hello", "Hello", `Hello`); // String
// console.log(true, false);  // Bulean
// console.log(null);  // Null
// console.log(undefined);  // Undefined
// console.log(Symbol());  // Symbol

// // Ссылочные данные
// console.log({ name: "Denis", age: 30 })  // Object
// console.log([ 1, 3, 4, 4 ])  // Object

const firstName = "Denis";
const lastName = "Pupkin";
const age = 30;

let str_1;
let div;

// ES5

// str_1 = '<ul>' +
// '<li>First name: ' + firstName +'</li>' +
// '<li>Last name: ' + lastName + '</li>' +
// '<li>Age: ' + age + '</li>' +
// '</ul>'
// document.body.innerHTML = str_1

// ES6

str = `
    <ul>
        <li>First name: ${firstName}</li>
        <li>Last name: ${lastName}</li>
        <li>Age: ${age}</li>
        <li>Math.random: ${Math.random()} </li>
        <li>5 + 5: ${5 + 5} </li>
        <li>Сейчас: ${new Date()} </li>
    </ul>

`;
document.body.innerHTML = str;

const user = {
  firstName: "Denis",
  lastName: "Pupkin",
  age: 30,
  isAdmin: true,
  email: "test@testusers.com",
  user_address: {
    city: "Moscow",
    street: "Lenina",
    building: "23",
  },
  skills: ["html", "css", "js"],
};

let value;
let prop;

prop = "email";
value = user.firstName;
value = user["isAdmin"];
value = user["user_address"];
value = user["user_address"]["city"];
value = user[prop];

user.firstName = "Den";
user.info = "Some info";
user["user_address"].city = "SPB";
user["user_address"].country = "Russia";

console.log(user);
console.log(value);
