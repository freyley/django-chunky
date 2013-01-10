from setuptools import setup
import subprocess
import os.path

setup(
    name='django-chunky',
    version='0.1.0',
    description='Editable content chunks for Django',
    author='Chris Pitzer, Jeff Schwaber, LoFi Art',
    author_email='freyley@gmail.com',
    url='',
    packages=['chunky'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    #test_suite='tests.runtests.runtests',
    package_data={
        'chunky': [
            '*.py',
            'templates/*.html',
            'templatetags/*.py',
            'static/*.js',
            'static/ckeditor/*',
            'static/ckeditor/*/*',
            'static/ckeditor/*/*/*',
            'static/ckeditor/*/*/*/*',
            'static/ckeditor/*/*/*/*/*',
            'static/js/*.js',
            'static/css/*.css',
            'migrations/*.py',
        ]
    },
)
