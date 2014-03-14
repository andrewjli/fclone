#!/usr/bin/perl
#read in the whole file as a string
local $/=undef;
open(FILE, 'TOH.java');
$text = <FILE>;
close FILE;
#replace all comments with nothing
$text =~ s{(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)}{}g;
#remove import statements
$text =~ s/import(.*)\n//g;

#remove all semicolons
$text =~ s/;//g;
# write back to the file
open(FILE, '>TOHprocessed.java');
print FILE $text;
close FILE;
$text = deQualify($text);
print $text;
sub deQualify{
	my $text = $_[0];
	print $text;
	my @matches = $text =~ m/([a-zA-Z]\w*\.[a-zA-Z]\w*)(\.[a-zA-Z]\w*)*/g;
	foreach (@matches){
		@haystack = split('\.', $_);
		$deQualified = pop (@haystack);
		$text =~ s/$_/$deQualified/g;
		
	}
	return $text;


}
