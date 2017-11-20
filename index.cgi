#!/usr/bin/perl
use strict;
use warnings;
use Filesys::DiskSpace;

# file system /home or /dev/sda5
my $dir = "/home";

# get data for /home fs
my ($fs_type, $fs_desc, $used, $avail, $fused, $favail) = df $dir;

# calculate free space in %
my $df_free = (($avail) / ($avail+$used)) * 100.0;

# display message
my $out = sprintf("Disk space on $dir == %0.2f\n",$df_free);

print "Content-type:text/html\r\n\r\n";
print '<html>';
print '<head>';
print '<title>Database events</title>';
print '</head>';
print '<body>';
print "<h2>Status: $out </h2>";
print '</body>';
print '</html>';

1;