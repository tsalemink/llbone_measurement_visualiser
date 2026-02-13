import os
import pyvista as pv

from ll_visualiser.utils import visualise_meshes, visualise_landmarks, get_files_by_extension, load_landmarks

pv.global_theme.allow_empty_mesh = True


model_directory = "D:\\Projects\\Gait\\example_models\\Models\\Meshes"
left_original_landmark_file = os.path.join(model_directory, 'orignial_lms_left.txt')
right_original_landmark_file = os.path.join(model_directory, 'orignial_lms_left.txt')
left_predicted_landmark_file = os.path.join(model_directory, 'predicted_lms_left.txt')
right_predicted_landmark_file = os.path.join(model_directory, 'predicted_lms_right.txt')


if __name__ == "__main__":
    p = pv.Plotter(lighting='light kit', theme=pv.set_plot_theme('default'), window_size=[2560, 1440])
    p.set_background('#2b2b2b')

    mesh_files = get_files_by_extension(model_directory, ['.ply', '.stl'])
    left_landmarks = load_landmarks(left_predicted_landmark_file)
    right_landmarks = load_landmarks(right_predicted_landmark_file)

    visualise_meshes(p, mesh_files)
    visualise_landmarks(p, left_landmarks, 'left')
    visualise_landmarks(p, right_landmarks, 'right')

    # Set initial view to frontal view.
    p.view_zy(negative=True)
    p.add_axes(labels_off=False)
    p.show(interactive=True, auto_close=False)
