<h1 align="center">Clean Code</h1>
<h4 align="center">BDR / Vantage Challange</h4>

## Introduction

A clean way of working is the basis of productivity. Decluttering your mind helps you to focus at the task at hand, a clean desk helps you to stay organized and clean code ensures efficient collaboration. 

That is 



## ⚡ Installation

---

1. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
```sh
git clone https://dev.azure.com/AD-GSO-BeCSE/DLL_Analytics/_git/healthy_alternative
cd healthy_alternative
```

```sh
conda create --name clean_code -y python=3.9
conda activate clean_code
```
3. install package locally

requirements.txt is a *minimal* and *complete* list of packages and versions for running the package.
requirements.dev.txt contains packages used for development.
The dependencies are part of the setup.py so automatically installed, when installing the repo.
   
```sh
pip install -r requirements.txt
```



See .pre-commit-config.yaml for config.

- Use PEP8 and PEP257.
- Check style with flake8 (flake8, flake8-docstrings, pep8-naming).
- Config is in pyproject.toml




##  ⚙ Deployment

---


## 📋 Task

---
Refactor the code in ```main.py``` to a nice piece of code.
Output of main should be the printed weights containing:
- all you colleagues
- The supplies: "pan", "koekenpan", "rasp" and "kom".


## 🔔 Notes

---
Make your code as self explanetory as possible
You only have to refactor main.py.

### Future work
- Use image recognition on dirty dishes.
