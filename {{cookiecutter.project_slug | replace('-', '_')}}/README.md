# {{ cookiecutter.project_slug | replace('-', '_') | replace('_', '\\_') }}

**{{ cookiecutter.project_description }}**

Long description of project.

## Python requirements
*Python will require these modules:*

```
example_package
```

**Tested on python {{ cookiecutter.project_python_version }}**

## File Structure

Describe the file structure

## Setup

```pip install -e .```

You may need to grant executable permissions to the bin file, to accomplish this run the following command
```chmod +x bin/{{ cookiecutter.project_slug | replace('-', '_') | replace('_','\\_') }}

Then local setup can be accomplished by running ```pip install -e .``` in the main directory

There is pre-built setup for Docker and Podman.