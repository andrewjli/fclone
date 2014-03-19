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

$text = breakVariables($text);
#remove all semicolons
$text =~ s/;//g;


#$text = deQualify($text);
# write back to the file
open(FILE, '>TOHprocessed.java');
print FILE $text;
close FILE;
#print $text;



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
	my @matches = $text =~ m/((\w* \s*\w*\s*(\s*,\s*\w*)+;))/g;
	foreach (@matches){	
		#need to get the first word, which is the type
		$a =$_ =~ /^(.*?)\s/;
		$type = $1;
	#	print("type: $type \n");
		$variableStr = $_;
		$variableStr =~  s/$type//g;
		print("variables: $variableStr\n");
		chop($variableStr);
		@variables = split(',', $variableStr);
		foreach(@variables){
		#	$variable = pop(@variables);
			print("$type $_ = 9 \n");

		}	

	}	
	return $text;

}
