import sys
import venv
import subprocess
from shutil import rmtree
from tempfile import mkdtemp

tmp_dir = mkdtemp()
venv.create(tmp_dir, with_pip=True)

pip_path = tmp_dir + "/bin/pip"
python_path = tmp_dir + "/bin/python"

subprocess.run([pip_path, "install", "pyfiglet"], 
                stdout = subprocess.DEVNULL, 
                stderr = subprocess.DEVNULL)
subprocess.run([python_path, "-m", "figdate", *sys.argv[1:]])

rmtree(tmp_dir)
