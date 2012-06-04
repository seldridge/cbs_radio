#!/usr/bin/perl

use LWP::Simple;

$url_list = "http://www.cbsrmt.com/?s=synopsis&y=all";
$url_dl = "http://www.cbsrmt.com/mp3/CBS%20Radio%20Mystery%20Theater%2074-01-06%20e0001%20The%20Old%20Ones%20Are%20Hard%20to%20Kill.mp3"
$list = "list.html";

getstore($url_list,$list);

open LIST, "<", $list or die "unable to open $list";
foreach $line (<LIST>){
    if ($line =~ m/<td><a href='.\/episode/){
        print $line;
        die;
    }
}
close LIST;
