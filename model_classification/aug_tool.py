import imageio  # 读写图像的库
import numpy as np
import imgaug as ia
from imgaug import augmenters as iaa

# 设置种子，以便复现
ia.seed(1)  
# 读入你要进行增强的图像
img = imageio.imread("test.jpg")
# 一张图像增强为 nums 张图像
nums = 10 
# iaa 库的输入是 Numpy 数组
images = np.array([img for _ in range(nums)], dtype=np.uint8)

# Sequential 就是从上到下顺序进行变换
seq = iaa.Sequential(
    [
    	# Sometimes 0.5 就是对所有 nums 张图像中的 50% 进行变换
    	iaa.Sometimes(0.5,
    		iaa.AdditiveGaussianNoise(scale=0.2*255, per_channel=True)
    	),
    	# SomeOf (2, 5) 就是随机进行其中 2 到 5 种变换
    	iaa.SomeOf((2, 5),  
    		[
    		# 亮度
    		iaa.MultiplyAndAddToBrightness(mul=(0.5, 1.5), add=(-30, 30)),
    		# 饱和度
    		iaa.MultiplySaturation((0.5, 1.5)),
    		# 对比度
    		aug = iaa.LinearContrast((0.4, 1.6), per_channel=True),
    		# 锐化
    		iaa.Sharpen(alpha=(0.0, 1.0), lightness=(0.75, 2.0)),
    		# OneOf 就是进行其中一种变换
    		iaa.OneOf([
    			# 模糊
            	iaa.GaussianBlur((0, 3.0)), 
                iaa.AverageBlur(k=(2, 7)), 
                iaa.MedianBlur(k=(3, 11)), 
                ]),
	        ],
	    	random_order=True)  # 这 2 到 5 种变换是随机顺序的  

# 对图像进行数据增强
images_aug = seq.augment_images(images)
# 将 nums 张图像分别进行保存
for i in range(nums):
    imageio.imwrite(str(i) + 'new.jpg', images_aug[i])
