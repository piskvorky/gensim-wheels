# Define custom utilities
# Test for OSX with [ -n "$IS_OSX" ]

function pre_build {
    # Any stuff that you need to do before you start building the wheels
    # Runs in the root directory of this repository.
    :
}

function run_tests {
    # Runs tests on installed distribution from an empty directory
    python --version
    if [[ "$PLAT" -ne "i686" ]]; then
        pip install "tensorflow<=1.3.0" "keras>=2.0.4"  # additional deps, available only for x64
    fi
    pip freeze
    pytest -rfxEXs --durations=20 --disable-warnings --showlocals --reruns 3 --reruns-delay 1 --pyargs gensim
}
