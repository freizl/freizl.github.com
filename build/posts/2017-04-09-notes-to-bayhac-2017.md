---
title: Somes notes to BayArea Haskell Hackathon 2017
author: Haisheng, Wu
tags: meetup
---

# Some notes to sessions

- BayArea Haskell Hackathon 2017 wiki home [^BayHac2017]

## Haskell for Flight Control at Kittyhawk by Greg Horn

- arrived a little later after session was started and the session didn't last as long as 50 minutes.
- the scenario is they're using haskell to genarate lots of C++ code to control motor of flight devices but missed the key concept how to convert Haskell to C++?

## How to create a new Haskell project by Gabriel Gonzalez

- Quite practical introduction session
- `Setup.hs` could be used to customize build. Shall check more details what it can do.
- `doctest` library could check haddock coverage. fabulous!
- `multi-ghc-travis` could test library against multiple ghc at travis. Interesting. While I still it's a lot easier to utilize multiple stack yaml files.
- Best practice: always to add example to haddock.
- Best practice: 100% haddock coverage.

## Putting lenses to work by John Wiegley

- recommend SPJ lens talk at skill matter [^SPJ-talk] which insprise John
- take away: "use lenses in application and write your own lenses function for library"
  - my question is that will your own lenses functions compatible with the `lens` library when people uses my library and use `lens` library at same time.
- lens comes has theory background (semantic editor contract??) plus Functor and ProFunctor.

## All About Applicative - Adelbert Chang

- free applicative (inspired by free monad)
- `Const` and `Identity` are pretty interesting. (quite similar usage from SPJ talk [^SPJ-talk])
- the key point is use data type (data structor) to represents program so that could do static analysis along with when program is running, and base on the assumption that the analysis doesn't need to know the program computation result.
- code samples at here [^ac-bayhac-2017]

``` haskell
data FileIOF a where
  FileRead :: FilePath -> FileIOF String
  FileWrite :: FilePath -> String -> FileIOF ()

-- the program is created in terms of data
program = fileRead "hello.txt" *> fileWrite "hello.txt" "hello!"

```

## Real World UIs with Reflex by Doug Beardsley

- It's so great to meet Doug in person who is co-author of snap which I was using years ago!
- never use reflex before so cant understand lots of content from talk
- still didnt buy the idea using FRP and GHCJS for frontend.

## Don't Eff It Up: Free Monads in Action by Sandy Maguire

- quite interesting talk. an smart to way to run program in `IO` (usually) and test in within another Monad.
- again, use data type to represent program
- free monad, he uses library called `free-effect`.
- slides: http://reasonablypolymorphic.com/dont-eff-it-up/

## Adjunctions in Everyday Life by Rúnar Bjarnason

- too theoretical to be understood
- looks very beautiful
- more like an proof to existing know stuff rather than discover news

## Epilogue

- Some sessions were happening in parallel at certain time period and some of them I missed seems interesting. Would watch videos after.

# Home work

- what's the fundimental theory of `Functor`, `Applicative`?
- lens
- free monad
- GADT
- type family

[^BayHac2017]: [BayHac2017 wiki home](https://wiki.haskell.org/BayHac2017)
[^SPJ-talk]: [SPJ lens talk](https://skillsmatter.com/skillscasts/4251-lenses-compositional-data-access-and-manipulation)
[^ac-bayhac-2017]: [adelbertc bayhac 2017](https://github.com/adelbertc/bayhac17/blob/master/src/Main.hs)
