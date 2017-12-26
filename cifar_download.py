# def maybe_download_and_extract():
"""Download and extract the tarball from Alex's website."""
import os
import sys
from six.moves import urllib
import tarfile
# 数据下载地址
DATA_URL = 'https://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz'

dest_directory = '/tmp/cifar10_data' #FLAGS.data_dir
if not os.path.exists(dest_directory):
    os.makedirs(dest_directory)
filename = DATA_URL.split('/')[-1]
filepath = os.path.join(dest_directory, filename)
if not os.path.exists(filepath):
    def _progress(count, block_size, total_size):
        sys.stdout.write('\r>> Downloading %s %.1f%%' % (filename,
                                                         float(count * block_size) / float(total_size) * 100.0))
        sys.stdout.flush()


    filepath, _ = urllib.request.urlretrieve(DATA_URL, filepath, _progress)
    print()
    statinfo = os.stat(filepath)
    print('Successfully downloaded', filename, statinfo.st_size, 'bytes.')
extracted_dir_path = os.path.join(dest_directory, 'cifar-10-batches-bin')
if not os.path.exists(extracted_dir_path):
    tarfile.open(filepath, 'r:gz').extractall(dest_directory)
