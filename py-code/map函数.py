
#把不规范的名字改成首字母大写，后边字母小写的形式
#方法1
a=['adam','LISA','barT']
def f(x):
	n=x[0].upper()+x[1:].lower()
	return n
map(f,a)

#方法2
name = ['jim','ToM','KOII']
name = [x.capitalize() for x in name]

#方法3
name = map(lambda x: x.capitalize()), name)

string.capitalize()#返回首字母大写的字符串副本
