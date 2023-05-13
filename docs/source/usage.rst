Usage
=====

Install package:


.. code-block:: console

   (.venv) $ pip install astrotraders

Currently, you can use API wrapper which  represented by `AstroTradersClient` class:

.. code-block:: python

    from astrotraders import AstroTradersClient
    client = AstroTradersClient.set_up(
        "token_here",
    )

After initializing client you can use API resources, for example:

.. code-block:: python

    agent = client.agents.info()
    systems = client.systems.list()
    contracts = client.contracts.list()
    factions = client.factions.list()
