# Define custom utilities

function pre_build {
    # Any stuff that you need to do before you start building the wheels
    # Runs in the root directory of this repository.
    :
}

function run_tests {
    # Runs tests on installed distribution from an empty directory
    python --version
    pip freeze
    pytest -rfxEXs --durations=20 --disable-warnings --showlocals --pyargs gensim
}
