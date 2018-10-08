#!/usr/bin/env python
# -*- coding: utf-8 -*-


# the apk place in container
APK_NAME = "/apk_shell/xhs.apk"

# stf_url address
STF_URL = "http://192.168.10.233:7100/api/v1/devices"

"""
access token of stf

STF uses OAuth 2.0 for authentication. In order to use the API,
you will first need to generate an access token. Access tokens
can be easily generated from the STF UI. Just go to the Settings
tab and generate a new access token in Keys section.
Don't forget to save this token somewhere, you will not be able to see it again.
"""
TOKEN = "41e5f0f70184464d93e787087bdc9bc6bb29076f15c943fc848d577cb1f9f65f"

STF_DELETE_URL = "http://192.168.10.233:7100/api/v1/user/devices/"

# some variables in desired_capablities
PLATFORM_NAME = 'Android'
NEW_COMMAND_TIMEOUT = 60

# come infomation needed by docker_compose.yml
APPIUM_CARTIEREJ_IMAGE = "appium_cartierej_docker:latest"
PORTS = 4723
APPIUM_CARTIEREJ_CMD = "bash /app_shell/app.sh"
APP_APK_VOLUMES = "/Users/red/apk:/apk_shell"

"""
Use device name as directory to save docker_compose.yml and app.sh
Need abs path
"""
DOCKER_COMPOSE_VOLUMES = "/Users/red/DisCartierEJ/resources/dockercomposes/"

# logs save place in local
LOCAL_LOG_DIR = "/Users/red/tmp/logs/"
APPIUM_CARTIEREJ_LOGS_VOLUMES = LOCAL_LOG_DIR + 'RANDOM:/opt/node/CartierEJ/logs'  # RANDOM为变量在生成的过程中替换

# case to run
CASE_NAME = "test_login.py"