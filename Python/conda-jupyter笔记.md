# conda

## environment
```bash
conda create -n [venvName] [--clone [venv_source]] python=3.11
conda env list
conda remove -n [venvName] --all
conda env export > environment.yml # 备份环境
conda env create -f environment.yaml # 导入环境

conda activate [venvName]
conda deactivate
```
## packages
```bash
conda --version
conda update numpy
conda clean -a # 清除多余的包

conda list [-e > requirements.txt]
conda search numpy # search versions
conda install numpy==1.14.5 [--channel URL] [--use-local path] [--file requirements.txt]
conda remove numpy

pip --version
pip install -U pip
pip list | pip freeze > requirements.txt
pip install --upgrade numpy | pip install ~/Downloads/a.whl
pip install [-r requirements.txt] [numpy -i https://pypi.tuna.tsinghua.edu.cn/simple]
pip uninstall numpy
pip show numpy # show info
```

## channel settings
```bash
conda info # 详细信息
conda config # 生成.condarc
conda config --get channels # 查看通道和优先级
conda clean -i

ssl_verify: true
show_channel_urls: true
proxy_servers:
  http: http://127.0.0.1:7890
  https: http://127.0.0.1:7890
```

# jupyter notebook
edit: `enter`/`esc`
compile: `shift+Enter`/`Ctrl+Enter`
place cells:`b`/`a`
delete: `dd`
code/markdown: `y`/`m`
find: `f`   copy/cut/paste:`c`/`x`/`v`  undo:`z`
line number:`l`

tooltip:`shift+Tab`
indent/dedent:`Ctrl+[`/`Ctrl+]`
delete words:`Ctrl+backspace`/`Ctrl+delete`
`%` magic functions 模拟命令行

```py
%matplotlib inline/notebook/wiget # 每个单元格后自动补plt.show() 

import IPython.display as ipd
ipd.Audio(waveform.numpy(), rate=sample_rate)

```
