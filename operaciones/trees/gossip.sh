#!/usr/bin/env sh


for S in $(cat $1 | awk '{print $1}');
do
	grep $S $2;
done
