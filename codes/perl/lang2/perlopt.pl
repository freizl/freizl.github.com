use Getopt::Long;

my $data   = "file.dat";
my $length = 24;
my $verbose;
my @bomdirs = ();
  $result = GetOptions ("length=i" => \$length,    # numeric
                        "file=s"   => \$data,      # string
                        "bomdirs=s{,}" => \@bomdirs,  # array
			"verbose"  => \$verbose);  # flag

print $length,"\n";
print $result,"\n";
map {print $_,","}  @bomdirs;
