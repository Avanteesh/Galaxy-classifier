import cv2
import numpy as np
from os import path, listdir
from sklearn.svm import SVC
from matplotlib import pyplot as plt

def load_training_data(target_folder):
    dataset = listdir(target_folder)
    x_training, y_training = [], []
    for k, classes in enumerate(dataset, 1):
        class_folder = path.join(target_folder, classes)
        for each_file in listdir(class_folder):
            img = cv2.imread(path.join(class_folder, each_file), cv2.IMREAD_GRAYSCALE)/255
            x_training.append(img)
            y_training.append(k)
    return np.array(x_training), np.array(y_training), dict(enumerate(dataset,1))

def load_testing_data(test_folder):
    testing_data_folder = listdir(test_folder)
    x_test = []
    for each_file in testing_data_folder:
        image = cv2.imread(path.join(test_folder, each_file), cv2.IMREAD_GRAYSCALE)/255
        x_test.append(image)
    return np.array(x_test), [path.join(test_folder, item) for item in testing_data_folder]

def train_and_predict():
    X_train, y_train, data_labels = load_training_data("training-data")
    print(data_labels)
    X_train_flattened = np.reshape(X_train,(X_train.shape[0],X_train.shape[1]*X_train.shape[2]))
    model = SVC(kernel="rbf")
    model.fit(X_train_flattened, y_train)
    testing_data, test_images = load_testing_data("testing-data")
    testing_data_flattened = np.reshape(
      testing_data,(testing_data.shape[0],testing_data.shape[1]*testing_data.shape[2])
    )
    prediction = model.predict(testing_data_flattened)
    print(prediction)
    testimage_index = 1
    plt.imshow(cv2.imread(test_images[testimage_index]))
    plt.title(f"This galaxy is probably: {data_labels[prediction[testimage_index]]}")
    plt.show()

if __name__ == "__main__":
    train_and_predict()


