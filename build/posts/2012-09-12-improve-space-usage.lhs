---
title: Improve Space Usage
author: Haisheng, Wu
tags: reading,haskell
---

It is example from [programming in haskell] video lection 12 by Eric M.
I just like to know whether GHC profile tool could help to figure out such problem.


> module Main where
> 
> sumWith1 v [] = v
> sumWith1 v (x:xs) = sumWith1 (v+x) xs
> 
> sumWith2 v [] = v
> sumWith2 v (x:xs) = (sumWith2 $! (v+x)) xs
>
> test = sumWith2 0 [1..20000000]
> 
> main = print test
> 
