steps=10
walk_length=20

node_to_node_dict_data='data/node_to_node_dict.data'
write_to_seq_file='data/deepwalk_seq'


python random_walk.py $node_to_node_dict_data $steps $walk_length $write_to_seq_file

