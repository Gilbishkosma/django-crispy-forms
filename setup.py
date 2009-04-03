from setuptools import setup, find_packages
 
version = '0.3'
 
LONG_DESCRIPTION = """
=====================================
django-uni-form (Django Uni-Form)
=====================================

[http://djangoproject.com Django] forms are easily rendered as tables,
paragraphs, and unordered lists. However, elegantly rendered div based forms
is something you have to do by hand. The purpose of this application is to
provide a simple tag and/or filter that lets you quickly render forms in a div
format.

[http://sprawsm.com/uni-form Uni-form]  has been selected as the base model
for the design of the forms.


Using django-uni-form
========================
1. Install as uni_form in your Django apps directory.
2. Copy the site_media files in uni_form to your project site_media directory.
    uni-form-generic.css
    uni-form.css
    uni-form.jquery.js
3. Add 'uni_form' to INSTALLED_APPS in settings.py.
4. Add '{% load uni_form %}' to the template that calls your form.
5. Append your form call with the as_uni_form filter:

    {{ my_form|as_uni_form }}

6. Add the class of 'uniForm' to your form. Example:

    <form action="" method="post" class="uniForm"

"""
 
setup(
    name='django-uni-form',
    version=version,
    description="django-uni-form",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='forms,django',
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/django-uni-form/tree/master',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
    setup_requires=['setuptools_git'],
)