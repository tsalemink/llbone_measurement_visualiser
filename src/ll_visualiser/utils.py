
import os
import numpy as np
import pyvista as pv


def get_files_by_extension(directory, extensions):
    return [os.path.join(directory, file) for file in os.listdir(directory)
            if any(file.endswith(extension) for extension in extensions)]


def load_landmarks(landmark_file):
    """
    Load landmarks from a file into a dictionary.

    Args:
        landmark_file (str): Path to landmark file.

    Returns:
        dict: {landmark_name: [x, y, z], ...}
    """
    data = np.loadtxt(landmark_file, dtype=str)
    return {row[0]: row[1:].astype(float).tolist() for row in data}


def visualise_meshes(p, mesh_files):
    """
    Args:
        p (pv.Plotter): PyVista Plotter object.
        mesh_files (list): List of mesh files.
    """
    meshes = []
    for file in mesh_files:
        meshes.append(pv.read(file))

    # TODO: This array is used for things like associated check-boxes.
    bones_mesh_actor_arr = []
    for mesh in meshes:
        bones_mesh_actor_arr.append(p.add_mesh(mesh, color='white', show_edges=False, opacity=0.99))


def visualise_landmarks(p, landmarks, side):
    """
    Args:
        p (pv.Plotter): PyVista Plotter object.
        landmarks (dictionary): Dictionary of landmarks.
    """
    label_text_color = 'white'

    plot_landmarks_lbls, plot_landmarks_points, ll_meshes, sphere_meshes = process_landmarks(landmarks, side)

    # landmark label lines
    for mesh in ll_meshes:
        p.add_mesh(mesh, color='green', show_edges=False, opacity=0.30, line_width=4)

    # landmark point spheres
    for mesh in sphere_meshes:
        p.add_mesh(mesh, color='red', show_edges=False, opacity=0.99)

    # Plots landmarks
    landmark_actor = p.add_point_labels(plot_landmarks_points,
                                        plot_landmarks_lbls,
                                        text_color=label_text_color,
                                        shape_color='green',
                                        background_color='green',
                                        font_size=12,
                                        always_visible=True,
                                        render_points_as_spheres=True,
                                        point_size=8, pickable=True)


def process_landmarks(landmarks, side, units='m'):
    # Define landmark size and positioning based on units.
    scale = 1000 if units == 'mm' else 1 if units == 'm' else None
    if scale is None:
        raise ValueError(f"Unsupported units: {units}. Use 'm' or 'mm'.")
    spacing = 0.003 * scale
    offset = 0.02 * scale
    z_offset = 0.15 * scale
    sphere_radius = 0.003 * scale

    plot_landmarks_labels = []
    plot_landmarks_points = []
    ll_meshes = []
    sphere_meshes = []

    for i, (label, point) in enumerate(landmarks.items()):
        end_point = point.copy()
        end_point[1] += (i * spacing) + offset
        end_point[2] += z_offset * (1 if side == "right" else -1)

        ll_meshes.append(pv.Line(point, end_point))
        sphere_meshes.append(pv.Sphere(radius=sphere_radius, center=point))
        plot_landmarks_labels.append(label)
        plot_landmarks_points.append(end_point)

    return plot_landmarks_labels, plot_landmarks_points, ll_meshes, sphere_meshes
