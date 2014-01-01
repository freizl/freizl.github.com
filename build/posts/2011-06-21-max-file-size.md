---
title: Max size file in desired directory
author: Haisheng, Wu
tags: monad,haskell
---

While doing some refactoring work on solution from this guy[^garriot], I realized a pretty trivial thing about Manod method `>>=`.

Take a look at its definition:

~~~~~
Prelude> :t (>>=)
(>>=) :: (Monad m) => m a -> (a -> m b) -> m b
~~~~~

Both `a` and `b` ought to be some Monadic type!
In other words, all computation glued together by `>>=` have same Manodic type.

It is really straightforward however I did not have that in mind.

Since I did want to define a function take a `String` and return a list of `String` while its implementation has several computations that return IO type.
Obviously the function failed to compiled.
Therefore I changed it to return `IO [String]`.

~~~~~
-- FilePath is from package System.IO and it is synonyms of String
getFilesInDir :: FilePath -> IO [FilePath]
getFilesInDir inp = do 
  isDir <- doesDirectoryExist inp
  files <- if isDir then
              (do
               names <- getDirectoryContents inp
               forM [ inp </> x | x <- names, isNotSpecialDir x ] getFilesInDir)
           else return [[inp]]              
  return $ concat files
~~~~~~

PS:

* Full source code here[^fullcode] or hpaste[^hpaste] which is cool as give me several suggestions.
* I think hpaste using hlint to do code analysis and provide suggestions
* Actually it is possible to have multiple Monad in one `do` levarage Monad Transformers.

[^garriot]: [Never ending](http://www.never-ending.me/blog/2011/06/16/276/)
[^fullcode]: [MaxSizeFile.hs](https://github.com/freizl/dive-into-haskell/blob/master/io/MaxSizeFile.hs)
[^hpaste]: [hpaset](http://hpaste.org/47969)
