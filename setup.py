from setuptools import setup,find_packages
import os
def get_source_files():
    for dirname, _, files in os.walk('chunky'):
        for filename in files:
            if not filename.endswith('.pyc'):
                yield os.path.join('/'.join(dirname.split('/')[1:]), filename)


setup(
    name='django-chunky',
    version='0.1.1',
    description='Editable content chunks for Django',
    author='Chris Pitzer, Jeff Schwaber, LoFi Art',
    author_email='freyley@gmail.com',
    url='',
    packages=find_packages(),
    #include_package_data=True,
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
    package_data = { 'chunky' : list(get_source_files()) }
        

)
