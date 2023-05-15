import numpy as np


# Hozz létre egy bemeneti "képet" (numpy array-t)  (5x5)
# Az értékei legyenek 0 vagy 1
# dtype legyen np.float32
img = np.random.randint(low=0, high=2, size=(5, 5)).astype(np.float32)


# Hozz létre egy kernelt (numpy array-t)(3x3)
# Az értékei legyenek 0 vagy 1
# dtype legyen np.float32
kernel = np.random.randint(low=0, high=2, size=(3, 3)).astype(np.float32)


# Mentsd el két külön változóba a létrehozott "kép" (5x5)
# dimenzióinak méretét (height,width)
img_height, img_width = img.shape


# Mentsd el két külön változóba a létrehozott kernel (3x3)
# dimenzióinak méretét (height,width)
kernel_height, kernel_width = kernel.shape


# Számold ki a kimeneti "kép" dimenzióinak a méretét
# Padding = 0, Stride = 1
# A magasságot és szélességet két külön változóba mentsd el
# NOTE: használt az előbb kiszámold "kép" és kernel szélességet és magasságot
output_height, output_width = 3, 3


# Hozz létre egy az előbb kiszámolt kimeneti "kép"
# dimenziójával megegyező 0-kal feltöltött numpy array-t
output = np.zeros((output_width, output_height))


# Hajts végire konvolúciót a bemeneti "képen"
# az eredményt az előbb létrehozott kimeneti "képbe" mentsd el
# NOTE: a kimeneti "kép" 1 db pixel értéke a bemeneti kép n darab értékének összegéből jön létre
# (n = amennyi nem 0 érték van a kernelben)
submatrices = np.lib.stride_tricks.sliding_window_view(img, window_shape=(kernel_width, kernel_height))
for i in range(len(submatrices)):
    for j in range(len(submatrices[i])):
        output[i][j] = np.sum(submatrices[i][j] * kernel)


# printeld ki a bemeneti "képet", kernelt és a végeredményül kapott "képet"
print(img, kernel, output, sep="\n\n")
# Ellenőrizd le, hogy tényleg jó működik a kódod (nem kell semmit írni, csak a printelt értékeket ellenőrizd le)



import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_images, test_images = train_images, test_images

class ConvolutionLayer:
    def __init__(self, kernel_num, kernel_size):
        self.kernel_num = kernel_num
        self.kernel_size = kernel_size
        self.kernels = np.random.randn(kernel_num, kernel_size, kernel_size) / (kernel_size ** 2)

    def patches_generator(self, image):
        image_h, image_w = image.shape
        patches = []
        for h in range(image_h - self.kernel_size + 1):
            for w in range(image_w - self.kernel_size + 1):
                patch = image[h:h+self.kernel_size, w:w+self.kernel_size]
                patches.append((patch, h, w))
        return patches

    def forward(self, image):
        image_h, image_w = image.shape
        convolution_output = np.zeros((image_h - self.kernel_size + 1, image_w - self.kernel_size + 1, self.kernel_num))
        for patch, h, w in self.patches_generator(image):
            convolution_output[h, w] = np.sum(patch * self.kernels, axis=(1, 2))
        return convolution_output, self.kernels

def plot_convolution_output(convolution_output, kernels, title=None):
    nrows, ncols = 2, (convolution_output.shape[-1] + 1) // 2

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols*2, figsize=(15, 6))

    for i in range(nrows):
        for j in range(ncols):
            idx = i * ncols + j
            if idx < convolution_output.shape[-1]:
                # Plot the kernel
                axes[i, j * 2].imshow(kernels[idx], cmap='viridis')
                axes[i, j * 2].set_xticks([])
                axes[i, j * 2].set_yticks([])
                axes[i, j * 2].set_title(f'Kernel {idx + 1}')

                # Plot the corresponding convolution output
                axes[i, j * 2 + 1].imshow(convolution_output[:, :, idx], cmap='viridis')
                axes[i, j * 2 + 1].set_xticks([])
                axes[i, j * 2 + 1].set_yticks([])
                axes[i, j * 2 + 1].set_title(f'Conv Output {idx + 1}')
            else:
                axes[i, j * 2].axis('off')
                axes[i, j * 2 + 1].axis('off')

    if title:
        fig.suptitle(title)

    plt.show()

n = 5
kernel_num = 6
kernel_size = 3

conv = ConvolutionLayer(kernel_num=kernel_num,kernel_size=kernel_size)

for index in range(n):
    plt.imshow(train_images[index])
    features,kernels = conv.forward(train_images[index])
    plot_convolution_output(features,kernels)
