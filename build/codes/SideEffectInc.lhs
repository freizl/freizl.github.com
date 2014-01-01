> module SideEffectInc where
> 
> -- Side effect increase
> type Count = Int
> newtype Sint a = Sint {getSint :: (a, Count)}
> 
> instance Monad Sint where
>     return v = Sint (v, 0)
>     p >>= f  = let (a, c1) = getSint p
>                    (b, c2) = getSint (f a)
>                in Sint (b, c1+1)

> sInc ::(Num a) => a -> Sint a
> sInc x = Sint (x+1, 1)

