import lldb
import os

def cmd(debugger, command, result, internal_dict):
    os.system(command)

def ls(debugger, command, result, internal_dict):
    os.system("ls " + command)

def pwd(debugger, command, result, internal_dict):
    os.system("pwd")

def cd(debugger, command, result, internal_dict):
    os.chdir(command)

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f libbonus.cmd cmd')
    debugger.HandleCommand('command script add -f libbonus.ls ls')
    debugger.HandleCommand('command script add -f libbonus.pwd pwd')
    debugger.HandleCommand('command script add -f libbonus.cd cd')
