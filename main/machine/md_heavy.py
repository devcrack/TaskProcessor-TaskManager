import os
import subprocess as sbp
import main.utils.simple_mnge_files as dummy_sys_file
import main.utils.date_time as time


home = os.path.expanduser('~')
prg_dir = '/core_programs//NSCGLE_Theory'
prg_path = home + prg_dir
""" directory where user files are stored"""
fles_dir = home + '/hipcc_data/'


def exe_dyn_mdl(fv, usr):
    """
    Execute the program of dynamic module


    Args:
        frac_vol (float):Volumen Fraction for do the calculates.

        Returns:
            void:nothing :p
    """

    exe = os.chdir(prg_path + '/dynamic_mdl-0.1')     
    exe = os.getcwd()    
    pcs = sbp.Popen([exe + '/a.out', str(fv)], stdout=sbp.PIPE, stderr=sbp.PIPE)
    out, error = pcs.communicate()
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())     
    if not pcs.poll():
        print("Dynamic Module execute finish")
    p_nme = 'Dynamic'
    dest_pth = fles_dir + usr + '/' + p_nme
    dest_pth = dest_pth + '/' + time.get_date_time_hm()
    dummy_sys_file.crt_dir(dest_pth)
    """Creating directory for program execution"""

    """Names of the generated files"""
    fle_name1 = 'sk'
    fle_name2 = 'f_self'
    fle_name3 = 'coefficient'
    """full path of the outputs of program"""
    out_fle1 = exe + '/' + 'sk.dat'
    out_fle2 = exe + '/' + 'fself.dat'
    out_fle3 = exe + '/' + 'coeficiente.dat'    
    dummy_sys_file.cpy_file_to_pth_dir(out_fle1, dest_pth, fle_name1)
    dummy_sys_file.cpy_file_to_pth_dir(out_fle2, dest_pth, fle_name2)
    dummy_sys_file.cpy_file_to_pth_dir(out_fle3, dest_pth, fle_name3)

if __name__ == "__main__":
    exe_dyn_mdl(0.5, 'ubaman')