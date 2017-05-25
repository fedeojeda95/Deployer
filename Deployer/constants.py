GLASSFISH_LOCATION = "/Applications/NetBeans/glassfish-4.1.1"
ADMIN_LOCATION = f"{GLASSFISH_LOCATION}/bin"
PROJECT_LOCATION = "~/Desktop/Facultad/ArqDeSoftware/Testing/TestingScript/build/TestingScript-war.war"
PROJECT_NAME = "TestingScript-war"

DEPLOY = f"./asadmin deploy {PROJECT_LOCATION}"
UNDEPLOY = f"./asadmin undeploy {PROJECT_NAME}"
START_DOMAIN = "./asadmin start-domain"
STOP_DOMAIN = "./asadmin stop-domain"
