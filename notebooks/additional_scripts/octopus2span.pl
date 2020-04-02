#!/usr/bin/perl -w 
###############################################################################
# written by Bjorn Wallner and modified by Vladimir Yarov-Yarovoy             #
# Script takes transmembrane topology predicted by OCTOPUS server             #
# (http://octopus.cbr.su.se/) and converts it to *.span format for input      #
# to rosetta-membrane ab initio protocol                                      #
###############################################################################

if ($#ARGV < 0) {
    print STDERR "usage: $0 <OCTOPUS topology file>\n";
    exit -1;
}

$file=$ARGV[0];
$monomers=1;
$len=0;
if(defined($ARGV[1]))
{
    $monomers=$ARGV[1];
    $len=$ARGV[2];
}

$TMpred="";
%data=();
$get_sequence=0;
$get_topo=0;
open(FILE,$file);

while(<FILE>)
{
    chomp;
    
    if($get_topo)
    {
	$TMpred.=$_;
    }
    if(/OCTOPUS predicted topology:/)
    {
	$get_sequence=0;
	$get_topo=1;
    }
    if($get_sequence)
    {
	$seq.=$_;
    }
       
    $get_sequence=1 if(/Sequence:/);
   
}

if(length($TMpred)!=length($seq))
{
    print STDERR "Length difference between seq and TMpred!\n";
    print STDERR "$seq\$\n$TMpred\$\n";
    exit(1);
}
$data{$file}=$TMpred;

foreach $key(keys(%data))
{
    print "TM region prediction for $key predicted using OCTOPUS\n";
    for(my $i=1;$i<=$monomers;$i++)
    {
	$offset=($i-1)*$len;
	$span=Mspan($data{$key},$offset);
	print $span;
    }
}

sub Mspan
{
    my ($str,$offset)=@_; #shift;
    my $span="";
    my @pred=split(//,$str);
    my $start=1;
    my $label=$pred[0];
    my $i=1;
    my $counter=0;
    for(;$i<scalar @pred;$i++)
    {
	if($pred[$i-1] ne $pred[$i])
	{
	    my $end=$i;
	    if($label eq "M")
	    {
		$span.=sprintf("%4d  %4d  %4d  %4d\n",$start+$offset,$end+$offset,$start+$offset,$end+$offset);
		$counter++;
	    }
	     $start=$i+1;
	    $label=$pred[$i];
	}
    }
    $end=$i;

    if($label eq "M")
    {
	$span.=sprintf("%d %d %d %d\n",$start+$offset,$end+$offset,$start+$offset,$end+$offset);
	$counter++;
    }
    $span="$counter $end\nantiparallel\nn2c\n$span";
    return $span;
}


