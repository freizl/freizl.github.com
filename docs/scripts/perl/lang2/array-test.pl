
use POSIX;
use Data::Dumper;
use List::Util qw(reduce);

my @arr = (1..8);
my @arr_slice = @arr[0..10];
my @arr2 = (2..6);

my @ma = (@arr, @arr2);

my $aoa = [ [1,2,3], [4,7,8] ];
my @ma2 = ();
map { push @ma2, @$_; } @$aoa;
print Dumper(@ma2);
#print Dumper( reduce { [@$a, @$b]; } @aoa ) , "\n" ;

my $ret = unconcat_array(\@arr, 3);
#print Dumper(@$ret[2]), "\n";

my $ids = join(",", map { "'" . $_ . "'" } grep { $_; } @{@$ret[2]});
#print $ids;

sub unconcat_array
{
    my ($arry, $size) = @_;
    $size = 30 if ! $size;
    return ()  if ! $arry;

    my $thredhold = floor( scalar(@$arry) / $size );
    my @ret = map { [ @$arry[0+$_*$size..$size+$_*$size-1] ] ; } (0..$thredhold);
    return \@ret;
}
