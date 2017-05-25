import os
import subprocess

GLASSFISH_LOCATION = "/Applications/NetBeans/glassfish-4.1.1"
ADMIN_LOCATION = f"{GLASSFISH_LOCATION}/bin"
PROJECT_LOCATION = "~/Desktop/Facultad/ArqDeSoftware/Testing/TestingScript/build/TestingScript-war.war"
PROJECT_NAME = "TestingScript-war"

DEPLOY = f"./asadmin deploy {PROJECT_LOCATION}"
UNDEPLOY = f"./asadmin undeploy {PROJECT_NAME}"
START_DOMAIN = "./asadmin start-domain"
STOP_DOMAIN = "./asadmin stop-domain"


def run_command(args):
    is_list = type(args) == list
    return subprocess.run(args, shell=not is_list, check=True, stdout=subprocess.PIPE).stdout.decode('utf-8')


def print_current_step(title):
    print("")
    print("---------------------------")
    print(title)
    print("---------------------------")
    print("")


if __name__ == "__main__":
    print_current_step("MOVING TO GLASSFISH FOLDER:")
    os.chdir(ADMIN_LOCATION)

    print_current_step("STOPPING THE OLDER DOMAIN:")
    run_command(STOP_DOMAIN)

    print_current_step("STARTING DOMAIN AGAIN:")
    run_command(START_DOMAIN)

    print_current_step("UNDEPLOYING OLDER VERSION:")
    run_command(UNDEPLOY)

    print_current_step("DEPLOYING NEW VERSION:")
    run_command(DEPLOY)
