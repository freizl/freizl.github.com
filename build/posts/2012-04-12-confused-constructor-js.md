---
title: Confused Constructor in JavaScipts
author: Haisheng, Wu
tags: javascripts
---

# Introduction

I can not quite remember what happened when invoking `new` over a function.
While I'm looking at function `init` at jQuery source, the concern comes to me again.

Fourtunaly I think the answer at this[^stacknew] thread turns out to be a quite clear explanation.

Just three things according to that answer.

  1. Creates a new object. Its type is `object`.
  2. Sets this new object's internal, inaccessible, `[[prototype]]` property to be the constructor function's external, accessible, `prototype` object.
     *Refer to line 11 at [sample](#sample)*.
  3. Executes the constructor function, using the new object whenever `this` is mentioned.

Regarding #2, we might have question like

  i. What is constuctor function's `prototype` object?
  ii. What is the `[[prototype]]`?

The answer are

  i. Function's `prototype` property is automatically created which in turn has a constructor property pointing back to the function.
     *Refer to line 4 at [sample](#sample)*
  ii. Basically `[[prototype]]` is used for prototype chain. Find details at here[^joost] and Ecma-262[^ecma262].

Therefore if we change the `prototype` property of the function before `new`, the `[[prototype]]` of instances afterwards is vary accordingly.
*Refer to line 19 at [sample](#sample)*

# Sample

- **tested at google chrome 18 and pay close attention to comments.**

~~~~~~{.javascript .numberLines}

var fn1 = function () { this.name = "fn1"; }

fn1.prototype          // Object { constructor: function () { this.name = "fn1"; }
                       //        , __proto__: Object }

fn1.__proto__          // function Empty() {}


var x1 = new fn1();
x1.__proto__ === fn1.prototype  // True

x1.__proto__           // Object { constructor: function () { this.name = "fn1"; }
                       //        , __proto__: Object }
x1.constructor         // function () { this.name = "fn1"; }


fn1.prototype = {'location': 'sea'}

var y1 = new fn1();
x1.__proto__ === fn1.prototype  // True

y1.__proto__;          // Object { location: "sea"
                       //        ,__proto__: Object }
y1.constructor;        // function Object() { [native code] }


~~~~~~

- Quiz: Why y1.constructor is not same as x1.constructor?

# JQuery.fn.init

- `jQuery` is declarated as

~~~~~~{.javascript}
var jQuery = function( selector, context ) {
		// The jQuery object is actually just the init constructor 'enhanced'
		return new jQuery.fn.init( selector, context, rootjQuery );
	},
~~~~~~

- `jQuery.fn` is just a object as

~~~~~~{.javascript}
jQuery.fn = {
	constructor: jQuery,
	init: function( selector, context, rootjQuery ) {
		    var match, elem, ret, doc;
            ... ...
          },
    ... ... // many API declaration.
}
~~~~~~

- Function chain

Since `jQuery` is just a function, we are able to do with a selector like `jQuery('div.navigator').addClass('nav')`.

Actually in order to use jQuery API like `addClass`, there must exists following something
which of cource can be found at around line 322 of jQuery.1.7.1.css[^jquery].

~~~~~~{.javascript}
jQuery.fn.init.prototype = jQuery.fn;
~~~~~~


[^stacknew]: [What is new keyword in JS](http://stackoverflow.com/questions/1646698/what-is-the-new-keyword-in-javascript)
[^joost]: [Constructors considered confusing](http://joost.zeekat.nl/constructors-considered-mildly-confusing.html)
[^ecma262]: [Ecma262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)
[^jquery]: [jQuery 1.7.1](http://code.jquery.com/jquery-1.7.2.js)
