#!/bin/bash
: '
/*-------------------------------------
run_pre.sh
gtht

    by Daniel Richards (ddrichar@ucsc.edu)
       on 1-2-2019
--------------------------------------*/
'
rm output.txt
tns preview --bundle > output.txt &

while sleep 1; do 

    if [ $(wc -l < output.txt) -gt 30 ]; then
 	
        break
 
    fi
 
    echo "Sleep "; 
done

./qr_maker output.txt

open `pwd`/preview_qr.html

