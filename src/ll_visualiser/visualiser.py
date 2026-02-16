
from ll_visualiser.utils import visualise_meshes, visualise_landmarks, get_files_by_extension, load_landmarks


def visualise_model(plotter, model_directory, left_predicted_landmark_file, right_predicted_landmark_file):
    mesh_files = get_files_by_extension(model_directory, ['.ply', '.stl'])
    left_landmarks = load_landmarks(left_predicted_landmark_file)
    right_landmarks = load_landmarks(right_predicted_landmark_file)

    visualise_meshes(plotter, mesh_files)
    visualise_landmarks(plotter, left_landmarks, 'left')
    visualise_landmarks(plotter, right_landmarks, 'right')

    # Set initial view to frontal view.
    plotter.view_zy(negative=True)
    plotter.add_axes(labels_off=False)
