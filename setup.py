from setuptools import setup, Command
import subprocess


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @staticmethod
    def run():
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)


setup(
    name='Flask-Storage',
    version='0.0.1',
    url='https://github.com/SailerNote/flask-storage',
    license='MIT',
    author='Yansy',
    author_email='konsta.vesterinen@gmail.com',
    description='Various file storage backends for Flask apps.',
    long_description=
        open('README.rst').read() + '\n\n' +
        open('CHANGES.rst').read(),
    packages=['flask_storage'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=1.1.1'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules']
)
