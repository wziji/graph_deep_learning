train_seq_data=data/deepwalk_seq.txt
output_item_vec_data=data/item_vec.txt

word2vec_model='./word2vec' # c version word2vec
size=32
window=8
iter=20
classes=0
binary=0
threads=15
min_count=5

$word2vec_model -train $train_seq_data -output $output_item_vec_data -size $size -window $window -sample 1e-4 -negative 25 -hs 0 -binary $binary -cbow 1 -iter $iter -threads $threads -classes $classes -min_count $min_count 


# Delete the top 2 lines
sed -i 1,2d $output_item_vec_data