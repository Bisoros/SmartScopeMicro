import os, shutil

def instatrain(name, classes):
    # check type of parameters
    if not (type(name) == str and type(classes) == tuple):
        raise TypeError

    # download image data for each class
    for item in classes:
        os.system('python google_images_download.py -o=tf_files/training_data -f=jpg -l=20 -k=' + str(item))

    os.system('python -m retrain --bottleneck_dir=tf_files/bottlenecks  --image_dir=tf_files/training_data  --output_graph=tf_files/'
              + name + '.pb --output_labels=tf_files/' + name + '.txt')

    shutil.rmtree('tf_files/training_data')

def weight_names():
    ret = []
    abspath = os.path.abspath
    for filename in os.listdir('tf_files'):
        if filename.endswith('.pb'):
            ret.append(filename.replace('.pb', ''))
    print (ret)
    return ret


if __name__ == '__main__':
    weight_names()