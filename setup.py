from distutils.core import setup, Extension
import numpy.distutils.misc_util

module1 = Extension('spinumpy', sources = ['spi.c'])

setup (
    name = 'SPI-NumPy',
    author='Max Scheel',
    url='https://github.com/maxscheel/SPI-NumPy',
    download_url='https://github.com/maxscheel/SPI-NumPy/archive/master.zip',
    version = '1.0',
    description = 'SPI-NumPy: Hardware SPI as a C Extension for Python with NumPy',
    license='GPL-v2',
    platforms=['Linux'],
    include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
    ext_modules = [module1]
)
