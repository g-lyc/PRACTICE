#!usr/bin/perl 
use strict;
use warnings;                                          #模块的加载

my %hash;                                              #创建一个名为hash的哈希
open IN,"$ARGV[0]";									   #打开文件，命令行第一个参数(就是perl nnn.pl 后边的文件名)
my $title = <IN>;                                      #取第一行赋值给标量$title
chomp $title;                                          #chomp作用于单个变量，去除后边的换行符
my @sample = (split /\t/,$title)[3..13];               #创建一个数组sample，添加标量title中3到13的值，并且用制表符分隔
while (<IN>) {                                         #循环读取文件每一行
	chomp;                                             #去掉每一行后边的换行符
	my @line = split /\t/,$_;                          #将这行元素按照制表符分隔，存储在数组line中
	my @array = @line[3..13];                          #数组line中3到13的元素储存在数组array中
	my $gene = $line[15];                              #标量gene为数组line中的第15个元素
	foreach my $i (0..$#sample) {                      #循环遍历sample的索引
		if (exists $hash{$gene}{$sample[$i]}) {        #如果hash{gene}中存在$sample[$i]这个键，则执行if内的条件
			if ($array[$i] ne '-') {                   #如果array[$i]不等于'-'，则哈希中的二级键自加1
				$hash{$gene}{$sample[$i]} ++;
			}
		}else{
			if ($array[$i] ne '-') {
				$hash{$gene}{$sample[$i]} = 1;
			}else{
				$hash{$gene}{$sample[$i]} = 0;
			}
		}
	}
}
close IN;                                              #关闭打开的文件

print "gene\t",join "\t",@sample,"\n";                 #打印表头
foreach my $key (sort keys %hash) {                    #排序hash中的键并且遍历
	print "$key";                                      
	foreach my $i (@sample){
		print "\t$hash{$key}{$i}";
	}
	print "\n";
}
