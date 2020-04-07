data = []
data_length = []
count = 0
data_length_count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		data_length.append(len(line))
		count += 1
		data_length_count += len(line)
		if count % 100000 == 0:
			print(len(data))
			print(data_length_count)
average_length = data_length_count/len(data)
print(data_length_count)
print('留言平均長度為', average_length, '個字')
print('檔案讀取完了，總共有', len(data), ' 筆資料')