from setuptools import setup, find_packages  
  
setup(  
    name = "Wechat-AI-Robot",  
    version = "1.0",  
    keywords = ("wechat", "ai","robot"),  
    description = "Wechat robot",  
    long_description = "This scrip is used for fun, you can set up your wechat robot automaticlly thinking and reply",  
    license = "MIT Licence",  
    url = "https://github.com/E0han",  
    author = "0han",  
    author_email = "0han@protonmail.com",   
    packages = find_packages(),  
    include_package_data = True,  
    platforms = "MacOS",  
    install_requires = [
        'requests>=2.18.3',
        'itchat>=1.3.9'
    ],
    scripts = [],  
    entry_points = {  
    'console_scripts': [  
    'start = robot27:main'  
    ]  
    }  
    )  