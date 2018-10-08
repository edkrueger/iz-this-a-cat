import os
import shutil

path_to_train_data = os.path.join("unorganized_data", "train")

def organize_train_data(in_dir, out_dir):
    
    filenames = os.listdir(in_dir)
    
    try:
        os.mkdir(out_dir)
    except:
        pass

    for filename in filenames:

        label = filename.split(".")[0]

        try:
            os.mkdir(os.path.join(out_dir, label))
        except:
            pass

        path_to_image = os.path.join(in_dir, filename)
        
        shutil.copy(path_to_image, os.path.join(out_dir, label, filename))

organize_train_data(path_to_train_data, "data")