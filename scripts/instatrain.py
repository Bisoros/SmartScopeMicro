import os, shutil, sys, argparse

def instatrain(name, classes):
    # check type of parameters
    if not (type(name) == str and type(classes) == tuple):
        raise TypeError
    if len(classes) < 2:
        raise IndexError

    # download image data for each class
    for item in classes:
        os.system('python3 scripts/google_images_download.py -o=tf_files/training_data -f=jpg -k=' + str(item))

    # train the cnn
    os.system('python3 -m scripts/retrain --bottleneck_dir=tf_files/bottlenecks  --image_dir=tf_files/training_data  --output_graph=tf_files/'
              + name + '.pb --output_labels=tf_files/' + name + '.txt')

    # delete data
    shutil.rmtree('tf_files/training_data')

#checks if label file exists
def check_file(filename):
    #print (os.path.abspath('./tf_files/' + filename.replace('.pb', '.txt')))
    return os.path.isfile('./tf_files/' + filename.replace('.pb', '.txt'))

# create list with all weights
def weight_names():
    ret = []

    for filename in os.listdir('tf_files'):
        if filename.endswith('.pb') and check_file(filename):
            ret.append(filename.replace('.pb', ''))
    print(ret)
    return ret


if __name__ == '__main__':
    # parser set up
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', help = 'name of the resulted weights', type = str, required = True)
    parser.add_argument('-c', '--classes', help = 'classes separated by spaces', type = str, required = True)
    args = parser.parse_args()

    classes = tuple(args.classes.split())
    instatrain(args.name, classes)
