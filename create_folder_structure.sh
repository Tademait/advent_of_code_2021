#!/bin/bash
i=3
while [ "$i" -lt 25 ];do
    mkdir "advent${i}"
    (cd "advent${i}" || exit
    touch "advent${i}.py"
    touch "advent${i}b.py"
    touch "input.txt"
    )
    (( i=i+1 ))
done