#!/usr/bin/perl -w

use feature ':5.10';

sub multiply1 {
    my (@ops) = @_;
    return $ops[0] * $ops[1];
}

sub multiply2 {
    my ($x, $y) = @_;
    return $x * $y;
}

for my $i (1 .. 10) {
     say "$i squared is ", multiply2($i, $i);
}
