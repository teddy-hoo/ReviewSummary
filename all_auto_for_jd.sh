#!/bin/bash
#539349 jsonp1385449909950 1385449925804 ../samples/sample_14/comment ../samples/sample_14/hot_comment
comment_dir=/home/teddy/Documents/yhd_comment/$4

#get_comment
python get_comment_jd.py $1 $2 $3 $comment_dir/comments $comment_dir/hot_comment

#segment and tag
sh for_segment_and_tagger.sh $comment_dir

#ue_evaluation
python ue_analysis_for_chunk.py $comment_dir/comments_tagged