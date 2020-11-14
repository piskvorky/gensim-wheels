#
# Ugly work-around for https://github.com/RaRe-Technologies/gensim-wheels/issues/10
#
import os.path

curr_dir = os.path.abspath(os.path.dirname(__file__))
setup_path = os.path.join(curr_dir, 'gensim', 'setup.py')

with open(setup_path, 'rt') as fin:
    script = fin.read()

script = script.replace(
    '"dataclasses; python_version < \'3.7\'",  # pre-py3.7 needs `dataclasses` backport for use of `dataclass` in doc2vec.py',
    '"dataclasses; python_version < \'3.7\'",',
)

with open(setup_path, 'wt') as fout:
    fout.write(script)
