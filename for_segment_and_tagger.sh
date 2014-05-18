#!/bin/bash
#for stanford segmenter and pos tagger

#comment_dir=/home/teddy/Documents/yhd_comment/$1
segmenter_dir=/home/teddy/stanford_nlp/stanford-segmenter-2013-06-20
tagger_dir=/home/teddy/stanford_nlp/stanford-postagger-full-2013-06-20

#segment
sh $segmenter_dir/segment.sh ctb $1/comments UTF-8 0 > $1/comments_segmented

#for_tag
python comment_process.py $1/comments_segmented

#tag
cd $tagger_dir
sh stanford-postagger.sh models/chinese-distsim.tagger $1/comments_segmented_for_tag > $1/comments_tagged
cd /home/teddy/Documents/yhd_comment/code
