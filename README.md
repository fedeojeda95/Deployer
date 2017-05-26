# Deployer

Small tool for deploying projects in Java EE developed in netbeans quickly for development in macOS. Currently,
Netbeans has a lot of trouble managing Glassfish by itself in macOS, so this script automatically starts glassfish
and deploys the project.

## Install

### Pyenv

Usage of pyenv to manage the python version and its dependencies is recommended

1. [Install pyenv](https://github.com/yyuu/pyenv-installer)
2. [Install pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)
3. Install Python (preferably, the latest version available):

    ```shell
    pyenv install 3.6.1
    ```

4. Create a virtual env for this project:

    ```shell
    pyenv virtualenv 3.6.1 deployer
    ```

5. Activate it (be sure to be in the right path):

    ```shell
    pyenv local deployer
    ```

### Global version

Just be sure to have python version 3.6.1

## Usage

* Change both the variables `GLASSFISH_LOCATION` to your glassfish instalation folder and `PROJECT_LOCATION`,
 `PROJECT_NAME` to the corresponding of your project
* To run the script, just execute `python -m Deployer` from the root


Created by [Federico Ojeda](https://github.com/fedeojeda95)