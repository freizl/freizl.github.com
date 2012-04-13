# TODO:
# how to define a sub and use it directly
#
#
my $x = 'RCA1:None';
my $y = 'RCA1:CVS,CVS';
my $pattern = 'RCA\d:(?!None)'; 
if ( $x =~ /$pattern/ ) {
	print "Match: x" . "\n" ;
}
if ( $y =~ /$pattern/ ) {
	print "Match: y" . "\n" ;
}

my $rca = "Integration site, packing-test";
    if ( $rca =~ /([\w\s-]+), ([\w\s-]+)/i ) {
		print $1 . "::" . $2;
    } else {
        print "ERROR: incorrect pattern found of RCA: $rca";
    }
