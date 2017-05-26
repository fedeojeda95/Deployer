GLASSFISH_LOCATION = "/Applications/NetBeans/glassfish-4.1.1"
ADMIN_LOCATION = f"{GLASSFISH_LOCATION}/bin"
PROJECT_LOCATION = "/Users/fedeojeda/Desktop/Facultad/ArqDeSoftware/Testing/TestingScript/dist/TestingScript.ear"
PROJECT_NAME = "TestingScript"

DEPLOY = f"./asadmin deploy {PROJECT_LOCATION}"
UNDEPLOY = f"./asadmin undeploy {PROJECT_NAME}"
START_DOMAIN = "./asadmin start-domain"
STOP_DOMAIN = "./asadmin stop-domain"
