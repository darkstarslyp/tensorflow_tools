# coding:utf-8

import tensorflow as tf
import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-model",help='Input model path',default="")
parser.add_argument("-console",help='Set -console y os yes plain text will output console ',default='y')


def main():
    args = parser.parse_args()
    model_path = args.model
    console = args.console

    if not model_path or not os.path.exists(model_path) or not os.path.isfile(model_path):
        print "Not a file or file not exists!"
        exit(0)

    if console == "y" or console == "yes":
        pass
    else:
        back_stdout = sys.stdout
        file_name = str(model_path).split(os.sep)[-1]+".txt"
        log_file = open('./build/'+os.sep+file_name,"w")
        sys.stdout = log_file

    with tf.gfile.FastGFile(model_path,"rb") as pb_file:
        graph = tf.GraphDef()
        graph.ParseFromString(pb_file.read())
        nodes =  graph.node
        op_array = []
        for node in nodes:
            op_array.append(node.op)

        real_op_array = list(set(op_array))
        print("Op total count ",len(op_array),"Op real count",len(real_op_array))
        print(real_op_array)


if __name__ == "__main__":
    main()
