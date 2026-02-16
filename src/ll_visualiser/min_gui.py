import os
import pyvista as pv

from ll_visualiser.visualiser import visualise_model


pv.global_theme.allow_empty_mesh = True


model_directory = os.path.join('..', '..', 'test', 'asm_test')
left_original_landmark_file = os.path.join(model_directory, 'orignial_lms_left.txt')
right_original_landmark_file = os.path.join(model_directory, 'orignial_lms_left.txt')
left_predicted_landmark_file = os.path.join(model_directory, 'predicted_lms_left.txt')
right_predicted_landmark_file = os.path.join(model_directory, 'predicted_lms_right.txt')


if __name__ == "__main__":
    plotter = pv.Plotter(lighting='light kit', theme=pv.set_plot_theme('default'), window_size=[2560, 1440])
    plotter.set_background('#2b2b2b')
    visualise_model(plotter, model_directory, left_predicted_landmark_file, right_predicted_landmark_file)
    plotter.show(interactive=True, auto_close=False)
