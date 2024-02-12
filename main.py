import os
import shutil


path = 'C:\\Users\\wojci\\Downloads\\'
video_extentions = ['mp4', 'avi', 'mkv', 'mov', 'wmv']
text_extentions = ['docx', 'rtf', 'doc', 'odt', 'txt']
exe_extentions = ['exe', 'app', 'jar', 'rpm', 'deb', 'dmg']
picture_extentions = ['jpg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'svg']
zip_extentions = ['zip', 'rar', '7z', 'tgz', 'gz', 'tbz', 'xz', 'bz2']


def print_hi(name):
    print(f'Hi, {name}')

def create_dir_for_pdf():
    directory = 'C:\\Users\\wojci\\OneDrive\\Pulpit\\pobrane_pdf'
    os.makedirs(directory, exist_ok=True)
    return directory

def create_dir_for_video():
    directory = 'C:\\Users\\wojci\\OneDrive\\Pulpit\\pobrane_video'
    os.makedirs(directory, exist_ok=True)
    return directory

def create_dir_for_text():
    directory = 'C:\\Users\\wojci\\OneDrive\\Pulpit\\pobrane_text'
    os.makedirs(directory, exist_ok=True)
    return directory

def create_dir_for_pictures():
    directory = 'C:\\Users\\wojci\\OneDrive\\Pulpit\\pobrane_pictures'
    os.makedirs(directory, exist_ok=True)
    return directory

def create_dir_for_zip():
    directory = 'C:\\Users\\wojci\\OneDrive\\Pulpit\\pobrane_zip'
    os.makedirs(directory, exist_ok=True)
    return directory

def create_dir_for_exe():
    directory = 'C:\\Users\\wojci\\OneDrive\\Pulpit\\pobrane_exe'
    os.makedirs(directory, exist_ok=True)
    return directory

def create_dir_for_others():
    directory = 'C:\\Users\\wojci\\OneDrive\\Pulpit\\inne'
    os.makedirs(directory, exist_ok=True)
    return directory

def take_files_from_download():
    file_name_list = []
    file_name_dict = {}
    downloads = os.listdir(path)

    i = 0
    for file in downloads:
        file_name_list.append(file)
        file_name_dict[file] = i + 1

    return file_name_list

def organization():
    list_of_files = take_files_from_download()

    others_path = create_dir_for_others()
    pdf_path = create_dir_for_pdf()
    exe_path = create_dir_for_exe()
    picture_patrh = create_dir_for_pictures()
    zip_path = create_dir_for_zip()
    text_path = create_dir_for_text()
    video_path = create_dir_for_video()

    for file in list_of_files:
        x = file.split('.')
        if x[-1].lower() == 'pdf':
            shutil.move((path + file), pdf_path)

        elif x[-1].lower() in video_extentions:
            shutil.move((path + file), video_path)

        elif x[-1].lower() in text_extentions:
            shutil.move((path + file), text_path)

        elif x[-1].lower() in zip_extentions:
            shutil.move((path + file), zip_path)

        elif x[-1].lower() in exe_extentions:
            shutil.move((path + file), exe_path)

        elif x[-1].lower() in picture_extentions:
            shutil.move((path + file), picture_patrh)
        
        else:
            shutil.move((path + file), others_path)




if __name__ == '__main__':
    print_hi('PyCharm')
    organization()


