import os
import re

release = os.environ['RELEASE']


def tweak(filename, pattern, repl):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'rt') as fin:
        text = fin.read()

    tweaked_text = re.sub(pattern, repl, text, flags=re.MULTILINE)
    assert text != tweaked_text

    with open(path, 'wt') as fout:
        fout.write(tweaked_text)


tweak('.travis.yml', r'\bBUILD_COMMIT=.+$', 'BUILD_COMMIT=%s' % release)
tweak('appveyor.yml', r'\bBUILD_COMMIT: .+$', 'BUILD_COMMIT: %s' % release)
os.system('git diff | cat')

if input('commit? y / [n]\n') == 'y':
    os.system('git commit .travis.yml appveyor.yml -m "bumped commits for release %r"' % release)
