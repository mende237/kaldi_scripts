#!/bin/bash
error=0

if [ -z "$1" ]
then
    error=1
fi

if [ -z "$2" ]
then
    error=1
fi

if [ $error -eq 1 ];
then
    echo "syntaxe -> ./create_word.sh kaldi_text_path kaldi_word_path"
    exit 1
fi

if [ ! -f $1 ];
then
    echo "File is not found $1"
    exit 1
fi

# if [ ! -f $2 ];
# then
#     echo "File is not found $2"
#     exit 1
# fi

cut -d ' ' -f 2- $1 | sed 's/ /\n/g' | sort -u > $2
sed -i -e $'s/\t//g' -e "s/[[:punct:]]\+//g" -e "s/./\L&/g" $2
