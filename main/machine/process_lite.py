"""Execution of simple structures factor for the alpha version of HipCC.

In this version of the development of hipcc the manage of files is made through simple tools that we 
have created but in the nearly future we pretend that all this stuffs be made with a efficient 
data base that store large files that can manage big data among others cool features.    

So for the moment we need the user name to store his file in the correct directory.
"""
import os
import subprocess as sbp
import main.utils.simple_mnge_files as dummy_sys_file

home = os.path.expanduser('~')
"""  directory of core programs""" 
prg_dir = '/core_programs/Bank_Mdls'
""" full path of core programs""" 
prg_path = home + prg_dir
""" directory where user files are stored""" 
fles_dir = home + '/hipcc_data/'


def exe_hard_sphere(frac_vol,usr):
    """ 
    Execute the program of hard sphere 


    Args:
        frac_vol (float):Volumen Fraction for do the calculates.


    Returns:
        void:nothing :p
    """

    exe = os.chdir(prg_path + '/01Sk_HSphere/Benny_Version')     
    exe = os.getcwd()
    pcs = sbp.Popen([exe + '/01Hard_Spheere', str(frac_vol)], stdout=sbp.PIPE, stderr=sbp.PIPE)
    out, error = pcs.communicate()
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
        return 0        
    if not pcs.poll():
        print("Program hard_sphere execute finish")
    """Name of the generated file"""
    fle_name = 'sk_HSpheere'
    """full path of the output of program"""
    out_fle = exe + '/data/' + fle_name + '.dat'
    p_nme = 'Hard_Sphere'
    dest_pth = fles_dir + usr + '/' + p_nme
    dummy_sys_file.cpy_file_to_pth_dir(out_fle, dest_pth, fle_name)
    


def exe_soft_sphere(fv, it, usr):
    """ 
    Execute the program of soft sphere 


    Args:
        fv (float):Volumen Fraction for do the calculates.
        it (float):Initial tempeture
    
    
    Returns:
        void:nothing :p
    """

    exe_p = os.chdir(prg_path + '/02SK_Soft_Sphere')
    exe_p = os.getcwd()
    pcs = sbp.Popen([exe_p + '/02SSphere', str(fv), str(it)], stdout=sbp.PIPE, stderr=sbp.PIPE)       
    out, error = pcs.communicate()
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
        return 0        
    if not pcs.poll():
        print("Program soft_sphere execute finish")
    """Name of the file to Copy file"""
    fle_name = 'SKsoft_sphere'
    """full path of the output of program"""
    out_fle = exe_p + '/data/' + 'sk_SSphere.dat'
    p_nme = 'Soft_Sphere'
    dest_pth = fles_dir + usr + '/' + p_nme
    dummy_sys_file.cpy_file_to_pth_dir(out_fle, dest_pth, fle_name)
    


def exe_yukawa_hs(fv, it, usr):
    """ 
    Execute the program of yukawa hard spheres


    Args:
        fv (float):Volumen Fraction for do the calculates.
        it (float):Initial tempeture


    Returns:
        void:nothing :p
    """

    exe_p = os.chdir(prg_path + '/03SK-Yukawa_HardS')
    exe_p = os.getcwd()
    pcs = sbp.Popen([exe_p + '/03Yuk', str(fv), str(it)], stdout=sbp.PIPE, stderr=sbp.PIPE)       
    out, error = pcs.communicate()
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())        
    if not pcs.poll():
        print("Program yukawa execute finish")
    fle_name = 'SK_Yuwaka'
    """full path of the output of program"""
    out_fle = exe_p + '/data/' + 'sk_MonoYuk.dat'
    p_nme = 'Yukawa'
    dest_pth = fles_dir + usr + '/' + p_nme
    dummy_sys_file.cpy_file_to_pth_dir(out_fle, dest_pth, fle_name)


if __name__ == "__main__":
    exe_yukawa_hs(0.5, 0.1, 'ubaman')
