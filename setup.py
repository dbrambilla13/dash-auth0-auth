import setuptools

setuptools.setup(
    name='dash-auth0-oauth',
    version='0.1.3',
    author='Daniele Brambilla',
    author_email='daniele.bram@gmail.com',
    description='Authenticate to Dash app using Auth0',
    long_description=open('README.md', 'rt').read().strip(),
    long_description_content_type='text/markdown',
    url='https://github.com/dbrambilla13/dash-auth0-auth',
    packages=['dash_auth0_oauth'],
    install_requires=[
        'dash>=2.1.0',
        'Flask>=2.0.2',
        'authlib>=0.15.5',
        'requests>=2.27.1'
    ],
    python_requires='>=3.8',
    license='MIT',
)
