#!/usr/bin/perl -w

use feature ":5.10";

my $string = "The time is 12:25:30 and I'm hungry.";
if ($string =~ /((\d{1,2}):(\d{2}):(\d{2}))/) {
    my @time = ($1, $2, $3, $4);
    say "@time";
}


# notice the qr and \x

my $two_digits = qr/\d{2}/;
my ($time, $hours, $minutes, $seconds) =
    $string =~ /(                 # capture entire match
                    (\d{1,2})     # one or two digits for the hour
                    :
                    ($two_digits) # minutes
                    :
                    ($two_digits) # seconds
                )
    /x;
say "$hours";

# 
