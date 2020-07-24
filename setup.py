import sys

from skbuild import setup

def exclude_static_libraries(cmake_manifest):
    return list(filter(lambda name: not (name.endswith('.a')), cmake_manifest))

setup(
    name="gdcm",
    version="2.6.9",
    description="a minimal example package (cpp version)",
    author='The scikit-build team',
    license="Simplified BSD license,",
    # packages=['gdcm'],
    # package_dir={
        # 'gdcm': '.',
    # },
    package_data={
        "": ["*"]
    },
    long_description=open('README.txt').read(),
    cmake_args=['-DGDCM_WRAP_PYTHON:BOOL=OFF', '-DGDCM_BUILD_APPLICATIONS:BOOL=ON', '-DGDCM_BUILD_SHARED_LIBS:BOOL=OFF'],
    cmake_process_manifest_hook=exclude_static_libraries
)

