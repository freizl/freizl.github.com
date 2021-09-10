use Data::Dumper;


sub mychr
{
    return chr($_);
}

my @nums = (50..60);

print map(chr, @nums), "\n";

my $aref = \@nums;

print Dumper($aref);
print map(mychr, @$aref), "\n";


my @list = (1 .. 4);
my @mult = map { $_ *= 2 } @list;
print "\@list = @list\n";
print "\@mult = @mult\n";
