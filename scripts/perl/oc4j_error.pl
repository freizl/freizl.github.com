#!/usr/bin/perl -w

### The source error file is a XML file that has nodes like <MESSAGE>...</MESSAGE>,
### which in turn has a type node like <TYPE ...>...</TYPE>
if (@ARGV==0) {
    die "ERROR: specify a log file.";
}

open FILE, ">./output.xml" or die $!;

foreach (@ARGV) {
    print FILE "$_ \n";
    $LOGFILE = $_;
    open LOGFILE or die "Could not open log file $LOGFILE";
    read LOGFILE, $data, -s $LOGFILE;
    #rm all notification and warning message
    $data =~ s#<MESSAGE>.+?TYPE=\"WARNING\".+?</MESSAGE>##gs;
#    $data =~ s#<MESSAGE>.+?TYPE=\"(NOTIFICATION|WARNING)\"><.*?</MESSAGE>\n##gs;
#    $data =~ s#<MESSAGE>.{100,200}?TYPE=\"(NOTIFICATION)\"><.*?</MESSAGE>\n##gs;
#    $data =~ s#<MESSAGE>.{580,630}?<MSG_TEXT>JCA.*?</MESSAGE>\n##gs;
    print FILE $data;
    close LOGFILE;
}

close FILE;
