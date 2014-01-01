module Main where


> ----- Yet another Haskell toturial
> -- Exercise 3.10 Write a program that will repeatedly ask the user for numbers until she
> -- types in zero, at which point it will tell her the sum of all the numbers, the product of
> -- all the numbers, and, for each number, its factorial.

> main :: IO ()  
> main = do  
>     xs <- sgetline  
>     mapM_ (\s -> putStrLn s) (showSum xs : showProduct xs : (map showFactorial xs))
>   where   
>     showSum xs = "The sum is: " ++ (show . sum) xs
>     showProduct xs = "The product is: " ++ (show . product) xs
>     showFactorial xs = (show x) ++ " factorial is: " ++ (show . factorial) xs
>       
> sgetline :: IO [Int]  
> sgetline = do
>     putStrLn "Give me a number (or 0 to stop) :"    
>     x <- getLine  
>     if x `elem` ["", "0"] then -- isStringEmpty??  
>       do return []  
>       else  
>       do xs <- sgetline  
>          return ((read x):xs)  
>   
> factorial n = product [1..n]
