import tensorflow as tf
import os
from tensorflow.python.platform import gfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-model",help="Input model path",default="")

def main():
    args = parser.parse_args()
    model_path = args.model
    if not os.path.exists(model_path) or not os.path.isfile(model_path):
        print "Error model path!!!"
        exit()
    output_dir = "build"+os.sep+os.path.basename(model_path).split(".")[0]
    with tf.Session() as sess:
        model_filename =model_path
        with gfile.FastGFile(model_filename, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def)
        train_writer = tf.summary.FileWriter(output_dir)
        train_writer.add_graph(sess.graph)
        os.system("tensorboard --logdir "+output_dir)

if __name__=="__main__":
    main()
