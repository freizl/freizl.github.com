
my @x = ('RCA1:None','RCA1:CVS,CVS');
my $pattern = 'RCA\d:(?!None)'; 

### will print out @x[1] and ignore @x[0]
print grep { $_ =~ /$pattern/; } @x;
