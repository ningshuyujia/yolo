import os
import numpy as np
from PIL import Image, ImageEnhance
import random


def adjust_brightness(image):
    """随机调整亮度"""
    enhancer = ImageEnhance.Brightness(image)
    factor = random.uniform(0.5, 1.5)  # 亮度调整范围
    return enhancer.enhance(factor)


def add_noise(image):
    """添加高斯噪声"""
    img_array = np.array(image).astype(np.float32)
    noise = np.random.normal(0, 25, img_array.shape).astype(np.float32)  # 噪声强度
    noisy_array = np.clip(img_array + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_array)


def random_rotate(image):
    """随机旋转图像"""
    angle = random.uniform(-30, 30)  # 旋转角度范围
    return image.rotate(angle, expand=False, fillcolor=(255, 255, 255))


def random_translate(image):
    """随机平移图像"""
    dx = random.randint(-50, 50)  # 水平平移范围
    dy = random.randint(-50, 50)  # 垂直平移范围
    return image.transform(
        image.size,
        Image.AFFINE,
        (1, 0, dx, 0, 1, dy),
        fillcolor=(255, 255, 255)
    )


def apply_augmentations(image, output_path, augmentations):
    """应用数据增强并保存结果"""
    base_name = os.path.splitext(os.path.basename(output_path))[0]
    for i, augment in enumerate(augmentations):
        augmented_image = augment(image)
        augmented_image.save(f"{output_path}/{base_name}_aug{i}.jpg")


# 参数配置
input_dir = "E:/fj/ultralytics-main/datasets_5.13/images/val"  # 输入目录
output_dir = "E:/fj/ultralytics-main/datasets_5.13/images/valaugmented_images"  # 输出目录
num_augmentations = 5  # 每张图片生成的增强版本数量

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 定义增强方法列表
augmentation_functions = [
    adjust_brightness,
    add_noise,
    random_rotate,
    random_translate,
    lambda img: random_translate(random_rotate(add_noise(adjust_brightness(img))))  # 组合增强
]

# 遍历并处理所有图片
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg")):
        img_path = os.path.join(input_dir, filename)
        original_image = Image.open(img_path)

        # 应用所有基础增强方法
        for aug_func in augmentation_functions[:4]:
            augmented = aug_func(original_image.copy())
            augmented.save(os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_{aug_func.__name__}.jpg"))

        # 生成组合增强版本
        for i in range(num_augmentations):
            img = original_image.copy()
            # 随机应用多种增强
            if random.random() > 0.5:
                img = adjust_brightness(img)
            if random.random() > 0.5:
                img = add_noise(img)
            if random.random() > 0.5:
                img = random_rotate(img)
            if random.random() > 0.5:
                img = random_translate(img)

            img.save(os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_comb_{i}.jpg"))

print("数据增强完成！")