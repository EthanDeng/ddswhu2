# 本函数用来计算 msg 中每个字母出现的次数.
msg = "Economics"

count = {}
n = 1

for character in msg:
	# 对于 count 这个 dict，因为之前声明为空 dict，所以对于任何 key 都没有指定 value
	# 所以在每次遇到【新】字母的时候 setdefault 会把每个 character 作为 key，并且指定 value 为 0
	# 因为字母 o 在第三次循环的是已经更新过了，所以在第五次的时候，字母 o 这个 key 的 setdefault 语句是无效的。
	count.setdefault(character,0) 

	# 这个语句只是普通的字典更新的方法，dict[key] = X：将 key 的值设定为 X
	count[character] = count[character] + 1
	
	print("第",n,"次循环的时，count 的值",count)

	# 记录循环次数
	n += 1


	



