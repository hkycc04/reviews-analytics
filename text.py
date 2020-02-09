#讀取共100萬筆紀錄
#為何不用加strip

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 1000 == 0:
        	print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

