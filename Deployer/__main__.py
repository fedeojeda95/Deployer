import os
import subprocess
import sys
from .constants import *


def run_command(args):
    is_list = type(args) == list
    return subprocess.run(args, shell=not is_list, check=True, stdout=subprocess.PIPE).stdout.decode('utf-8')


def print_current_step(title):
    print("")
    print("---------------------------")
    print(title)
    print("---------------------------")
    print("")


def restart_domain():
    print_current_step("STOPPING THE OLDER DOMAIN:")
    run_command(STOP_DOMAIN)

    print_current_step("STARTING DOMAIN AGAIN:")
    run_command(START_DOMAIN)


def deploy_application(first_deploy):
    if not first_deploy:
        print_current_step("UNDEPLOYING OLDER VERSION:")
        run_command(UNDEPLOY)

    print_current_step("DEPLOYING NEW VERSION:")
    run_command(DEPLOY)


def move_to_admin():
    print_current_step("MOVING TO GLASSFISH FOLDER:")
    os.chdir(ADMIN_LOCATION)


def is_only_redeploy():
    return len(sys.argv) > 1 and (sys.argv[1] == '-r' or sys.argv[1] == '--redeploy')


def is_first_deploy():
    return len(sys.argv) > 1 and (sys.argv[1] == '-f' or sys.argv[1] == '--first-deploy')


if __name__ == "__main__":
    move_to_admin()
    should_only_redeploy = is_only_redeploy()
    first_deploy = is_first_deploy()
    if not should_only_redeploy:
        restart_domain()
    deploy_application(first_deploy)

