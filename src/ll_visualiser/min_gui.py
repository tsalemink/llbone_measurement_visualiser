import os

from ll_visualiser.visualiser import visualise_model


model_directory = os.path.join('..', '..', 'test', 'asm_test')
left_original_landmark_file = os.path.join(model_directory, 'orignial_lms_left.txt')
right_original_landmark_file = os.path.join(model_directory, 'orignial_lms_left.txt')
left_predicted_landmark_file = os.path.join(model_directory, 'predicted_lms_left.txt')
right_predicted_landmark_file = os.path.join(model_directory, 'predicted_lms_right.txt')


if __name__ == "__main__":
    p = visualise_model(model_directory, left_predicted_landmark_file, right_predicted_landmark_file)
    p.show(interactive=True, auto_close=False)
