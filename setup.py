from setuptools import setup

setup(name='explain',
      version='0.1',
      description='Explain Stuff to yourself & Save it in one place so you stop forgetting.',
      url='https://github.com/sten2lu/explain',
      author='Carsten Lueth',
    #   author_email='flyingcircus@example.com',
      license='MIT',
      packages=['explain'],
      scripts=['bin/explain'],
      zip_safe=False)