#!/usr/bin/perl -w 
open IN,$ARGV[0];
$num = $ARGV[1];
$/=">";<IN>;$/="\n";
while (<IN>){
chomp($_);
$id=(split(/\s/,$_))[0];
$/=">";
$seq=<IN>;
chomp ($seq);
$seq=~s/\n+//g;
$len=length($seq);
if ($len > $num){
$id=$id."\t".$len;
$hash{$id}=$seq;}
$/="\n";
}
close IN;
foreach (keys %hash) {
print "$_\n$hash{$_}\n";}