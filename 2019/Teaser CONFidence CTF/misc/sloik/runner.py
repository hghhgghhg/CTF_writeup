import os
import shutil
import signal
import subprocess
import sys

cwd = os.getcwd()
sandbox_name = ''


def cleanup(a, b):
    global sandbox_name
    if sandbox_name != '':
        sandbox_path = os.path.join(cwd, sandbox_name)
        if os.path.exists(sandbox_path):
            shutil.rmtree(sandbox_path)


def main():
    global sandbox_name
    signal.signal(signal.SIGALRM, cleanup)
    signal.alarm(10)

    print "username: ",
    sys.stdout.flush()
    sandbox_name = sys.stdin.readline().strip()
    sandbox_path = os.path.join(cwd, "sandbox", os.path.basename(sandbox_name))

    if os.path.exists(sandbox_path):
        print "Sorry, this name is taken"
        exit(1)
    else:
        os.mkdir(sandbox_path)
        java_app = 'sloik-1.0-SNAPSHOT-jar-with-dependencies.jar'
        shutil.copy(java_app, sandbox_path)
        flag_data = open('flag.txt','r').read()
        os.chdir(sandbox_path)
        subprocess.call(['java', '-Xmx8m', '-jar', java_app], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, env={'flag': flag_data})
    os.chdir("../")
    cleanup("","")


main()
