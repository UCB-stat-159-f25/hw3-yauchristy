ENV_NAME = ligo

ENV_FILE = environment.yml

.PHONY : env html clean

env:
    # creates and configures the environment, update the environment with a provided environment.yml file
    @if conda env list | grep -q "$(ENV_NAME)"; then \
        echo "Environment exists. Updating..."; \
        conda env update -f $(ENV_FILE) -n $(ENV_NAME); \
    else \
        echo "Environment does not exist. Creating..."; \
        conda env create -f $(ENV_FILE) -n $(ENV_NAME); \
    fi


html:
    # build the html rendering of MyST site
    myst build --html

clean : 
    # clean up the figures, audio and _build folders.
    rm -rf figures/*
    rm -rf audios/*
    rm -rf _builds/*