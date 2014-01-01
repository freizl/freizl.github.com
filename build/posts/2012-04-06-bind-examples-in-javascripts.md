---
title: Trivial bind examples in JavaScipts
author: Haisheng, Wu
tags: javascripts
---

# Defined a function

~~~~~~{.javascripts}
var fn = function (x, y, z) {
  console.log("The value: ", this.shangHai);
  console.log("The sum is: ", x+y+z);
}
~~~~~~

# Run it
~~~~~~{.javascripts}
fn(1);
~~~~~~

-> Output

~~~~~~{.javascripts}
The value:  undefined
The sum is:  NaN
~~~~~~

~~~~~~{.javascripts}
fn(1,2,3);
~~~~~~

-> Output:

~~~~~~{.javascripts}
The value:  undefined
The sum is:  6
~~~~~~

# Run it with bind

## Less

~~~~~~{.javascripts}
fn.bind(null,1,2,3)
~~~~~~

-> Output:

~~~~~~{.javascripts}
function () { [native code] }
~~~~~~

Hmm..., seems bind return a function rather apply the function and return value.

What will happen if invoke the new function?

~~~~~~{.javascripts}
fn.bind(null,1,2,3)()
~~~~~~

-> Output:

~~~~~~{.javascripts}
The value:  undefined
The sum is:  6
~~~~~~

That is what we want.

## More

What are results respectively of following expressions?

  - `fn.bind(null, 1)()`
  - `fn.bind(null, 1)(2)`
  - `fn.bind(null, 1, 2)()`
  - `fn.bind(null, 1, 2)(3)`
  - `fn.bind(null, 1).bind(null, 2)()`
  - `fn.bind(null, 1).bind(null, 2)(3)`

Take one example

~~~~~~{.javascripts}
fn.bind(null,1,2)(3)
~~~~~~

-> Output:

~~~~~~{.javascripts}
The value:  undefined
The sum is:  6
~~~~~~

How it produce result 6? \
Because `bind` return is actually a partially applied function of`fn`.

In JavaScripts words, the new function got return is a closure
which holding 1st and 2nd parameters for function `fn` and ready to
accept the third parameter in order to fully apply function `fn`.

The concept is named *Currying* and find more in [Further](#further) section.

_PS_: turns out that `bind` is not really doing Currying according to [here](http://en.wikipedia.org/wiki/Currying)
and [here](http://www.uncarved.com/blog/not_currying.mrk). It is Partially Function Application more than Currying
thouht it can do Currying at some sense.

# Run with bind and context

What I really mean context here is actually about `this` used in the
function. Still now, _this.shangHai_ always output `undefined` but we
would like it to mean something.

~~~~~~{.javascripts}
fn.bind({shangHai:"lovely"},1,2,3)();
~~~~~~

-> Output:

~~~~~~{.javascripts}
The value:  lovely
The sum is:  6
~~~~~~

This time `this.shangHai` outputs "lovely" which obviously comes from
the object that pass as first parameter of `bind`.

Generally speaking,`this` will be the object that pass in as the first
parameter of bind when the object is not null.

Quiz: what `this` will be when passing null?

# Diff with call and apply
My understanding the key point is bind return a function.

By contract, `call` and `apply` is all about providing another way for
invoking a function.

# Further
  - [Currying](http://en.wikipedia.org/wiki/Currying)
