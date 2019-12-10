use strict;


# perl join.pl file1 file2 >file3


open (FILE1, $ARGV[0]) or die ("cannot open file $ARGV[0]");
open (FILE2, $ARGV[1]) or die ("cannot open file $ARGV[1]");

my @header1 = ();
my @header2 = ();

my %hash1 = ();
my %hash2 = ();
my %hash = ();
my $i=0;

while (<FILE1>){
   $i++;
   chomp ($_);
   my @linesplit = split ("\t", $_);
   if ($i==1){
     @header1 = @linesplit;
   }
   $hash1{$linesplit[0]} = $_;
   $hash{$linesplit[0]}++;
}


$i=0;
while (<FILE2>){
   $i++;
   chomp ($_);
   my @linesplit = split ("\t", $_);
   if ($i==1){
     @header2 = @linesplit;
   }
   $hash2{$linesplit[0]} = $_;
   $hash{$linesplit[0]}++;
}

close (FILE1);
close (FILE2);



my $header1 = join("\t", @header1);
my $header2 = join("\t", @header2);

my $l1 = @header1 -1 ;
my $l2 = @header2 -1 ;

print "$header1\t$header2\n";
while (my ($key, $val) = each (%hash)){

     my $first = $hash1{$key};
     my $second = $hash2{$key};

    if (!$first){
      $first = $l1;
    }

    if (!$second){
      $second = $l2;
    }

 print "$first\t$second\n";

}
