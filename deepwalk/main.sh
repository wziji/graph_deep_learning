echo "create seq data(true seq data) ~~~"
python random_seq_data.py

echo ""
echo "get node dict !!!"
sh node_to_node_dict.sh

echo ""
echo "create random walk seq data ~~~"
sh random_walk.sh

echo ""
echo "train word2vec model, get item vec data !!!"
sh train_word2vec_model.sh