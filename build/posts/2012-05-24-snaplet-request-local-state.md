---
title: 对Snaplet的Request local state的理解
author: Haisheng, Wu
tags: snap, snaplet
---

## 什么 Snaplet

Snap 从 0.6 版本引入 Snaplet 这个设计，它使得 Web 应用什么可组合化，开发者可以设计许多独立的功能模块，或者说小的应用模块，然后通过组合以组建一个大型的应用。

详细资料请看这里[^snaplets-tutorial]。

## Request local state

**Request Local State** 是 snaplet 的一个设计目标[^snaplets-design]。初识时并没引起什么关注，也是不太理解具体含义。最近在写 Snaplet-OAuth 的时候遇到问题，就是由于不知道这个东西的含义所造成的。

## Snaplet-oauth-0.0.0

根据 Snaplet 的常规模式，定义一个 data type 用于保存相关信息，比如

```haskell
data OAuthSnaplet = OAuthSnaplet
                    { getOauth     :: OAuth2
                    , getCodeParam :: BS.ByteString
                    }

class HasOauth b where
    oauthLens :: Lens b (Snaplet OAuthSnaplet)

data OAuth2 = OAuth2 { oauthClientId :: BS.ByteString
                     , oauthClientSecret :: BS.ByteString
                     , oauthOAuthorizeEndpoint :: BS.ByteString
                     , oauthAccessTokenEndpoint :: BS.ByteString
                     , oauthCallback :: Maybe BS.ByteString
                     , oauthAccessToken :: Maybe BS.ByteString
                     } deriving (Show, Eq)
```

如果从 Monad State Trans 的角度去理解， `OAuthSnaplet`就是一个要成为 State 的一个用户类型。
`HasOauth`可以理解为用户和其他 Snaplet 组合的接口。

如下代码就展示了如果将 OAuthSnaplet 加入到一个新的应用程序。(其实就是另一个 Snaplet)
如果你已用过其他 Snaplet，这看上去会很熟悉、常规。

```haskell
data App = App
    { _weibo   :: Snaplet OAuthSnaplet
    }

makeLens ''App

instance HasOauth App where
   oauthLens = weibo
```

拿新浪微薄[^weiboapi]举例，OAuth 的验证简单来说就是

1. 重定向到新浪微薄 OAuth 的验证页面，让用户授权
2. 授权后新浪微薄会调用我们的 App 指定的 Callback URL
3. 我们需要实现这个 Callback 已获取最终的 access token

下面来看下这个 callback 的实现

```haskell

oauthCallbackHandler :: HasOauth b
                     => Maybe BS.ByteString
                     -> Handler b b ()
oauthCallbackHandler uri = do
    oauthSnaplet <- getOauthSnaplet
    codeParam    <- decodedParam' (getCodeParam oauthSnaplet)
    oauth        <- getOauth oauthSnaplet
    maybeToken   <- liftIO $ requestAccessToken oauth codeParam
    case maybeToken of
        Just token -> do
             updateOAuthSnaplet (modify $ modifyOAuthState token)
             redirect $ fromMaybe "/" uri
        _ -> writeBS "Error getting access token."


modifyOAuthState :: AccessToken -> OAuthSnaplet -> OAuthSnaplet
modifyOAuthState (AccessToken at) oa = OAuthSnaplet { getOauth = newOA, getCodeParam = getCodeParam oa }
                                       where newOA = originOA { oauthAccessToken = Just at }
                                             originOA = getOauth oa

updateOAuthSnaplet :: (MonadSnaplet m) => m b OAuthSnaplet a -> m b OAuthSnaplet a
updateOAuthSnaplet = with' oauthLens

```

这里主要关注的是第 11 行到 13 行，`Just token`表示成功获取了 AccessToken，然后要

1. 将 OAuthSnpalet 里的 oauth 的 AccessToken 更新掉。
2. 然后将更新后 OAuthSnaplet 替代掉原来的

这样一来 OAuthSnaplet 就有 AccessToken，在往后的 Handler 都可以拿到这个 AcceeToken 来访问微薄资源。

然后事实并不是这样子，在这个 oauthCallbackHandler 对 OAuthSnaplet 的更新只限于这个 Handler。
**因为 snap 是多线程的且线程安全，每一次的 request 都是对 snaplet 状态的一份新拷贝。**
而由于初始化 OauthSnaplet 的时候是没有 AccessToken 的，这就意谓着所有的 Handler 默认读到的 AccessToken 是空的。

## 如何解决

解决方案就是把`OAuthSnaplet`里的`oauth`变成一个共享变量，这样可以在多线程之间共享。

一种实现方式就是用`MVar`[^mvar]，这样 OAuthSnaplet 就成了这样子

```haskell
data OAuthSnaplet = OAuthSnaplet
                    { getOauth     :: MVar OAuth2
                    , getCodeParam :: BS.ByteString
                    }
```

然后就很直观了，用`Control.Concurrent`库里提供的更新一个 MVar 的方式来做更新和读取。
最后的实现可以参考这里[^github-snaplet-oauth]，不在这里累赘。

## 还有什么问题

你可能已经发现，这样的实现方式，如何支持多用户，以及多个 OAuth Provider 呢？
我还没有答案，如果你知道怎么做，欢迎[send Pull Request].

[send pull request]: https://github.com/HaskellCNOrg/snaplet-oauth

[^snaplets-tutorial]: [Snaplets Tutorial](http://snapframework.com/docs/tutorials/snaplets-tutorial)
[^weiboapi]: [新浪微博授权机制说明](http://open.weibo.com/wiki/%E6%8E%88%E6%9D%83%E6%9C%BA%E5%88%B6%E8%AF%B4%E6%98%8E)
[^mvar]: [MVar](http://www.haskell.org/ghc/docs/7.0-latest/html/libraries/base-4.3.1.0/Control-Concurrent-MVar.html)
[^snaplets-design]: [Snaplets-Design](http://snapframework.com/docs/tutorials/snaplets-design)
[^github-snaplet-oauth]: [Snaplet-OAuth in Github](https://github.com/HaskellCNOrg/snaplet-oauth)
