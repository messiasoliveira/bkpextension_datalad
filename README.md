# DataLad extension template

[![Build status](https://ci.appveyor.com/api/projects/status/g9von5wtpoidcecy/branch/master?svg=true)](https://ci.appveyor.com/project/mih/datalad-extension-template/branch/master) [![codecov.io](https://codecov.io/github/datalad/datalad-extension-template/coverage.svg?branch=master)](https://codecov.io/github/datalad/datalad-extension-template?branch=master) [![crippled-filesystems](https://github.com/datalad/datalad-extension-template/workflows/crippled-filesystems/badge.svg)](https://github.com/datalad/datalad-extension-template/actions?query=workflow%3Acrippled-filesystems) [![docs](https://github.com/datalad/datalad-extension-template/workflows/docs/badge.svg)](https://github.com/datalad/datalad-extension-template/actions?query=workflow%3Adocs)


This repository contains an extension template that can serve as a starting point
for implementing a [DataLad](http://datalad.org) extension. An extension can
provide any number of additional DataLad commands that are automatically
included in DataLad's command line and Python API.

For a demo, clone this repository and install the demo extension via

    pip install -e .

DataLad will now expose a new command suite with a `hello...` command.

    % datalad --help |grep -B2 -A2 hello
    *Demo DataLad command suite*

      lgpd-extension
          Short description of the command

To start implementing your own extension, [use this
template](https://github.com/datalad/datalad-extension-template/generate), and
adjust as necessary. A good approach is to

- Pick a name for the new extension.
- Look through the sources and replace `datalad_lgpdextension` with
  `datalad_<newname>` (hint: `git grep datalad_lgpdextension` should find all
  spots).
- Delete the example command implementation in `datalad_lgpdextension/__init__.py`
  by (re)moving the `lgpdextension` class.
- Implement a new command, and adjust the `command_suite` in
  `datalad_lgpdextension/__init__.py` to point to it.
- Replace `lgpd_extension` with the name of the new command in
  `datalad_lgpdextension/tests/test_register.py` to automatically test whether the
  new extension installs correctly.
- Adjust the documentation in `docs/source/index.rst`.
- Replace this README.
- Update `setup.cfg` with appropriate metadata on the new extension.

You can consider filling in the provided [.zenodo.json](.zenodo.json) file with
contributor information and [meta data](https://developers.zenodo.org/#representation)
to acknowledge contributors and describe the publication record that is created when
[you make your code citeable](https://guides.github.com/activities/citable-code/)
by archiving it using [zenodo.org](https://zenodo.org/). You may also want to
consider acknowledging contributors with the
[allcontributors bot](https://allcontributors.org/docs/en/bot/overview).
