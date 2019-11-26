import easydev
import os
import tempfile
import subprocess
import sys


sequana_path = easydev.get_package_location('sequana_demultiplex')
sharedir = os.sep.join([sequana_path , "sequana", 'data'])


def test_help():
    cmd = """sequana_pipelines_demultiplex --help"""
    subprocess.call(cmd.split())

def test_standalone_subprocess(tmp_path):
    directory = tmp_path / "test"
    directory.mkdir()

    with tempfile.TemporaryDirectory() as directory:
        cmd = """sequana_pipelines_demultiplex --bcl-directory {} """
        cmd += """--run-mode local --working-directory {} --force"""
        cmd = cmd.format(sharedir, directory)
        subprocess.call(cmd.split())


def test_standalone_script(tmp_path):
    directory = tmp_path / "test"
    directory.mkdir()
    import sequana_pipelines.demultiplex.main as m
    sys.argv = ["test", "--bcl-directory", sharedir, "--run-mode", "local",
          "--working-directory", str(directory), "--force"]
    m.main()