from cx_Freeze import setup, Executable

setup(
    name="Calculator",
    version="1.0.1",
    options={"build_exe": {
        'packages': ["tkinter"],
        'include_files': ['Images/calculator.png', 'Images/calculator.ico'],
        'include_msvcr': True,
    }},
    executables=[Executable("main.pyw", base='Win32GUI',
                            icon='Images/calculator.ico',
                            target_name='Calculator',
                            shortcutName='Calculator',
                            shortcutDir='DesktopFolder')]
)

# python setup.py bdist_msi
