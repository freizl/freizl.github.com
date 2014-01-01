---
title: "Magic" Monad Transformer
author: Haisheng, Wu
tags: monad, mtl,haskell
---

# Monad-Transformer

The code fragment below is from chapter 18 Monad Transform of \<Real World Haskell\>[^rwh-mt].

When the first time I read this example, I was confused with how it is possible to
use `ask` of `MonadReader` (line 6) and `get` of `MonadState` (line 13) functions in the same `App` Monad content.

The only reasonable explanation is that `App` is both `MonadReader` and `MonadState`.
While looking at `App` type definition (line 1), seems it is not possible.

~~~~~~~{.haskell .numberLines}
type App = ReaderT AppConfig (StateT AppState IO)

constrainedCount :: Int -> FilePath -> App [(FilePath, Int)]
constrainedCount curDepth path = do
  contents <- liftIO . listDirectory $ path
  cfg <- ask
  rest <- forM contents $ \name -> do
            let newPath = path </> name
            isDir <- liftIO $ doesDirectoryExist newPath
            if isDir && curDepth < cfgMaxDepth cfg
              then do
                let newDepth = curDepth + 1
                st <- get
                when (stDeepestReached st < newDepth) $
                  put st { stDeepestReached = newDepth }
                constrainedCount newDepth newPath
              else return []
  return $ (path, length contents) : concat rest
~~~~~~~

# What is the so-called "Magic"

I turn to the source of package mtl[^package-mtl] and finding following implementations.

~~~~~~~{.haskell .numberLines}

-- | ReaderT
instance (Monad m) => MonadReader r (ReaderT r m) where
    ask = ReaderT.ask
    local = ReaderT.local

-- | StateT
instance (Monad m) => MonadState s (Lazy.StateT s m) where
    get = Lazy.get
    put = Lazy.put

-- | Combine ReaderT and StataT
instance (MonadState s m) => MonadState s (ReaderT r m) where
    get = lift get
    put = lift . put

~~~~~~~

If we do a substitution, will get

~~~~~~~
1. instance MonadReader AppConfig App where ...

2. instance (MonadState AppState (StateT AppState IO)
          => MonadState AppState (ReaderT AppConfig (StateT AppState IO)) where ...
   ~> instance MonadState AppState App where ...
~~~~~~~

Therefore `App` is both MonadReader and MonadState.

# A trivial demo

I made a very trivial sample [^demo] demostrating combine ReaderT and StateT.

[^rwh-mt]: [Chapter 8 Monad Transformer](http://book.realworldhaskell.org/read/monad-transformers.html)
[^package-mtl]: [mtl-2.0.1.0 in hackage](http://hackage.haskell.org/package/mtl-2.0.1.0)
[^demo]: [A clear demo](https://github.com/freizl/dive-into-haskell/blob/master/monad/hello-mtl.hs)
