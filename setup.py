from setuptools import setup

setup(
    name='django-chunky',
    version='0.1.7',
    description='Editable content chunks for Django',
    author='Chris Pitzer, Jeff Schwaber, LoFi Art',
    author_email='freyley@gmail.com',
    url='http://github.com/freyley/django-chunky',
    packages=['chunky'],
    include_package_data=True,
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
        

)
