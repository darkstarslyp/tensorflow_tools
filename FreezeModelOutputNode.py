# coding:utf-8
# 输出模型的输出节点
import tensorflow as tf
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("-model",help='Input model path',default="")


def main():
    args = parser.parse_args()
    model_path = args.model

    if not model_path or not os.path.exists(model_path) or not os.path.isfile(model_path):
        print "Not a file or file not exists!"
        exit(0)

    with tf.gfile.FastGFile(model_path,"rb") as pb_file:
        graph = tf.GraphDef()
        graph.ParseFromString(pb_file.read())
        nodes =  graph.node
        node_name_dict = {}
        for node in nodes:
            if not node_name_dict.__contains__(node.name):
                node_name_dict[node.name] = "0"
        for node in nodes:
            if node.op=="Placeholder":
                continue
            try:
                inputs = node.input
                for item_input in inputs:
                    node_name_dict[item_input] = "1"
            except:
                pass
        for key in node_name_dict.keys():
            if node_name_dict[key]=="0":
                print key,



if __name__ == "__main__":
    main()
