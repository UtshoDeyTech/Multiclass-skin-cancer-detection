# Skin Disease Diagnosis using Custom Convolutional Neural Networks

This repository contains the research work carried out for skin disease diagnosis using a custom Convolutional Neural Network (CNN) model. The model was designed specifically to classify various skin diseases using 28x28 RGB images from the HAM10000 dataset.

## Abstract

Skin diseases pose a significant global health challenge, and their accurate and prompt diagnosis is critical for effective treatment. Machine learning, particularly CNNs, has shown immense potential in skin disease diagnosis due to their ability to process and learn intricate patterns in image data. The custom CNN model developed in this study outperformed well-known pre-trained models like ResNet50 and EfficientNetB0/B2 in terms of test accuracy, test loss, and computational efficiency.

## Dataset

The model was trained, validated, and tested using the HAM10000 dataset, a comprehensive collection of dermatoscopic images from different populations, acquired and stored by different modalities. This dataset contains multiple classes of skin diseases, which allowed our model to learn the distinct features of each condition effectively.

## Model Performance

The model achieved an impressive overall accuracy of 0.97, underlining its reliability in skin disease classification. In comparison with popular pre-trained models, our custom model showcased superior performance, higher test accuracy, lower test loss, and notable computational efficiency. It also exhibits faster average training time per epoch and fewer trainable parameters, making it suitable for deployment in environments with limited computational resources.

## Files in the Repository

- `model.py`: Contains the code for the custom CNN model.
- `training.py`: Contains the code for model training, validation, and testing.
- `model_evaluation.py`: Contains the code for model evaluation and comparison with pre-trained models.
- `data_preprocessing.py`: Contains the code for data preprocessing.

## Conclusion

The research establishes the potential of using a custom CNN model as a potent, efficient, and effective tool for dermatological diagnosis. With its superior performance and computational advantages, our model promises to enhance diagnostic accuracy, potentially enabling earlier and more effective treatments for skin diseases.

## How to Run Code

1. Clone the repository.
```bash
git clone https://github.com/UtshoDeyTech/Thesis-Model.git
```
2. Change the directory
```bash
cd Thesis-Model
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


