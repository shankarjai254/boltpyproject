from setuptools import setup, find_packages

setup(
    name="sample-flask-app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask>=3.0.2",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample Flask application for Jenkins pipeline demo",
    keywords="flask,web,jenkins",
    url="https://github.com/yourusername/sample-flask-app",
    project_urls={
        "Source Code": "https://github.com/yourusername/sample-flask-app",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.8",
)