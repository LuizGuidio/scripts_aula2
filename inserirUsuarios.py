#!/usr/bin/env python3
import subprocess
#define o nome de usuario e senha do novo usuario

new_user_name = "luiz"
new_user_password = "luiz123"
#cria o usuario no sistema linux

subprocess.run(["sudo", "useradd", new_user_name])
subprocess.run(["sudo","passwd", new_user_name], input=f"{new_user_password}\n{new_user_password}\n".encode())