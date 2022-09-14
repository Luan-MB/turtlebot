from setuptools import setup

package_name = 'turtlebot_teste'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luan',
    maintainer_email='lumb19@inf.ufpr.br',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtlebot = turtlebot_teste.turtlebot:main',
            'talker = turtlebot_teste.publisher:main',
            'listener = turtlebot_teste.subscriber:main',
            'laser = turtlebot_teste.laser:main',
            'movimenta = turtlebot_teste.movimenta:main',
        ],
    },
)
