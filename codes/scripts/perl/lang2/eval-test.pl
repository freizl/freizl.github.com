
my $a = 11;
my $b = 22;
my $x = '$a + $b';
print eval $x;
print eval '$x';
print eval { $x };
