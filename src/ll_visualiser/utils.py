
import pyvista as pv


def visualise_meshes(p, mesh_files):
    """
    p: pv.Plotter object.
    mesh_files: List of mesh files.
    """
    meshes = []
    for file in mesh_files:
        meshes.append(pv.read(file))

    # TODO: This array is used for things like associated check-boxes.
    bones_mesh_actor_arr = []
    for mesh in meshes:
        bones_mesh_actor_arr.append(p.add_mesh(mesh, color='white', show_edges=False, opacity=0.99))


def visualise_landmarks(p, landmarks_labels, landmarks_points, landmark_filtered_labels):
    """
    p: pv.Plotter object.
    landmarks_points: List of landmark coordinates.
    landmarks_labels: List of landmark labels.
    landmark_filtered_labels: List of landmark labels to filter.
    """
    label_text_color = 'white'

    plot_landmarks_lbls, plot_landmarks_points, ll_meshes, sphere_meshes = process_landmarks(
        landmarks_labels, landmarks_points, landmark_filtered_labels)

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


def process_landmarks(landmarks_labels, landmarks_points, landmark_filtered_labels):
    plot_landmarks_lbls = []
    plot_landmarks_points = []
    ll_meshes = []
    sphere_meshes = []
    for i, lbl in enumerate(landmark_filtered_labels):
        try:
            idx = landmarks_labels.index(lbl)
            pnt = landmarks_points[idx]
            end_pnt = pnt.copy()
            if "right" in lbl:
                end_pnt[1] += (i*3) + 20
                end_pnt[2] += 150
            else:
                end_pnt[1] += (i*3) + 20
                end_pnt[2] -= 150
            ll_meshes.append(pv.Line(pnt, end_pnt))
            sphere_meshes.append(pv.Sphere(radius=3, center=pnt))
            plot_landmarks_lbls.append(lbl)
            plot_landmarks_points.append(end_pnt) #pnt
        finally:
            continue

    return plot_landmarks_lbls, plot_landmarks_points, ll_meshes, sphere_meshes
