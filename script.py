import numpy as np

a = np.array([[1,2,3,4,5], [1,2,3,4,5]])
b = np.arange(-5, 5, 1) 
#
c = np.linspace(1, 4, 3)
#
d = np.zeros((5, 3))# создаёт нулевой массив
#
s= np.ones((4, 4))
#
arr = np.random.randint(0, 20, 20)
mask = arr % 2 == 0
# print(mask)
# print(arr[mask])



import matplotlib.pyplot as plt
# plt.figure()
# x = np.arange(-10, 10.2, 0.2)
# for i in range(1, 6):
#     plt.plot(x, x**i)
# plt.show()



# t = np.linspace(-4*np.pi, 4* np.pi, 200)
# sn = 4 * np.sin(t)
# cs = np.cos(t*2)

# plt.plot(t, sn, label="sin(t)")
# plt.plot(t, cs, label="cos(t)")
# plt.grid()
# plt.legend()
# plt.show()


# r = 10
# x = []
# y = []

# for i in range(0, 360, 1):
#     x.append(r * np.cos(np.deg2rad(i)) + (-2))
#     y.append(r * np.sin(np.deg2rad(i)) + (2))

# plt.figure(figsize=(5, 5))
# plt.plot(x, y)
# plt.show()



# for y in range(image.shape[0]):
#     for x in range(image.shape[1]):
#         image[y, x] = np.sin(x/1) * np.cos(y/100)



# n = 0
# image = np.zeros((500, 500))

# for i in range(0, 500, 25):
#     for j in range(0, 500, 25):
#         image[i:i+25, j:j+25] = n
#         n += 1

# plt.figure(figsize=(5, 5))
# plt.imshow(image, cmap="pink_r")
# plt.show()



# x = np.arange(600).reshape(600, 1)
# y = np.arange(600).reshape(1, 600)
# r = 125
# image = (y-300)**2 + (x-300)** 2 >= r **2
# plt.imshow(image, cmap="pink_r")
# plt.show()





# from scipy.datasets import face

# def block_mean(image, y_size=20, x_size=20):
#     result = np.zeros_like(image)
#     for y in range(0, image.shape[0], y_size):
#         for x in range(0, image.shape[1], x_size): 
#             sarr = image[y:y+y_size, x:x+x_size]
#             result[y:y+y_size, x:x+x_size] = sarr.mean()
#     return result

# image = face(gray=True)
# plt.imshow(block_mean(image), cmap="gray")  
# plt.show()
#енот в плохое качество



from scipy.datasets import face

image = face(gray=True)

image = face(gray=True)
noised = image.copy()  # Создаем копию изображения

def mse(img1, img2):
    diff = ((img1 - img2) ** 2).sum()
    return diff / img1.size

def psnr(img1, img2):
    m = mse(img1, img2) ** 0.5
    return 20 * np.log10(img1.max() / m)

print(psnr(image, image))

n = 10
x = np.random.randint(0, image.shape[1], n)  # Убраны пробелы после randint
y = np.random.randint(0, image.shape[0], n)  # Убраны пробелы после randint
noised[y, x] = np.random.randint(0, 255, n)  # Правильная индексация

print(psnr(image, noised))
plt.subplot(121)
plt.imshow(image)  # image а не imsge
plt.subplot(122)
plt.imshow(noised)
plt.show()  # Добавлен show()