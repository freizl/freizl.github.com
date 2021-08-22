# PACKAGE DEFINATION

sub uniq {
    return keys %{{ map { $_ => 1 } @_ }};
}
