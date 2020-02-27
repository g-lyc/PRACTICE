#!/usr/bin/perl -w
open IN," $ARGV[0] " || die $!;
open OUT,"> $ARGV[1]" || die $!;
while ($dna=<IN>) {
        @data = (split (/\t/,$dna));
#        if ($data[1]=~/\S/) {
	$id=$data[1].$data[2];
        $hash1{$id}=join "\t",@data[1..6],$data[11],$data[12]; 
        if ($dna=~/杂合/) {
        	 if (exists $hash{$id} ){
                 	$hash{$id}++;
                 } 
                 else {
                 	$hash{$id}=1;
                 }
        }
        elsif ($dna=~/纯合/) {
        	if (exists $hash2{$id}){
                	$hash2{$id}++;
                }
                else {
                        $hash2{$id}=1;
                } 
        } 
#        }
}
foreach (keys %hash1) {
#	if ($hash{$id}!=0 && $hash2{$id}==0) {
                unless (exists $hash2{$_}){
                	$hash2{$_}=0;
                }
                unless (exists $hash{$_}){     
                        $hash{$_}=0;
                }
        	print OUT "$hash1{$_}\t$hash{$_}+$hash2{$_}\n";
}
