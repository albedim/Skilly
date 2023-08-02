import datetime
import os
import shutil
import sys


def create_project(project_name):
    os.mkdir("../" + project_name.capitalize())
    os.mkdir("../" + project_name.capitalize() + "/src")
    os.mkdir("../" + project_name.capitalize() + "/src/controller")
    os.mkdir("../" + project_name.capitalize() + "/src/service")
    os.mkdir("../" + project_name.capitalize() + "/src/model")
    os.mkdir("../" + project_name.capitalize() + "/src/model/entity")
    os.mkdir("../" + project_name.capitalize() + "/src/model/repository")
    os.mkdir("../" + project_name.capitalize() + "/skilly")
    src_path = r"./skilly//"
    dst_path = r"../"+project_name.capitalize()+"/skilly//"
    for item in os.listdir(src_path):
        s = os.path.join(src_path, item)
        d = os.path.join(dst_path, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)
    file = open("../" + project_name.capitalize() + "/src/config.py", "w")
    file.write("""database = {
    "type": "mysql",
    "host": "",
    "user": "",
    "db-name": "",
    "password": ""
}""")
    file.close()
    file = open("../" + project_name.capitalize() + "/src/app.py", "w")
    file.write("""from skilly.framework.db.src.init.skilly_init import entityInit
from skilly.framework.server.src.skilly_server import run_server

# register all the entities
# entityInit(User, Product)
entityInit()

if __name__ == '__main__':
    # run the web server
    run_server()

""")
    file.close()
    file = open("../" + project_name.capitalize() + "/src/schema.py", "w")
    file.write("""SCHEMA = [
    {
        "name": "EXAMPLE_SCHEMA_POST_REQ",
        "schema": {
            "name": str,
            "email": str
        }
    }
]""")
    file = open("../"+project_name.capitalize()+"/skilly_requirements.txt", "w")
    file.write("""install==1.3.5
mysql-client==0.0.1
mysql-connector-python==8.0.33
protobuf==3.20.3
PyJWT==2.7.0
""")
    file.close()
    file = open("../"+project_name.capitalize()+"/src/init.py", "w")
    init = open("./init.py", 'r')
    init = init.read()
    file.write(init)
    print(f"Project '{project_name}' created")


def main():

    if len(sys.argv) == 1:
        print("The correct use of this command is:\npython create_project.py <project_name>")
        return
    command = sys.argv[1]
    print("Loading...")
    create_project(command)


if __name__ == "__main__":
    main()