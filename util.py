import requests
import numpy as np
import pickle
import torchvision.models as models


def isEmpty(value):
    return True if value is "" else False


def save_url_img(url, save_path):
    img = requests.get(url)
    open(save_path, 'wb').write(img.content)


def get_model(model_name):
    if model_name == 'resnet18':
        model = models.resnet18(pretrained=True)
    else:
        AssertionError("[ERROR] This model is not supported")

    return model


def get_label(label_path):
    with open(label_path, "rb") as f:
        cls_name = pickle.load(f)

    return cls_name


def scaling(img):
    img = img - np.min(img)
    img = img / np.max(img)

    return img