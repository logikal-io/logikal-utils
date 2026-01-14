.. Documentation structure
.. toctree::
    :caption: Documentation
    :hidden:

    self
    docker
    download
    imports
    project
    testing
    development
    license

.. toctree::
    :caption: External Links
    :hidden:

    Release Notes <https://github.com/logikal-io/logikal-utils/releases>
    Issue Tracker <https://github.com/logikal-io/logikal-utils/issues>
    Source Code <https://github.com/logikal-io/logikal-utils>

Getting Started
===============
The ``logikal-utils`` library provides a set of simple common Python utilities. Installation is
very simple:

.. code-block:: shell

    pip install logikal-utils

That's it! You can now use any of the provided standard utilities.

Extras
------
docker
~~~~~~
The ``docker`` extra provides additional utilities for :ref:`managing Docker Compose services
<docker:Docker>`:

.. code-block:: shell

    pip install logikal-utils[docker]

download
~~~~~~~~
The ``download`` extra provides the :func:`~logikal_utils.download.download` function for
downloading resources from the internet.

.. code-block:: shell

    pip install logikal-utils[download]

string
~~~~~~~~
The ``string`` extra provides the :func:`~logikal_utils.string.compact` function for
formatting strings.
