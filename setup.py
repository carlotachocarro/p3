from setuptools import find_packages, setup

package_name = 'primer_package_prova'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nia',
    maintainer_email='tanverbus@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=[],
    entry_points={
        'console_scripts': [
            'primer_node_prova = primer_package_prova.primer_node_prova:main'
        ],
    },
)
