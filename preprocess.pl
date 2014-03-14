#!/usr/bin/perl
#read in the whole file as a string
local $/=undef;
open(FILE, 'TOH.java');
$text = <FILE>;
close FILE;
#replace all comments with nothing
$text =~ s{(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)}{}g;
$text =~ s/import(.*)\n//g;

#remove all semicolons
$text =~ s/;//g;
# write back to the file
open(FILE, '>TOHprocessed.java');
print FILE $text;
close FILE;
deQualify($text);

sub deQualify{


}
