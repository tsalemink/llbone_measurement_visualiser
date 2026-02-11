import os
import numpy as np
import pyvista as pv

from ll_visualiser.utils import visualise_meshes, visualise_landmarks

pv.global_theme.allow_empty_mesh = True


original_landmark_files = ["orignial_lms_left.txt", "orignial_lms_right.txt"]
predicted_landmark_files = ["predicted_lms_left.txt", "predicted_lms_right.txt"]


def get_files_by_extension(directory, extension):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(extension)]


def get_files_by_names(directory, names):
    return [os.path.join(directory, name) for name in names if os.path.exists(os.path.join(directory, name))]


def load_landmarks(landmark_files):
    """
    Load and concatenate all landmark files into a single dictionary.

    Args:
        landmark_files (list): List of landmark files.

    Returns:
        dict: {landmark_name: [x, y, z], ...}
    """
    all_landmarks = {}
    for landmark_file in landmark_files:
        data = np.loadtxt(landmark_file, dtype=str)
        all_landmarks.update({row[0]: row[1:].astype(float).tolist() for row in data})
    return all_landmarks


if __name__ == "__main__":
    p = pv.Plotter(lighting='light kit', theme=pv.set_plot_theme('default'), window_size=[2560, 1440])

    model_directory = os.path.join('..', '..', 'test', 'test_data')
    ply_files = get_files_by_extension(model_directory, '.ply')
    predicted_landmark_files = get_files_by_names(model_directory, predicted_landmark_files)
    predicted_landmarks = load_landmarks(predicted_landmark_files)

    visualise_meshes(p, ply_files)
    visualise_landmarks(p, predicted_landmarks)

    # Set intial view to frontal view
    p.view_zy(negative=True)
    p.add_axes(labels_off=False)
    p.show(interactive=True, auto_close=False)
