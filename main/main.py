from flask import Flask, make_response, request, send_file
from flask import jsonify

import main.task_s.task0 as task0
import main.configure
import main.machine.process_lite as p_lite
import main.machine.md_heavy as p_md_hvy
import main.utils.simple_mnge_files as dummy_sys_file

flask_app = Flask(__name__)

flask_app.config.from_object('main.configure.Development_Config')
#  Creating celery Instance
celery_instance = task0.make_celery(flask_app)


""" Get the petition with the json attached for process the request """


@flask_app.route('/start_work', methods=['POST'])
def api():
    data, msg, err = get_data()
    if err:
        return make_response(msg, err)
    # From we doing some insteresting stuffs
    call_task(data)
    return make_response('Chido', 200)


@flask_app.route('/mkdir_usr', methods=['POST'])
def crte_user():
    """
    Create the user directory with all its nested directories.


    Args:
        JSON trhough post request
        Example:
        {
            "user_mail":"myuser@mail.com,
            "psedo_pth:["Dynamic","magic_dir1"]
        }
        The json keys:
            user_mail: Mail user is the root directory name.
            psedo_pth: Is all the path of the nested
            directories from root directory.
    Returns:
        VOID
    """
    data, msg, err = get_data()
    if err:
        return make_response(msg, err)    
    usr_tg = data['user_mail']
    dummy_sys_file.crt_dir_user(usr_tg)
    return make_response('User correctly created', 200)


@flask_app.route('/ls_dir', methods=['POST'])
def get_directory_content():
    """
    Get the content of a directory

    Args:
        JSON trhough post request
        Example:
        {
            "user_mail":"myuser@mail.com,
            "psedo_pth:["Dynamic","magic_dir1"]
        }
        The json keys:
            user_mail: Mail user is the root directory name.
            psedo_pth: Is all the path of the nested
            directories from root directory.
    Returns:
        VOID
    """
    data, msg, err = get_data()
    if err:
        return make_response(msg, err)
    pth = data['user_mail']
    dirs = data['psedo_pth']
    for dr in dirs:
        pth = pth + '/' + dr
    _var = dummy_sys_file.ls_pth_dir(pth)
    return jsonify(_var)


@flask_app.route('/get_file', methods=['POST'])
def download_file():
    """
    Download a file from host

    Args:
        JSON trhough post request
        Example:
        {
            "user_mail":"myuser@mail.com,
            "psedo_pth:["Dynamic","magic_dir1"]
        }
        The json keys:
            user_mail: Mail user is the root directory name.
            psedo_pth: Is all the path of the nested
            directories from root directory.
    Returns:
        VOID
    """
    data, msg, err = get_data()
    if err:
        return make_response(msg, err)
    pth = data['user_mail']
    fle_nm = data['fle_name']
    dirs = data['psedo_pth']
    for dr in dirs:
        pth = pth + '/' + dr
    pth = pth + '/' + fle_nm
    pth = dummy_sys_file.get_fll_pth(pth)
    return send_file(pth, attachment_filename=fle_nm)
    

def get_data():
    try:
        try:
            data = request.json
            print(data)
        except:
            raise ValueError
        if data is None:
            raise ValueError
    except ValueError:
        print('Error 1: Error data (bad request)')
        return None, 'bad request', 400
    return data, None, None


def call_task(input):
    id_prog = input['id_process']
    fv = input['frac_vol']
    usr = input['user_mail']
    
    if id_prog == 0:
        exe_hrdsphere.delay(fv, usr)
    if id_prog == 1:
        it = input['ini_temp']
        exe_softsphere.delay(fv, it, usr)
    if id_prog == 2:
        it = input['ini_temp']
        exe_yuk_hs.delay(fv, it, usr)        
    if id_prog == 3:
        exe_dyn_mdl.delay(fv, usr)


"""Tasks implemented in Celery."""


@celery_instance.task
def exe_hrdsphere(frac_vol, user):    
    p_lite.exe_hard_sphere(frac_vol, user)


@celery_instance.task
def exe_softsphere(frac_vol, init, user):
    p_lite.exe_soft_sphere(frac_vol, init, user)


@celery_instance.task
def exe_yuk_hs(frac_vol, init, user):
    p_lite.exe_yukawa_hs(frac_vol, init, user)


@celery_instance.task
def exe_dyn_mdl(frac_vol, user):
    p_md_hvy.exe_dyn_mdl(frac_vol, user)
