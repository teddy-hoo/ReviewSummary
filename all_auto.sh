#!/bin/bash

comment_dir=/home/teddy/Documents/yhd_comment/$2

#get_comment
python get_comment.py $1 $comment_dir/comments

#segment and tag
sh for_segment_and_tagger.sh $comment_dir

#ue_evaluation
python ue_analysis_for_chunk.py $comment_dir/comments_tagged