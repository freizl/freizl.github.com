---
title: Lesson learned from Euler Problem 104
author: Haisheng, Wu
tags: euler,haskell
---

# Solutions

There are two solutions below. One is written by me and another from haskell wiki.

They look quite similar and I can not figure out why the wiki solution can solve problem but not mine.
(Actually mine take more than 15 minutes)

* My Solution

~~~~~~~{.haskell .numberLines}
main = print $ snd $ head $
       dropWhile (\ (x,y) -> (not . isLastNinePandigit "123456789") x)
                 (zip fibs [1..])

bothNinePandigit digits n =  isFirstNinePandigit digits n
                             && isLastNinePandigit digits n

isLastNinePandigit  digits = (== digits) . sort . lastDigits 9
isFirstNinePandigit digits = (== digits) . sort . firstDigits 9

firstDigits k n = take k (show n)
lastDigits  k n = show (n `mod` 10^k)

~~~~~~~

* Haskell Wiki solution[^HaskellWiki]

~~~~~~~{.haskell .numberLines}

fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

isFibPan n =
  let a = n `mod` 1000000000
      b = sort (show a)
      c = sort $ take 9 $ show n
  in  b == "123456789" && c == "123456789"

ex_104 = snd $ head $
         dropWhile (\(x,y) -> (not . isFibPan) x) (zip fibs [1..])

~~~~~~~

# Why the differences?

The key point here is should test start nine digits first or test end nine digits.

Two concerns here:

1. `show` function is (relatively) slow which used in test first 9 digits function.
2. quite few numbers are end in digits 1..9 in the first 329000 numbers

Therefore test last 9 digits first make great performance improvement.

*Thanks Brent[^Brent] explanation this sneaky thing very comprehensively in haskell-beginner.*

# Profiling

What help to identify is the GHC profiling tool.

Several options used here are

- **prof**: for basic time and allocation profiling

- **auto-all**:
  auto insert cost centers on all top level functions.
  "cost center" is a location in the program like to collect statistics about
  and GHC will generate code to compute the cost of evalutating the expression at each location.
  e.g.

~~~~~
  mean  s = {-# SCC "mean" #-} sum  s / fromIntegral (length s)
~~~~~

- **caf-all**:
  function with no parameters only computed once.
  CAF means constant applicative forms which used for calculate that once time evaluation.

- **fforce-recomp**:
  force full recompilation.


More details could go to chapter 25[^chp25] of [Real World Haskell] and GHC user guider chapter 5[^userguider].

~~~~~
# build with prof option on
ghc --make -O2 -prof -auto-all -rtsopts p104.hs

# then run
./p104 +RTS -p -RTS
~~~~~

# Further

1. Chapter 25 in Real Work Haskell about profile

[^HaskellWiki]: [Haskell Wiki Euler Problem](http://www.haskell.org/haskellwiki/Euler_problems/100_to_110)
[^Brent]: [Haskell Beginner 9175](http://comments.gmane.org/gmane.comp.lang.haskell.beginners/9175)
[^chp25]: [Profiling and optimization](http://book.realworldhaskell.org/read/profiling-and-optimization.html)
[^userguider]: [GHC User Guider](http://www.haskell.org/ghc/docs/latest/html/users_guide/profiling.html)
