FROM python:{{ cookiecutter.project_python_version }}-bullseye
RUN mkdir /config
COPY setup.py /
COPY bin/ bin/
COPY {{ cookiecutter.project_slug | replace('-', '_') }}_files /{{ cookiecutter.project_slug | replace('-', '_') }}_files
COPY {{ cookiecutter.project_slug | replace('-', '_') }}_rust_files /{{ cookiecutter.project_slug | replace('-', '_') }}_rust_files
COPY /config/example_secret_config.json /config
COPY requirements.txt /

ENV PIP_CONFIG_FILE=/run/secrets/pipconf

RUN --mount=type=secret,id=pipconf pip install .
FROM python:{{ cookiecutter.project_python_version }}-slim-bullseye

RUN apt update && apt install rustc sudo -y
RUN cargo build --release

COPY --from=0 /usr/local/lib/python{{ cookiecutter.project_python_version }}/site-packages /usr/local/lib/python{{ cookiecutter.project_python_version }}/site-packages/
COPY --from=0 /bin/{{ cookiecutter.project_slug | replace('-', '_') }} /usr/local/bin/{{ cookiecutter.project_slug | replace('-', '_') }}

CMD ["{{ cookiecutter.project_slug | replace('-', '_') }}"]