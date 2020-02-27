#-*-coding:utf-8-*-

'''
random模块
random.random()用于生成一个0到1的随机浮点数；
random.uniform(a,b)用于生成一个指定范围内的随机浮点数；
random.randint(a,b)用于生成一个指定范围内的随机整数；
random.randrange(a,b,c)在a到b的区间内，步长为c，在该序列中随机取一数字；
random.choice(sequence)参数为一有序类型，如list、tup、dic，随机取一个元素；
random.sample(seq,k)从指定序列中随机获取k长度的片段；
random.shuffle()用于将一个列表中的元素打乱；
'''

import random
#digit 优惠码位数
#count 优惠码数量
def make_promo_code(digit,count):
    base = ord('A')
    results = set()
    alphanums = [str(i) for i in range(10)] + [chr(base+i) for i in range(26)]
    #创建一个字符串，其中包含数字1-9和字母A-Z
    with open('result','w') as f:
        while len(results) < 200:
            temp = ''.join(random.choice(alphanums) for j in range(digit))
            if temp not in results:
                f.write(temp + '\r\n')
                results.add(temp)

if __name__ == '__main__':
    make_promo_code(8,200)
