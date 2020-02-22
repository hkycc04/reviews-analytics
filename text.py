#讀取共100萬筆紀錄
#為何不用加strip，加入後讀取筆數有差異

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
        	print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均長度是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言小於100字')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '留言提到good')


#文字計數

wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 #出現後次數加1
		else:
			wc[word] = 1 #第一次出現碰到新增設定1，加入
for word in wc: #把key抓出來
	if wc[word] > 1000000:
		print(word, wc[word]) #後面的次數也印出來
print(len(wc))

while True:
	word = input('請問您想查什麼字: ')
	if word == 'q':
		print('謝謝使用')
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('沒有這個字喔')


