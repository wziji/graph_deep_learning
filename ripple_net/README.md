参考：https://github.com/hwwang55/RippleNet


# 数据情况

### 1. 交互文件
(1) user \t item 

[user  (点击、购买、加购等行为的)  item]

### 2. 图谱文件
(1) item \t item 

[item  (通过某种关系(同一个品类、品牌或店铺)连接的)  item]

(2) item \t info 

[item  (的信息关系)  eg:品类/品牌]




# 解读 data_loader.py 

### 1. 交互数据
根据 `交互文件` 获得 user 的历史行为数据

例如：

user1 的历史行为数据为：[item_1, item_7, item_8, item_210, item_9]


### 2. 图谱数据
(1) item \t item 

例如： {'item_1': [('item_5', 'same_cate_relation'), ('item_6', 'same_brand_relation')]}

说明： 
> 'item_1', 'item_5', 'item_6' 为 `实体ID`

> 'same_cate_relation'，'same_brand_relation' 为 `关系`

> 'item_1' & 'item_5' 实体共同属于同一个类别(cate)，'item_1' & 'item_6' 实体共同属于同一个品牌(brand)


(2) item \t info 

例如： {'item_1': [('cate_222', 'cate_id'), ('brand_333', 'brand_id')]}

说明： 
> 'item_1', 'cate_222', 'brand_333' 为 `实体ID`

> 'cate_id'，'brand_id' 为 `关系`

> 'item_1' 的 类别(cate)信息是 'cate_222'，'item_1' 的 品牌(brand)信息是 'brand_333'

-----------------------


# 得到每个 user 的扩展序列：
示例 user1: 

user1 -> [(hop_0_heads, hop_0_relations, hop_0_tails), (hop_1_heads, hop_1_relations, hop_1_tails), ...]

### 0 波 (hop_0)： 

> memories_h: ['item_1', 'item_1' ； 'item_7', item_7； ,,,]

> memories_r: ['same_cate_relation', 'same_brand_relation'； ； ,,,]

> memories_t: ['item_5', 'item_6'； ； ,,,,]

得到： ((memories_h, memories_r, memories_t))

抽样得到：  ((sub_memories_h, sub_memories_r, sub_memories_t))


### 1 波 (hop_1)：

接着遍历尾部(tail)数据： sub_memories_t，步骤同上。
