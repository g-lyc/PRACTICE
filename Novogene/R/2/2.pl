#!/usr/bin/perl -w
$n=1;
$title = join "\t","Chr","Position","Ref";
while($file = shift){
        open IN,$file;
        $id =  (split (/\./,$file))[0];
        $title = $title."\t".$id;
      while(<IN>){
                chomp($_);
                @a = split /\t/,$_;
                $m = join "\t",@a[0..2];
                $seq=$a[3];
                       $hash{$m}{$n} = $seq;
        }
        $n++;
        close IN;
}
print $title,"\n";

foreach $atgc(keys %hash){
        print $atgc,"\t";
        for($i=1; $i<$n; $i++){
                if(exists $hash{$atgc}{$i}){
                        print $hash{$atgc}{$i},"\t";
                }else{
                        print "-\t";
                }
        }
        print "\n";
}

  



       
                
 
  