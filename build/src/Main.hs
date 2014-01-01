{-# LANGUAGE OverloadedStrings #-}
module Main where

import           Data.Monoid     (mconcat, (<>))
import           Prelude         hiding (id)
import           System.Cmd      (system)
import           System.FilePath (replaceExtension, takeDirectory)
import qualified Text.Pandoc     as Pandoc

import           Hakyll

postsWildcardMatch :: Pattern
postsWildcardMatch = "posts/**/*"

main :: IO ()
main = hakyllWith config $ do

    -- Compress CSS
    match "css/*" $ do
        route   idRoute
        compile compressCssCompiler

    -- Static directories
    match ("images/*" .||. "codes/*") $ do
        route   idRoute
        compile copyFileCompiler

    -- Tags
    tags <- buildTags "posts/*" (fromCapture "tags/*.html")

    -- just copy pre-compiled slides.
    match "slides/*.html" $ do
        route   $ idRoute
        compile $ copyFileCompiler

    -- Render each and every post
    match "posts/*" $ do
        route   $ setExtension ".html"
        compile $ do
--            pandocCompiler
            pandocCompilerToc
                >>= saveSnapshot "content"
                >>= return . fmap demoteHeaders
                >>= loadAndApplyTemplate "templates/post.html" (postCtx tags)
                >>= loadAndApplyTemplate "templates/default.html" defaultContext
                >>= relativizeUrls

    {--}

    -- Post list
    create ["posts.html"] $ do
        route idRoute
        compile $ do
            posts <- recentFirst =<< loadAll "posts/*"
            let ctx = constField "title" "Posts" <>
                      listField "posts" (postCtx tags) (return posts) <>
                      defaultContext
            makeItem ""
                >>= loadAndApplyTemplate "templates/posts.html" ctx
                >>= loadAndApplyTemplate "templates/default.html" ctx
                >>= relativizeUrls
 
    -- Post tags
    tagsRules tags $ \tag pattern -> do
        let title = "Posts tagged " ++ tag

        -- Copied from posts, need to refactor
        route idRoute
        compile $ do
            posts <- recentFirst =<< loadAll pattern
            let ctx = constField "title" title <>
                        listField "posts" (postCtx tags) (return posts) <>
                        defaultContext
            makeItem ""
                >>= loadAndApplyTemplate "templates/posts.html" ctx
                >>= loadAndApplyTemplate "templates/default.html" ctx
                >>= relativizeUrls

        -- Create RSS feed as well
        version "rss" $ do
          route   $ setExtension "xml"
        compile $ loadAllSnapshots pattern "content"
          >>= fmap (take 8) . recentFirst
          >>= renderRss (feedConfiguration title) feedCtx


    -- Render RSS feed
    create ["rss.xml"] $ do
        route idRoute
        compile $ do
            loadAllSnapshots "posts/*" "content"
                >>= fmap (take 10) . recentFirst
                >>= renderRss (feedConfiguration "All posts") feedCtx

    -- Index
    match "index.html" $ do
        route idRoute
        compile $ do
            posts <- fmap (take 10) . recentFirst =<< loadAll "posts/*"
            let indexContext =
                    listField "posts" (postCtx tags) (return posts) <>
                    field "tags" (\_ -> renderTagList tags) <>
                    defaultContext
            getResourceBody
                >>= applyAsTemplate indexContext
                >>= loadAndApplyTemplate "templates/default.html" indexContext
                >>= relativizeUrls

    -- Render some static pages
{-
    match (fromList []) $ do
        route   $ setExtension ".html"
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls
-}

    -- Render the 404 page, we don't relativize URL's here.
    match "404.html" $ do
        route idRoute
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls

    -- CV as HTML
    match (fromList cvs) $ do
        route   $ setExtension ".html"
        compile $ do
            cvTpl      <- loadBody "templates/cv.html"
            defaultTpl <- loadBody "templates/default.html"
            pandocCompiler
                >>= applyTemplate cvTpl defaultContext
                >>= applyTemplate defaultTpl defaultContext
                >>= relativizeUrls

    -- CV as PDF
    match (fromList []) $ version "pdf" $ do
        route   $ setExtension ".pdf"
        compile $ do
            cvTpl <- loadBody "templates/cv.tex"
            getResourceBody
                >>= (return . readPandoc)
                >>= (return . fmap (Pandoc.writeLaTeX Pandoc.def))
                >>= applyTemplate cvTpl defaultContext
                >>= pdflatex

    match "templates/*" $ compile templateCompiler

  where
    cvs = [ "cv.md", "cv-full.md" ]
    
    pandocCompilerToc = pandocCompilerWith defaultHakyllReaderOptions withToc

    withToc = defaultHakyllWriterOptions
        { Pandoc.writerTableOfContents = True
        , Pandoc.writerTemplate = "$toc$\n$body$"
        , Pandoc.writerStandalone = True
        }

--------------------------------------------------------------------------------
postCtx :: Tags -> Context String
postCtx tags = mconcat
    [ modificationTimeField "mtime" "%U"
    , dateField "date" "%B %e, %Y"
    , tagsField "tags" tags
    , defaultContext
    ]


--------------------------------------------------------------------------------
feedCtx :: Context String
feedCtx = mconcat
    [ bodyField "description"
    , defaultContext
    ]

--------------------------------------------------------------------------------
feedConfiguration :: String -> FeedConfiguration
feedConfiguration title = FeedConfiguration
    { feedTitle       = "Haisheng's Tech Blog " ++ title
    , feedDescription = "Haisheng's Tech Blog."
    , feedAuthorName  = "Haisheng Wu"
    , feedAuthorEmail = "freizl@gmail.com"
    , feedRoot        = "http://freizl.github.io/"
    }

--------------------------------------------------------------------------------
config :: Configuration
config = defaultConfiguration
    { deployCommand = "rsync -c -r -ave 'ssh' \
                      \_site/* freizl_freizl@ssh.phx.nearlyfreespeech.net:/home/public"
    }


--------------------------------------------------------------------------------
-- | Hacky.
pdflatex :: Item String -> Compiler (Item TmpFile)
pdflatex item = do
    TmpFile texPath <- newTmpFile "pdflatex.tex"
    let tmpDir  = takeDirectory texPath
        pdfPath = replaceExtension texPath "pdf"

    unsafeCompiler $ do
        writeFile texPath $ itemBody item
        _ <- system $ unwords ["pdflatex", "-halt-on-error",
            "-output-directory", tmpDir, texPath, ">/tmp/freizl.log", "2>&1"]
        return ()

    makeItem $ TmpFile pdfPath
