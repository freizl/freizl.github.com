#!/usr/bin/perl

##############################
# 1. No comma when print to FileHandle.
#    Actually I think the print function syntax is
#    print FILEHANDLE $output_data
#    by default:
#    FILEHANDLE is STDOUT
#    $output_data could be string or arrays
##############################

use feature ':5.10';

$INPUTFILE = "./input.txt";

open $afile, $INPUTFILE or die "Can not open file $INPUTFILE: $!";
#@data = <$afile>;
say "=== 1";
print while <$afile>;
close $afile;

$OUTPUTFILE = 'output.txt';
open $bfile, '>', $OUTPUTFILE or die "Can not create file $OUTPUTFILE: $!";
say  $bfile "a new file";
close $bfile;

open $bfile, '>>', $OUTPUTFILE or die "Can not create file $OUTPUTFILE: $!";
say $bfile "append data";
close $bfile;

#TODO: file testing like -M, -s, -e
open $afile, $INPUTFILE or die "Can not open file $INPUTFILE: $!";
print(join("\n", stat($afile)));
close $afile;
