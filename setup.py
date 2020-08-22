from setuptools import setup


setup(
      name='my_custom_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/piiiiva/sklearn_transforms/',
      author='Vanderlei Munhoz',
      author_email='piiiiva@gmail.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms'
      ],
      zip_safe=False, 
      # install_requires=['scikit-learn==0.22']
)
