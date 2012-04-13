#! /usr/bin/perl
        
use DBI;

# my $dbh = DBI->connect("dbi:SQLite:dbname=test1.db","","", {'RaiseError' => 1} );
my $dbh = DBI->connect("dbi:SQLite::memory:","","", {'RaiseError' => 1} );

my $rv = $dbh->do("CREATE TABLE test (id INTEGER NOT NULL, desc VARCHAR(80))");
$rv = $dbh->do("INSERT INTO test (id) VALUES (0)");

$dbh->commit();
$dbh->disconnect();
