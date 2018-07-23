from setuptools import setup

setup(name='MAX7219',
      version='0.1',
      description='MAX7219',
      url='http://github.com/arno06/MAX7219',
      author='Arnaud NICOLAS',
      author_email='arno06@gmail.com',
      license='MIT',
      packages=['max7219'],
      install_requires=[
          'spidev',
      ],
      zip_safe=False)