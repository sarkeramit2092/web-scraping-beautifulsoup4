# Installing Python and Setting Up a Virtual Environment

## Check Python and Pip Versions

```sh
python --version
python3 --version

pip --version
pip3 --version
```

## Install JupyterLab (Version Mismatch Issue and Solution)

```sh
pip install jupyterlab
```

*Note: If you encounter a version mismatch, using an isolated sandbox (virtual environment) is recommended.*

## Navigate to Working Directory

```sh
cd Desktop/download/jbooks
pwd
```

## Download Anaconda Distribution

[Anaconda Download](https://www.anaconda.com/download)

The Anaconda Distribution is a popular open-source distribution of Python and R that includes package management and deployment tools for data science, machine learning, and AI. It comes pre-installed with many libraries and tools such as NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow, and Jupyter Notebook.

-- Key Features:
- Pre-packaged Python & R libraries for data science and ML.
- Conda package manager for easy dependency management.
- Jupyter Notebook, JupyterLab, and Spyder IDE included.
- Cross-platform support (Windows, macOS, Linux).

## Create a Virtual Environment

```sh
python3 -m venv .venv
```

*For Windows:*

```sh
python -m venv .venv
```

## Activate the Virtual Environment

```sh
source .venv/bin/activate
```

*For Windows:*

```sh
.venv\Scripts\activate
```

---

## Verify Virtual Environment Setup

```sh
(venv) python3 --version
(venv) python --version
(venv) pip --version
(venv) python -m pip install --upgrade pip
```

*Note: Changes inside the virtual environment do not affect the main system Python installation.*

## Install JupyterLab in Virtual Environment

```sh
(venv) pip install jupyterlab
(venv) jupyter lab  # Invoke Jupyter
```


