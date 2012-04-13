
my $file = "delete.me.file";

mkdir("project") || print "fail to mkdir , : $! \n";

$file = "project/" . $file;

open FH, ">", $file or die "can't open $file: $!\n";
print FH "hi..";
close FH;

open FH2, "<", $file or die "can't open $file: $!\n";
my @lines = <FH2>;
print @lines,"\n";
close FH2;

#unlink $file || print "failed to delete $file: $! \n";
