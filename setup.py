import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='ATS-API',  
     version='0.1',
     py_modules=['ATS-API'] ,
     author="Robin Kolk <kloknibor>",
     author_email="robinkolk@msn.com",
     description="Communication for ATS alarm",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/kloknibor/ATS-API",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )