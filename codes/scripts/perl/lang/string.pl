#!/usr/bin/perl -w

use feature ":5.10";

### STRINGS TO BE FORMATTED
$mystring = "welcome to tizag.com!";
$newline = "welcome to \ntizag.com!";
$capital = "\uwelcome to tizag.com!";
$ALLCAPS = "\Uwelcome to tizag.com!";

# PRINT THE NEWLY FORMATTED STRINGS
print $mystring, "\n";
print $newline, "\n";
print $capital, "\n";
print $ALLCAPS, "\n";

### substr
$mystring = "Hello, am I about to be manipulated?!";
print "Original String: $mystring \n";
$substringoffset = substr($mystring, 7);
print "Offset of 7: $substringoffset \n";
$suboffsetANDlength = substr($mystring, 7, 10, "I want");
print "mystring is now: $mystring \n";
print "original off string is: $suboffsetANDlength \n";

### sorting
@names = qw(Simon Jeff Nalen);
print "@names \n";
say "reverse:", reverse @names;
say "inline: ", sort {$a cmp $b} @names;
