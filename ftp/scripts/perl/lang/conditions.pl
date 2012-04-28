#!/usr/bin/perl -w

@names = qw(Billy Steven Connor);

$n = 0;
while ($names[$n]) {
    print $n+1, ", $names[$n++] \n";
}


$count = 0;
while ($count < 7) {
    if ($count == 3) {
        print "skill $count. \n";
        next;
    } elsif ($count == 4) {
      #        print "Redo $count. \n";
      #       redo;
    } elsif ($count == 5) {
        print "Break out at $count. \n";
        last;
    }
    

    print $count, "\n";
}
continue {
    $count++;
};

foreach $name (sort @names) {
    print "$name\t";
}
print "\n";
