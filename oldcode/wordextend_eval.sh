#!/bin/bash

work_dir=/home/teddy/Documents/yhd_comment/samples/sample_$1

#python word_extend_for_chunk.py $work_dir/comments_tagged_inverted_list $work_dir/comments_tagged_high_frequency $work_dir/comments_word_about_sentiment $work_dir/comments_word_about_ue 

python ue_eval_for_chunk.py $work_dir/comments_word_about_sentiment $work_dir/comments_word_about_ue $work_dir/comments_tagged_inverted_list $work_dir/comments_ue_eval