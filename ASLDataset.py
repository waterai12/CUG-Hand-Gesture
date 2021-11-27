import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

__CLASSES__ = ['_background_', 'hand', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
               'X', 'Y']


def plot_results(pil_img, boxes, labels):
    plt.imshow(pil_img[..., [2, 1, 0]])
    ax = plt.gca()
    for label, (xmin, ymin, xmax, ymax) in zip(labels, boxes.tolist()):
        ax.add_patch(plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, fill=False, color='r', linewidth=3))
        ax.text(xmin, ymin, __CLASSES__[label], fontsize=15, bbox=dict(facecolor='yellow', alpha=0.5))
    plt.show()


ROOT = 'CUG_Hand'
train_set_dir = os.path.join(ROOT, 'training_dataset.npy')
test_set_dir = os.path.join(ROOT, 'testing_dataset.npy')
data_train = np.load(train_set_dir, allow_pickle=True)
data_test = np.load(test_set_dir, allow_pickle=True)

for i, data in enumerate(data_test):
    image = cv2.imread(os.path.join(ROOT, data['rgb_dir']))
    plot_results(image, data['boxes'], data['label'])
