#!usr/bin/perl 
use strict;
use warnings;

my %hash;
open IN,"$ARGV[0]";
my $title = <IN>;
chomp $title;
my @sample = (split /\t/,$title)[3..13];
while (<IN>) {
	chomp;
	my @line = split /\t/,$_;
	my @array = $line[3..13];
	my $gene = $line[15];
	foreach my $i (@array) {
		if ($array[$i] eq '-') {
			$array[$i] = 0;
		}else{
			$array[$i] = 1;
		}
	}
	if (exists $hash{$gene}) {
		$hash{$gene} = [map{${$hash{$gene}}[$_] + $array[$_]} 0..10];
	}else{
		$hash{$gene} = [@array];
	}
}
close IN;

print "gene\t",join '\t',@sample,"\n";
foreach my $key (%hash) {
	print "$key\t$hash{$key}\n";
}