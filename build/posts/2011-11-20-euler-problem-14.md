---
title: Solving Euler Problem 14
author: Haisheng, Wu
tags: euler,haskell
---

# Solution One

I should say this solution only work while upper limit is under 100000.
Otherwise it is really slow and I have no patient for the result.
I wonder it would take minutes or even hours.

So, problem solving failed.

~~~~~{.haskell}
module Main where
import Data.Word

main :: IO ()
main = print $ p14

p14 = maximum [ (startChain n 0, n) | n <- [2..1000000] ]

startChain :: Int -> Int -> Int
startChain 1 count    = count + 1
startChain n count    = startChain (intTransform n) (count+1)

intTransform :: Int -> Int
intTransform n
  | even n         = n `div` 2
  | otherwise      = 3 * n + 1

~~~~~

Compile as otherwise Stack space overflow : `ghc --make p14-1.hs -O2 -fforce-recomp -rtsopts`

# Solution Two

I went for Haskell Wiki[^HaskellWiki] for help by finding solution one there is similar to one of its solutions.
The significate difference is it uses type `Word32` for `n` rather than `Int`.
I picked this difference and make the following change and it worked out really cool.

The result came under 1.5s at my local!

~~~~~{.haskell}

startChain :: Word32 -> Int -> Int
startChain 1 count    = count + 1
startChain n count    = startChain (intTransform n) (count+1)

intTransform :: Word32 -> Word32
intTransform n
  | even n         = n `div` 2
  | otherwise      = 3 * n + 1

~~~~~

Compile as otherwise Stack space overflow : `ghc --make p14-1.hs -O2 -fforce-recomp -rtsopts`

# Other solutions

Haskell Wiki[^HaskellWiki] presents several solutions.
One interested me is that levearages parallel programming `Control.Parallel`.

# Further

## **Why solution 2 make great differences?**
I asked question in haskell-beginer but still can not get clear understanding.

## More about Parallel programming in Haskell?

[^HaskellWiki]: [Haskell Wiki Euler Problem](http://www.haskell.org/haskellwiki/Euler_problems/11_to_20)
