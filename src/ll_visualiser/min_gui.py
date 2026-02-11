import os
import numpy as np
import pyvista as pv

from ll_visualiser.utils import visualise_meshes, visualise_landmarks

pv.global_theme.allow_empty_mesh = True


def get_files_by_extension(directory, extension):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]


if __name__ == "__main__":
    p = pv.Plotter(lighting='light kit',
                   theme=pv.set_plot_theme('default'),
                   window_size=[2560, 1440])

    model_directory = os.path.join('..', '..', 'test', 'test_data')
    txt_files = get_files_by_extension(model_directory, '.txt')
    ply_files = get_files_by_extension(model_directory, '.ply')

    for f in txt_files:
        if "landmark" in f:
            if "_filtered" not in f:
                l_path = f
            else:
                lf_path = f
        if "measurements" in f:
            if "_filtered" not in f:
                m_path = f
            else:
                mf_path = f

    # load landmarks and measurements
    landmarks = np.loadtxt(l_path, dtype=object).ravel()
    measurements = np.loadtxt(m_path, dtype=object)

    landmark_filtered_labels = np.loadtxt(lf_path, dtype=str)
    measurement_filtered_labels = np.loadtxt(mf_path, dtype=str)

    measurements_labels = measurements[0].split(',')
    measurements_data = measurements[1] + measurements[2]
    measurements_data = measurements_data.split(',')

    landmarks_points = []
    landmarks_labels = []

    # row 0 is the header
    for row in landmarks[1:]:
        splits = row.split(',')
        landmarks_points.append([float(x) for x in splits[1:4]])
        landmarks_labels.append(splits[0])

    visualise_landmarks(p, landmarks_labels, landmarks_points, landmark_filtered_labels)

    visualise_meshes(p, ply_files)

    # Set intial view to frontal view
    p.view_zy(negative=True)
    p.add_axes(labels_off=False)
    p.show(interactive=True, auto_close=False)
