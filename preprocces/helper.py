import os


def get_absolute_path(folder_name, file_name):

    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    file_path = os.path.join(project_path, folder_name, file_name)

    return file_path




