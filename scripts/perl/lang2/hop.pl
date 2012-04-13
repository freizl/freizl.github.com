# TODO:
# how to define a sub and use it directly
#
#
my $asub = sub {
    return $_ * $_;
};

my ($pid, $platform) = ("983", "Win");
print $pid, $platform;

my @ar = (1,2,3);
my @ar2 = map { $asub->($_) }  @ar;

map { print $_,"," } @ar;
print "\n";
map { print $_,"," } @ar2;
print "\n";

my @data = ([9,2,3],[9,5,6]);
map {  map {print $_, ","}  @$_; print "\n"; }  @data;


#########
my $c = "Prod";
my $a = "active";

print $c eq "Prod" && $a eq "active";
