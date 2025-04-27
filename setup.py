from cx_Freeze import setup,Executable,sys
includefiles=['icon.ico','back_button.png','category.png','category.py','dashboard.py','employees.png','employees.py','exit.png','inventory.png','logo.png','product_category.png','products.png','products.py','sales.png','supplier.png','supplier.py','total_cat.png','total_emp.png','total_prod.png','total_sales.png','total_sup.png']
excludes=[]
#packages=['os','pyttsx3']
#includes =["pyttsx3.drivers"]
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[ 
    ("DesktopShortcut",
     "DesktopFolder",
     "Inventory Management System",
     "TARGETDIR",
     "[TARGETDIR]\dashboard.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="Inventory Management System",
    author="Yohannes Bogale",
    name="IM-System",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="dashboard.py",
            base=base,
            icon='icon.ico',
        )
    ]
)