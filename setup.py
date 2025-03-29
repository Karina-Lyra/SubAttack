from cx_Freeze import setup, Executable




executables = [Executable("main.py")]

setup(
    name="SubAttack",
    version="1.0",
    description="Sub Attack app",
    options={"buid_exe": {"packeges": ["pygame"]}},
    executables=executables
)
