set -euxo pipefail

release=$RELEASE

cd gensim
git fetch origin
git checkout "$release"
# git pull

cd ..
git commit gensim -m "update gensim submodule to point to tag $release"
