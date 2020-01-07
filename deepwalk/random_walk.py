import sys
import pickle
import random
from tqdm import tqdm


def load_dict_data(node_to_node_dict_data):
	node_to_node_dict = open(node_to_node_dict_data, 'rb')
	node_to_node_dict = pickle.load(node_to_node_dict)

	return node_to_node_dict


def random_walk(node_to_node_dict, \
	steps, \
	walk_length, \
	write_to_seq_file):
	
	write_to_seq_file = open(write_to_seq_file, 'w')

	# epochs --> steps
	for r in range(steps):
		node_index_list = node_to_node_dict.keys()
		print('node num is: ', len(node_index_list))

		for node in tqdm(node_index_list):
			count = 1
			tmp_seq_list = [node]

			while count < walk_length:
				if node not in node_to_node_dict:
					break
				
				cur_node_neighbour_list = node_to_node_dict[node]
				next_node = random.choice(cur_node_neighbour_list)
				tmp_seq_list.append(next_node)

				node = next_node
				count += 1

			tmp_seq = ' '.join(tmp_seq_list)
			write_to_seq_file.write('%s\n'%tmp_seq)

	write_to_seq_file.close()

	return


def main(node_to_node_dict_data, \
	steps, \
	walk_length, \
	write_to_seq_file):

	node_to_node_dict = load_dict_data(node_to_node_dict_data)

	random_walk(node_to_node_dict, \
		steps, \
		walk_length, \
		write_to_seq_file)

	return


if __name__ == '__main__':
	node_to_node_dict_data = sys.argv[1]
	steps = int(sys.argv[2])
	walk_length = int(sys.argv[3])
	write_to_seq_file = sys.argv[4]

	main(node_to_node_dict_data, \
		steps, \
		walk_length, \
		write_to_seq_file)


