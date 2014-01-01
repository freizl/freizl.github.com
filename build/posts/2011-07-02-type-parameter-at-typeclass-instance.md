---
title: Type parameter at type class instance
author: Haisheng, Wu
tags: typeclass,haskell
---

# A newbie concern

A concern arise while I compare following two instances of `Maybe`.

~~~~~
class Eq a where  
    (==) :: a -> a -> Bool  
    (/=) :: a -> a -> Bool 

class Functor f where
    fmap :: (a -> b) -> f a -> f b

instance (Eq a) => Eq (Maybe a) where
    Just x == Just y = x == y  
    Nothing == Nothing = True  
    _ == _ = False  

instance Functor Maybe where
    fmap f (Just x) = Just (f x)  
    fmap f Nothing = Nothing 

~~~~~

It put `Maybe` as type parameter while instance `Functor` class.
By contract, it is `Maybe a` while at `Eq` case.

Why?

A answer from Haskell beginner seems comprehensive but I did not understand completely. And I re-read chapters related to type from LYGH[^LYGH] and found several useful explanations.

For instance `Maybe` of `Eq`, it reads

> the a has to be a concrete type but Maybe isn't a concrete type. It's a type constructor that takes one parameter and then produces a concrete type. 
> It would also be tedious to write instance Eq (Maybe Int) where, instance Eq (Maybe Char) where, etc. for every type ever. So we could write it out like so: (Eq a) => Eq (Maybe a)

For instance `Maybe` of `Functor`, it reads

> If we want to make a type constructor an instance of Functor, it has to have a kind of * -> *, which means that it has to take exactly one concrete type as a type parameter. For example, Maybe can be made an instance because it takes one type parameter to produce a concrete type, like Maybe Int or Maybe String. If a type constructor takes two parameters, like Either, we have to partially apply the type constructor until it only takes one type parameter. So we can't write instance Functor Either where, but we can write instance Functor (Either a) where and then if we imagine that fmap is only for Either a, it would have a type declaration of fmap :: (b -> c) -> Either a b -> Either a c. As you can see, the Either a part is fixed, because Either a takes only one type parameter, whereas just Either takes two so fmap :: (b -> c) -> Either b -> Either c wouldn't really make sense.

My understanding comes:

parameter `f a` of `fmap` should be concrete type, therefore `f` is a Type Constructor which takes one type parameter in order to construct concrete type. That is the reason the quote says *it has to have a kind of* `* -> *`.

# Another interesting Funtor

It is `(->) r` which was confusing at first glance. However, if we read it having Polish notation[^polish] in mind, it looks like less confusing.

~~~~~~
instance Functor ((->) r) where  
    fmap f g = (\x -> f (g x))
~~~~~~

Quiz: what does following expression produce?

> fmap (*3) (+100) 1

# Further reading

I got to read paper at type class topic[^typeclass] in order to have more knowledge.

[^LYGH]: [Learn Your Good Haskell](http://learnyouahaskell.com)
[^typeclass]: [Wikipedia Type Class](http://en.wikipedia.org/wiki/Type_class)
[^polish]: [Polish notation](http://en.wikipedia.org/wiki/Polish_notation)
