// === 1

function F(){};
var f = new F();
console.log(f.__proto__ === F.prototype);
F.prototype.someProperty = "some value";
console.log(f.someProperty);
console.log(f instanceof F);

F.prototype = {anotherProperty: "another value"};

console.log(f.someProperty);
console.log(f.anotherProperty);
console.log(f instanceof F);

// === 2
function a(x) {
    return x * 2;
}
var a;
console.log(a);

// === 3

var x = new String("abc"),
    y = String("abc"),
    z = "" + "abc";
console.log(x == y)
console.log(x == z)
console.log(y == z)
console.log(x === y);
console.log(x === z);
console.log(y === z);

// === 4
// http://www.ecma-international.org/ecma-262/5.1/#sec-11.9.3
console.log('' == '0'); // false
console.log(0 == '');   // true
console.log(0 == '0');  // true
console.log(0 == false);  // true
console.log(false == 'false'); // false
console.log(false == '0'); // true
console.log(false == undefined); // false
console.log(false == null); // false
console.log(null == undefined); // true

// === 5
function b(x, y, a) {
    arguments[2] = 10;
    console.log(a);
}
b(1, 2, 3);
