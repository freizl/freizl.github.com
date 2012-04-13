#!/usr/bin/perl -w

%coins = ("Quarter", 25, "Dime", 10, "Nickel", 5);
print %coins, "\n";

### Interator keys & values
while (($key,$value) = each(%coins)) {
    print "$key, $value \n";
}

### Interator keys
foreach $key (keys %coins) {
    print "$key,";
}
print "\n";

### Add and remove
$coins{"Penny"} = 1;
print %coins, "\n";

delete($coins{Dime});
print %coins, "\n";
