from mnist_database import mnist_database


mnist = mnist_database()

test_images = mnist.get_test_images()
print('Done')


