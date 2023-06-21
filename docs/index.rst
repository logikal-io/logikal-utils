.. Documentation structure
.. toctree::
    :caption: Documentation
    :hidden:

    self
    project
    docker
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

Docker
------
In case you want to use the :ref:`Docker utilities <docker:Docker>`, you need to install the
``docker`` extra:

.. code-block:: shell

    pip install logikal-utils[docker]
