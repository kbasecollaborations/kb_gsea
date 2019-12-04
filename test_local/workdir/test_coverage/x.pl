while (<>){

my @cr = split ("\t", $_);

my $x = $cr[0] + $cr[1] + $cr[2] + $cr[3] + $cr[4] ;

if ($x==0){
  next;
}
print $_;
}
