#! /usr/bin/perl -w

use Pod::Usage;
use LWP::Simple;
use Getopt::Long;
use Benchmark;

my $component;
my $dryrun;
my $help;

my $depends_dir = "depends";

my @depend_arr = ();

GetOptions ("component=s"   => \$component,
            "dry-run"  => \$dryrun,
            "help|?"   => \$help) or pod2usage(2);

pod2usage(1) if $help;

sub logdebug {
    print "> DEBUG: [ @_ ]; \n" if $dryrun;
}

sub get_externals_value {
    my $url = shift;
    if ( -d $url || head($url) ) {
        my $extern_output = `svn pg svn:externals $url`;
        return unless $extern_output;
        return if ($extern_output =~ /does not exist in revision/ );
        return $extern_output;
    }
}

sub split_external_value_item {
    my $value = shift;
    return split /\s+/, $value, 2;
}

sub get_url_part {
    my @values = split_external_value_item $_;
    return $values[-1];
}


sub retrieve_depends {
    my $wc = shift;
    my $url_callback = shift;
    $wc = $url_callback->($wc) if ($url_callback);
    my $url = "$wc/$depends_dir";

    my $ext_values = get_externals_value($url);
    return undef unless $ext_values;

    map { push @depend_arr, $_; retrieve_depends($_, \&get_url_part);  } split /\n|\r\|\r\n/, $ext_values;
}

sub consolidate_depends {
    my $dependsarr = shift;
    my %depend_hash = ();
    my %error_hash = ();
    foreach my $extern_string (@$dependsarr) {
	logdebug "String: $extern_string";
	my ($component,$version_url) = split_external_value_item $extern_string; #split(/\s+/,$extern_string,2);
	
	# Component already has  defined as a dependency.  Check if it conflicts 
	if (defined $depend_hash{$component} ) {
            my $hash_val = $depend_hash{$component};
            if ( "$hash_val" ne "$version_url")  {
                print "Error: $component has a dependency of $version_url.\n";
                print "\tBut already has a previous dependency of $hash_val\n";
                # Push this onto the Error hash
                $error_hash{$component} = "$version_url";
            }
	} else {
            # Add it to the hash
            $depend_hash{$component} = "$version_url";
	}
    }
    return ( \%depend_hash, \%error_hash );
}

sub do_export {
    my $depends = shift;
    while ( my ($key,$value) = each(%$depends) ) {
        my $export_dir = "$component/../$depends_dir/$key";
        if ( -d $export_dir ) {
            print "Warning: directory already exists: $export_dir \n";
            next;
        }
        unless ( $dryrun ) {
            system("svn export --ignore-externals $value $export_dir");
        } else {
            logdebug "checkout $value to $export_dir";
        }
    }
}

sub main {
    retrieve_depends $component if $component;
    my ($dependhash, $errorhash) =  consolidate_depends \@depend_arr;
    do_export $dependhash;
}

my $t0 = Benchmark->new();
main();
my $t1 = Benchmark->new();
print "Checking out took:", timestr(timediff($t1,$t0)), "\n";

=head1 NAME

RetrieveDepends - 

=head1 SYNOPSIS

RetrieveDepends [options]

  Options:
    --component       target component that retrieveing its depends.(required)
    --dry-run         dry-run checkout
    --help            brief help message

=back

=cut
