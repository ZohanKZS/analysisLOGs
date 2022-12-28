import PyInstaller.__main__
import pyinstaller_versionfile
from main import VER

def createBat():
    f=open('exefile.bat','w')
    f.write('pyinstaller --onefile main.py --icon "logo zohan.ico" --name "OPSURT to Kaspi KZS '+VER+'" --version-file ver.txt\n')
    f.write('pause')
    f.close()

def createEXEfile():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--windowed',
        '--icon=zohan.ico',
        '--name=Clear logs files KZS '+VER+'',
        '--version-file=ver.txt'
    ])

def createVer():


    pyinstaller_versionfile.create_versionfile(
        output_file="ver.txt",
        version=VER,
        company_name="KZS Studio",
        file_description="Это приложение для чистки логов АСБК",
        internal_name="Clear logs files",
        legal_copyright="© KZS Studio Company. All rights reserved.",
        original_filename="Clear logs files KZS "+VER+".exe",
        product_name="ClearLogs"
    )




if __name__=='__main__':
    #createBat()
    createVer()
    createEXEfile()
