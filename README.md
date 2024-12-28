# Skin Disease Diagnosis using Custom Convolutional Neural Networks

This repository contains the research work carried out for skin disease diagnosis using a custom Convolutional Neural Network (CNN) model. The model was designed specifically to classify various skin diseases using 28x28 RGB images from the HAM10000 dataset.

## Abstract

Skin diseases pose a significant global health challenge, and their accurate and prompt diagnosis is critical for effective treatment. Machine learning, particularly CNNs, has shown immense potential in skin disease diagnosis due to their ability to process and learn intricate patterns in image data. The custom CNN model developed in this study outperformed well-known pre-trained models like ResNet50 and EfficientNetB0/B2 in terms of test accuracy, test loss, and computational efficiency.

## Dataset

The model was trained, validated, and tested using the HAM10000 dataset, a comprehensive collection of dermatoscopic images from different populations, acquired and stored by different modalities. This dataset contains multiple classes of skin diseases, which allowed our model to learn the distinct features of each condition effectively.
[Skin Cancer MNIST (HAM10000) Dataset](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)


## Model Performance

The model achieved an impressive overall accuracy of 0.97, underlining its reliability in skin disease classification. In comparison with popular pre-trained models, our custom model showcased superior performance, higher test accuracy, lower test loss, and notable computational efficiency. It also exhibits faster average training time per epoch and fewer trainable parameters, making it suitable for deployment in environments with limited computational resources.

## Files in the Repository

- **01. custom model:** This folder likely contains files related to a custom model implementation or customization. It may include code, configuration files, or documentation specific to your custom model.

- **02. resnet50:** This folder likely contains files related to the ResNet-50 model. ResNet-50 is a popular convolutional neural network architecture commonly used for image classification and computer vision tasks. The folder may include pre-trained weights, model definition files, or scripts for training and evaluating the ResNet-50 model.

- **03. efficientNetB2:** This folder likely contains files related to the EfficientNet-B2 model. EfficientNet is a family of convolutional neural network architectures that are known for their efficiency and performance across various tasks. The EfficientNet-B2 model is a specific variant within the EfficientNet family. The folder may include model files, documentation, or utility scripts specific to the EfficientNet-B2 model.

- **04. efficientnetB0:** This folder likely contains files related to the EfficientNet-B0 model. Similar to the EfficientNet-B2 folder, this folder is specific to the EfficientNet-B0 variant, which is another member of the EfficientNet family. It may contain model files, training scripts, or other resources specific to EfficientNet-B0.


## Conclusion

The research establishes the potential of using a custom CNN model as a potent, efficient, and effective tool for dermatological diagnosis. With its superior performance and computational advantages, our model promises to enhance diagnostic accuracy, potentially enabling earlier and more effective treatments for skin diseases.

## How to Run Code

1. Clone the repository.
```bash
git clone https://github.com/UtshoDeyTech/Multiclass-skin-cancer-detection.git
```
2. Change the directory
```bash
cd Multiclass-skin-cancer-detection
```
3. Create a Virtual Enviroment
```bash
python -m venv env
```
4. Activate the enviroment
```bash
.\env\Script\activate
```
5. Install the Libraries from the requirements.txt files
```bash
pip install -r requirements.txt
```
6. Now run this comand to open jupyter lab (If you used jupyter lab)
```bash
jupyter lab
```


