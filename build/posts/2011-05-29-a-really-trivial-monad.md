---
title: A really trivial monad
author: Haisheng, Wu
tags: monad,haskell
---

Generally some people saying that Monad is a computation that take a 'world' as parameter and produce a result along with modified 'world'. And this a manner that doing inpure in a pure language.

While thinking in terms of Parser, it means taking a String and produce a result along with the rest of the string which is not parsed[^1]. Consequently, we think a monadic type in Haskell is just a function. 

It probably is at most of time but not have to be. For instance the `Maybe` type. The trial mentioned below is a little similar with `Maybe`.

Actually I would to play with such idea:
    
> To add a count of operations performed to it

Therefore the type is actually any value plus a count

~~~~~
> newtype Sint a = Sint (a, Count)
~~~~~

In order to be a monad, it has to be a instance of `Monad` and the implementation of `>>=` is

~~~~~
> p >>= f = let (a, c1) = getSint p
>               (b, c2) = getSint (f a)
>               in Sint (b, c1+c2)
~~~~~

It means keep the result of the second computation and combinate the count together. Find full code [`here`](/codes/SideEffectInc.lhs)

Now, I realiaze that to implement a Monadic Type, two key points we need to do, which also turn to be simple.

+ Define a type that carry along the 'side effect'
+ Implement Monad class, a.k.a the `>>=` and `return` function[^2]

[^1]: [Functional parsers by Erik Meijer](http://ecn.channel9.msdn.com/o9/ch9/1/1/2/4/0/5/C9LecturesMeijerC8_2MB_ch9.wmv)
[^2]: [Brian Beckman: Don't fear the Monad](http://channel9.msdn.com/shows/Going+Deep/Brian-Beckman-Dont-fear-the-Monads/)
