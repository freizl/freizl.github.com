use Switch;

my $team = 3;

print localtime;

switch (@ARGV[0]) 
{
    case [2] 
    { 
        print "I am 2 \n"; 
    }
    case [3,7] 
    { 
        print "I am 3 or 7 \n"; 
    }
    case [1..9] 
    { 
        print "I am in 1..9 \n"; 
    }
}

print "\n";
print localtime;
