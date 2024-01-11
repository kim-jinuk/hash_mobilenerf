from llff.poses.pose_utils import gen_poses
import sys
import os

data_name = sys.argv[1]
if not os.path.exists('datasets/nerf_llff_data/' + data_name + '/poses_bounds.npy'):
	print('generating .npy file.')
	gen_poses('datasets/nerf_llff_data/' + data_name, 'exhaustive_matcher')
	print('Done.')