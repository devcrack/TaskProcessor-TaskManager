from shutil import copyfile
import os
import errno
import pathlib
from main.utils import date_time


home = os.path.expanduser('~')
fles_dir = home + '/hipcc_data/'


def crt_dir(pth_dir):
    try:
        os.makedirs(pth_dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def cpy_file_to_pth_dir(src_pth_fle, dest_pth, fle_name):
    """
    Copy a file from the source path file to the user directory


    Args:
        src_pth_fle(string): source path to the file to copy.

        dest_pth(string): Destination path to the file to copy.

        fle_name(string): Name of file to copy.
    Returns:
        dest_file(string): Complete path of the file copied to the user folder.
    """
    os.chdir(dest_pth)
    dte_time = '-' + date_time.get_date_time_own_format()
    dest_file = './' + fle_name + dte_time + '.dat'
    copyfile(src_pth_fle, dest_file)
    return dest_file


def crt_dir_user(user_tag):
    """
    Create the user directory and all its nested directories.

    Args:
        user_tag(string): Is a tag for identified the directory of this user.

    Returns:
        VOID
    """

    dict_dir = ['Hard_Sphere', 'Soft_Sphere', 'Yukawa', 'Dynamic']
    fll_pth = fles_dir + user_tag
    try:
        os.makedirs(fll_pth)
        for a_directory in dict_dir:
            if not os.path.exists(fll_pth + '/' + a_directory):
                os.makedirs(fll_pth + '/' + a_directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def ls_pth_dir(pth):
    splt = pth.split('/')
    nme_dir = splt[len(splt) - 1]
    data = {}
    data[nme_dir] = []
    fll_pth = fles_dir + pth
    crrnt_dir = pathlib.Path(fll_pth)
    for _file in crrnt_dir.iterdir():
        data[nme_dir].append(_file.name)
    data[nme_dir].sort()
    return data


def get_fll_pth(psedo_pth):
    return fles_dir + psedo_pth


if __name__ == "__main__":
    crt_dir('aurelio@gmail.com')
