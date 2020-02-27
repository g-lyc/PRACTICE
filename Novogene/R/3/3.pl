#!/usr/bin/perl -w 
open IN,$ARGV[0];
$/=">";<IN>;$/="\n";
while (<IN>){
 $A=0;
 $G=0;
 $C=0;
 $T=0;
chomp($_);
$id = (split (/\s/,$_))[0];
$/=">";
$seq=<IN>;
chomp ($seq);
$seq=~s/\n+//g;
while($seq =~ m/A/ig){$A++}
while($seq =~ m/C/ig){$C++}
while($seq =~ m/G/ig){$G++}
while($seq =~ m/T/ig){$T++}
$GC=(($C+$G)/($G+$A+$C+$T))*100;
$hash{$id}=$GC;
$/="\n";
}
close IN;
 foreach $actg (sort{$hash{$b}<=>$hash{$a}}keys%hash){
 printf "%4s %4.2f\n",$actg,$hash{$actg};
 }
 

 
 
 
