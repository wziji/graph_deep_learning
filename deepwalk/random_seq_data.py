# -*- coding: utf-8 -*-

import random

user_num = 10000
item_num = 2000

random_seq_data = open('./data/seq_data.txt', 'w')
for u in range(user_num):
	user_id = 'user_{0}'.format(u)

	watch_item_num = random.sample(range(1, 100), 1)[0]
	item_ids = random.sample(range(item_num), watch_item_num)
	item_ids = ['item_{0}'.format(i) for i in item_ids]
	item_ids = ','.join(item_ids)

	random_seq_data.write('%s\t%s\n'%(user_id, item_ids))

random_seq_data.close()