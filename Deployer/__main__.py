import os
import subprocess
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


def redeploy_application():
    print_current_step("UNDEPLOYING OLDER VERSION:")
    run_command(UNDEPLOY)

    print_current_step("DEPLOYING NEW VERSION:")
    run_command(DEPLOY)


def move_to_admin():
    print_current_step("MOVING TO GLASSFISH FOLDER:")
    os.chdir(ADMIN_LOCATION)


if __name__ == "__main__":
    move_to_admin()
    restart_domain()
    redeploy_application()

