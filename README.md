#  2025.5.14使用Git的三个简单指令：
1.添加单个文件：`git add 文件`

2.`git commit -m "对刚上传的代码简单概括"辅助记忆`

3.更新：`git push origin main`


# 5.14完成：
- 成功学会使用isat-sam进行半自动打标签，选择使用电脑yolov5虚拟环境，进入文件夹下E:\fj\ISAT_with_segment_anything-master运行
`python main.py`

- 采集数据集，数据增强代码在E:\fj\ultralytics-main\add_aug.py

- 打完标签为json文件，在isat-sam中进行格式转换，转换成yolo格式

- 运行divide_yolov8.py进行划分数据集，位于E:\fj\ultralytics-main\dispose_yolov8

- 数据集制作完成，开始进行训练，训练代码为train_seg.py,位于E:\fj\ultralytics-main

- 成功学会分析训练结果，不过需要加强
