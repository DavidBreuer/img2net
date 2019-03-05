from setuptools import setup

setup(name='img2net',
      version='0.1',
      description='Automated network-based analysis of imaged phenotypes',
      author='David Breuer <david.breuer@posteo.de>',
      url='http://mathbiol.mpimp-golm.mpg.de/img2net/index.html',
      packages=['img2net'],
      include_package_data=True,
      scripts=[
          'bin/run_img2net.py',
      ],
      python_requires='~=2',
)
