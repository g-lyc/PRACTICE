# encoding=utf-8
import os
import imageio
import random
import numpy as np
import imgaug as ia
import concurrent.futures
from imgaug import augmenters as iaa
import matplotlib.pyplot as plt
from argparse import ArgumentParser

ia.seed(4)
# %matplotlib inline

# 参考 https://github.com/aleju/imgaug
func_norm = iaa.ContrastNormalization(alpha=(0.5, 1.5), per_channel=False)
func_add = iaa.Add(value=(-30, 40), per_channel=False)
func_hue_saturation = iaa.AddToHueAndSaturation(
    value=(-35, 30), per_channel=False)
func_multiply = iaa.Multiply(mul=(0.8, 1.5), per_channel=False)
func_gamma = iaa.GammaContrast(gamma=(0.8, 1.5), per_channel=False)
func_log = iaa.LogContrast(gain=(0.7, 1.2), per_channel=False)
func_sigmoid = iaa.SigmoidContrast(gain=(2, 5), cutoff=0.5, per_channel=False)
func_coarse = iaa.CoarseDropout(
    p=(0.1, 0.2), size_percent=0.1, per_channel=False)

switch_func = {
    0: func_norm,
    1: func_add,
    2: func_hue_saturation,
    3: func_multiply,
    4: func_gamma,
    5: func_log,
    6: func_sigmoid,
    7: func_coarse
}


def getFilePath(root_path, file_list):
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        dir_file_path = os.path.join(root_path, dir_file)
        if os.path.isdir(dir_file_path):
            getFilePath(dir_file_path, file_list)
        else:
            file_list.append(dir_file_path)


def getFilePath2(root_path, file_list, folder_list):
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        dir_file_path = os.path.join(root_path, dir_file)
        if os.path.isdir(dir_file_path):
            folder_list.append(dir_file_path)
            getFilePath2(dir_file_path, file_list, folder_list)
        else:
            file_list.append(dir_file_path)


def getFilePathFilters(root_path, file_list, dir_filters):
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        dir_file_path = os.path.join(root_path, dir_file)
        if os.path.isdir(dir_file_path):
            if dir_file in dir_filters:
                getFilePathFilters(dir_file_path, file_list, dir_filters)
        else:
            file_list.append(dir_file_path)


def makeDir(root_path):
    if not os.path.exists(root_path):
        os.makedirs(root_path)


def showImage(image):
    image = np.array(image)
    plt.imshow(image)
    plt.show()


def saveImage(image, write_path):
    imageio.imwrite(write_path, image)


def augmentFunc(image, index):
    return switch_func[index].augment_image(image)


# 多线程执行函数
def augExecute(file_path):
    new_file_path = file_path.replace(args.root_folder, args.new_folder)
    print(new_file_path, end='\n')
    image = imageio.imread(file_path)
    index = random.randint(0, 7)
    new_image = augmentFunc(image, index)
    # showImage(new_image)
    saveImage(new_image, new_file_path)


def colorImageAugment(augment_list, max_workers, dir_dict):
    for augment_folder in augment_list:
        file_list = []
        folder_list = []
        getFilePath2(augment_folder, file_list, folder_list)
        # 创建新目录文件夹及其子文件夹
        for folder_path in folder_list:
            new_folder_path = folder_path.replace(
                args.root_folder, args.new_folder)
            makeDir(new_folder_path)

        if max_workers == 0:
            # 单线程
            for file_path in file_list:
                augExecute(file_path)
        else:
            # 多线程
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                for _ in executor.map(augExecute, file_list):
                    pass


def main(args):
    aug_folder_list = args.image_folder_path
    dir_dict = {'root_dir': args.root_folder, 'trans_dir': args.new_folder}
    max_workers = int(args.max_workers)
    print("Start to augment image")
    colorImageAugment(aug_folder_list, max_workers, dir_dict)
    print("The end")


if __name__ == "__main__":
    parser = ArgumentParser(description="Augment color image")
    parser.add_argument(
        "image_folder_path", nargs='+', help="Absolute path of image folder that going to augmentation")
    parser.add_argument(
        "root_folder", type=str, help="The folder and file under the root_folder is going to augmentation")
    parser.add_argument("new_folder", type=str,
                        help="The folder that going to be build")
    parser.add_argument("max_workers", type=int,
                        default=9, help="Multi thread num")
    args = parser.parse_args()
    main(args)