from setuptools import setup

setup(
    name='dbeaver_updater',
    version='1.0',
    description='Execute sql on a remote ssh tunnel db',
    url='https://github.com/Thepowa753/dbeaver_updater_script',
    author='Federico Bregant',
    author_email='bregant.fede@gmail.com',
    license='MIT',
    packages=['dbeaver_updater'],
    entry_points={
        'console_scripts': [
            'dbeaver_updater = dbeaver_updater:run',
        ],
    },
    classifiers=[
        'Intended Audience :: Automatic update dbeaver CE',
        'Operating System :: Linux :: RedHat based :: Debian based',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
