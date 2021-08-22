use Date::Format;
use Time::Local;

print time, "\n";

my $str = "20110511";
my ($year, $mon, $day) = ( $str =~ /(\d{4})(\d{2})(\d{2})/);

my $date = timelocal(0, 0, 0, $day, $mon, $year);

my $result =  time2str("%d %b %Y", $date);

print $date, "\n";
print $result;
