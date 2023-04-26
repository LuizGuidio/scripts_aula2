#!/usr/bin/env python3
import pwd

# LISTA TODOS OS USUÁRIOS DO SISTEMA
for user in pwd.getpwall():
    print(user.pw_name)