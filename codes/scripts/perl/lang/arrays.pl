#!/usr/bin/perl -w

@coins = ("Quarter","Dime","Nickel");

print "@coins \n";
print $coins[0], "\n";

### quotations
@coins2 = qw(Quarter Dime Nickel);
print "@coins2 \n";

### length
@10 = (1 .. 10);
print "@10 \n";
$nums = @10;
print "$nums \n";

print "=== add and move \n";
@coins3 = qw(Quarter Dime Nickel);
push @coins3, "Penny";
print "@coins3 \n";
unshift @coins3, "Dollar";
print "@coins3 \n";
pop @coins3;
print "@coins3 \n";
shift @coins3;
print "@coins3 \n";

print "=== slicing\n";
@slicecoins = @coins[0,2];
print "@slicecoins\n";

print "=== replace\n";
@20 = (1..20);
splice(@20, 2, 5, 21..25);
print "@20 \n";

print "=== transform\n";
$namelist = "Larry,David,Roger,Ken,Michael,Tom";
@names = split(",", $namelist);
print "@names \n";
$namelist2 = join("_", @names);
print "$namelist2 \n";
