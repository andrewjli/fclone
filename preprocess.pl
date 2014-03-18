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


$text = deQualify($text);
$text = breakVariables($text);
# write back to the file
open(FILE, '>TOHprocessed.java');
print FILE $text;
close FILE;
print $text;



#dequalifies any functions/variabe declearations,
# java.lang.Integer becomes Integer
# system.out.println becomes println
sub deQualify{
	my $text = $_[0];
	print $text;
	my @matches = $text =~ m/(\w+\.\w+[\.\w+]+)/g;
	foreach (@matches){
		print("match: $_\n");
		@haystack = split('\.', $_);
		$deQualified = pop (@haystack);
		$text =~ s/$_/$deQualified/g;
		
	}
	return $text;
}

sub breakVariables{
	my $text = $_[0];
	#the whole thing
	my @matches = $text =~ m/(([a-zA-Z0-9].*\s*(\s*\,[a-zA-Z0-9].*)+)\s*=\s*'*"*\w.*"*'*)/g;
	foreach (@matches){	
		my $thing = $_ =~ m/(([a-zA-Z0-9].*(\,[a-zA-Z0-9].*)+)\s*)/g;
		print $thing;
		

	}	
	return $text;

}
