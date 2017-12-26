# myfirstcifar
cifar图像识别笔记文档
整个程序包含  部分分别是：
1，	图像数据下载，对应的程序是cifar_download.py:
其使用six.moves的urllib
https://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz下载数据包
并且使用tarfile 模块解压

2，	图像输入到模型，采用distorted_inputs，输入图像，并且包含label
3，	整个计算图采用2个卷积层+Relu激活函数+池化+LRN归一化（现在最流行的是batch normaling）,在连接2个全连接层和一个输出层，
4，	第1层卷积层中的卷积内核形状5x5，输入3通道，输出64通道，步进为1.
5，	第1层卷积层中池化的内核形状3x3，步进为2,   其权值变量计算L2范数并decay后计入LOSS（实际上decay = 0所以并没有计入LOSS）
6，	第2层卷积层中的卷积内核形状5x5，输入64通道，输出64通道，步进为1.
7，	第2层卷积层中池化的内核形状3x3，步进为2,    其权值变量计算L2范数并decay后计入LOSS（实际上decay = 0所以并没有计入LOSS）
第3层全连接层输出为384，输入大小dim根据函数reshape = tf.reshape(pool2, [FLAGS.batch_size, -1])
dim = reshape.get_shape()[1].value ；最终使用Relu作为激活函数, 其权值变量计算L2范数并decay后计入LOSS（实际上decay = 0.004计入LOSS）
8，	第4层全连接层输入为384，输出为192，使用Relu作为激活函数, 其权值变量计算L2范数并decay后计入LOSS（实际上decay = 0.004计入LOSS）
9，	输出层全连接层输入为192，输出为10，使用softmax作为激活函数 , 其权值变量计算L2范数并decay后计入LOSS（实际上decay = 0所以并没有计入LOSS）
10，	Loss层计算交叉熵LOSS，并叠加上之前计算的LOSS，形成L2正则化
训练操作，采用学习率下降方法，tf.train.exponential_decay（），实现特定步长的学习速率下降。采用opt = tf.train.GradientDescentOptimizer(lr)
                grads = opt.compute_gradients(total_loss)
            apply_gradient_op = opt.apply_gradients(grads, global_step=global_step)
实现梯度下降算法。





