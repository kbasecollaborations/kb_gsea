use strict;

open (FILE, "../Ath.chip") or die ("nnc");

my %hashx = ();
while (<FILE>){

my @cr = split ("\t", $_);

$hashx{$cr[0]}++;

}


my %hash = ();
while (<>){
chomp ($_);
 my ($x, $y, @f) = split ("\t", $_);
my @bx =();
 foreach my $line (@f){

     if ($line =~/^AT/){
       if ($hashx{$line}){
       push (@bx, $line);    
      }
     } 

}

 my $n = join ("\t", @bx);
if ($n){
 print "$x\t$y\t$n\n";
}
}


#while (my ($key, $val) = each (%hash)){
#  print "$key\n";
#}
