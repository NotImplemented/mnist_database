import urllib
import os.path
import gzip


class mnist_database:

    test_file_images = 't10k-images-idx3-ubyte'
    test_file_labels = 't10k-labels-idx1-ubyte'

    train_file_images = 'train-images-idx3-ubyte'
    train_file_labels = 'train-labels-idx1-ubyte'

    database_location = 'http://yann.lecun.com/exdb/mnist/'

    def get_contents(self, filename):

        if not os.path.exists(filename):

            url = self.database_location + filename + '.gz'
            print('Getting {} ...'.format(url))

            urllib.urlretrieve(self.database_location + filename + '.gz', filename + '.gz')
            print('Done')

        with gzip.open(filename + '.gz', 'rb') as file:
            contents = file.read()

            return contents

    def get_test_images(self):

        images = self.get_contents(self.test_file_images)
        return images
