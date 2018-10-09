import os
import shutil
from numpy.random import seed, shuffle
from numpy import floor

path_to_labeled_data = os.path.join("unorganized_data", "train")

def organize_data(in_dir, out_dir, train_size, set_seed=1000):

	def move_images(filenames, in_dir, destination):

		for filename in filenames:

			label = filename.split(".")[0]

			os.makedirs(os.path.join(destination, label), exist_ok=True)

			path_to_image = os.path.join(in_dir, filename)

			shutil.copy(path_to_image, os.path.join(destination, label, filename))

		return

	seed(set_seed)

	filenames = os.listdir(in_dir)
	shuffle(filenames)

	train_cutoff = int(floor(len(filenames) * train_size))
	train_filenames = filenames[0:train_cutoff]
	test_filenames = filenames[train_cutoff:]

	train_dir = os.path.join(out_dir, "train")
	test_dir = os.path.join(out_dir, "test")


	os.makedirs(train_dir, exist_ok=True)
	os.makedirs(test_dir, exist_ok=True)

	move_images(train_filenames, in_dir, train_dir)
	move_images(test_filenames, in_dir, test_dir)

	return

organize_data(path_to_labeled_data, "data", .8)