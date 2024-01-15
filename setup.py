import sys
from distutils.core import setup

python_version = sys.version_info[:2]
required_python_version = (3,9)
if python_version < required_python_version:
  sys.stderr.write("This tool doesn't support Python version 3.9 and below. Use the latest version of Python.")
  sys.exit(1)

with open('README.md','r',encoding = 'utf-8') as doc:
  readme = doc.read()

setup(
  name = 'asone',
  packages = ['asone'],
  version = '0.0.2',
  license='MIT',
  description = 'Facebook Scrapper',
  long_description=readme,
  long_description_content_type="text/markdown",
  author = 'Crd Dapunta Khurayra X',
  author_email = 'zaypaihtet@gmail.com',
  url = 'https://github.com/zaypaihtet/asonethod',
  keywords = ['facebook-scraper', 'facebook-parser', 'facebook-scraper-without-apikey', 'facebook-tools', 'facebook'],
  python_requires=">=3.9",
  install_requires=[
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3 :: Only'
  ],
)
