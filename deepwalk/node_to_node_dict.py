from tqdm import tqdm 
import pickle
import sys
from collections import defaultdict


def get_node_to_node_dict(seq_data, \
	node_to_node_dict_file):

	node_to_node_dict = defaultdict(list)

	with open(seq_data) as f:
		for line in tqdm(f):
			if line == '':
				continue

			line_list = line.strip().split('\t')
			if len(line_list) != 2:
				continue

			seq_list = line_list[1].split(',')
			if len(seq_list) == 1:
				continue

			for i in range(len(seq_list)-1):
				start_node = seq_list[i]
				end_node = seq_list[i+1]

				node_to_node_dict[start_node].append(end_node)


	# wb --> w
	with open(node_to_node_dict_file, 'wb') as wf:
		wf.write(pickle.dumps(node_to_node_dict))



if __name__ == '__main__':
	seq_data = sys.argv[1]
	node_to_node_dict_file = sys.argv[2]

	get_node_to_node_dict(seq_data, \
		node_to_node_dict_file)

