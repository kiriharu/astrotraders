import json
from typing import TypeVar

from astrotraders import AstroTradersClient
from astrotraders.api.schemas import (
    AgentSchema,
    PaginatedObject,
    System,
    Waypoint,
    Market,
    Shipyard,
    JumpGate,
    ContractSchema,
    AcceptContractResult,
    DeliverContractResult,
    FullfillContractResult,
    Faction,
    ShipSchema,
    PurchaseShipResult,
    ShipType,
    ShipCargo,
    ShipNav,
    Produce,
    ShipRefineResult,
    ChartShipResult,
    Cooldown,
    CreateSurveyResult,
    Survey,
    Size,
    ExtractResourcesResult,
    ShipJumpResult,
    ShipNavigateResult,
    ShipNavFlightMode,
    SellCargoResult,
    ScanSystemsResult,
    ScanWaypointsResult,
    ScanShipsResult,
    RefuelShipResult,
    PurchaseCargoResult,
    TradeSymbol
)
from astrotraders.api.utils import to_schema, ORJSONDecoder

T = TypeVar("T")


def serialize_json_to_obj(data: str, to: T) -> T:
    return to_schema(json.loads(data, cls=ORJSONDecoder), to)


def test_agents_info(api_client: AstroTradersClient):
    example = """
    {
        "data": {
            "accountId": "string",
            "symbol": "string",
            "headquarters": "string",
            "credits": 0
        }
    }
    """
    obj = serialize_json_to_obj(example, AgentSchema)

    result = api_client.agents.info()

    assert obj == result


def test_systems_list(api_client: AstroTradersClient):
    example = """
    {
      "data": [
        {
          "symbol": "string",
          "sectorSymbol": "string",
          "type": "NEUTRON_STAR",
          "x": 0,
          "y": 0,
          "waypoints": [
            {
              "symbol": "string",
              "type": "PLANET",
              "x": 0,
              "y": 0
            }
          ],
          "factions": [
            {
              "symbol": "string"
            }
          ]
        }
      ],
      "meta": {
        "total": 0,
        "page": 0,
        "limit": 0
      }
    }
    """
    obj = serialize_json_to_obj(example, PaginatedObject[System])

    result = api_client.systems.list()

    assert obj == result


def test_systems_get(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "symbol": "string",
        "sectorSymbol": "string",
        "type": "NEUTRON_STAR",
        "x": 0,
        "y": 0,
        "waypoints": [
          {
            "symbol": "string",
            "type": "PLANET",
            "x": 0,
            "y": 0
          }
        ],
        "factions": [
          {
            "symbol": "string"
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, System)

    result = api_client.systems.get("test")

    assert obj == result


def test_systems_waypoints_list(api_client: AstroTradersClient):
    example = """
    {
      "data": [
        {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0,
          "orbitals": [
            {
              "symbol": "string"
            }
          ],
          "faction": {
            "symbol": "string"
          },
          "traits": [
            {
              "symbol": "UNCHARTED",
              "name": "string",
              "description": "string"
            }
          ],
          "chart": {
            "waypointSymbol": "string",
            "submittedBy": "string",
            "submittedOn": "2019-08-24T14:15:22Z"
          }
        }
      ],
      "meta": {
        "total": 0,
        "page": 0,
        "limit": 0
      }
    }
    """
    obj = serialize_json_to_obj(example, PaginatedObject[Waypoint])

    result = api_client.systems.waypoints.list("test")

    assert obj == result


def test_systems_waypoints_get(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "symbol": "string",
        "type": "PLANET",
        "systemSymbol": "string",
        "x": 0,
        "y": 0,
        "orbitals": [
          {
            "symbol": "string"
          }
        ],
        "faction": {
          "symbol": "string"
        },
        "traits": [
          {
            "symbol": "UNCHARTED",
            "name": "string",
            "description": "string"
          }
        ],
        "chart": {
          "waypointSymbol": "string",
          "submittedBy": "string",
          "submittedOn": "2019-08-24T14:15:22Z"
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, Waypoint)

    result = api_client.systems.waypoints.get("test", "test")

    assert obj == result


def test_systems_waypoints_market(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "symbol": "string",
        "exports": [
          {
            "symbol": "PRECIOUS_STONES",
            "name": "string",
            "description": "string"
          }
        ],
        "imports": [
          {
            "symbol": "PRECIOUS_STONES",
            "name": "string",
            "description": "string"
          }
        ],
        "exchange": [
          {
            "symbol": "PRECIOUS_STONES",
            "name": "string",
            "description": "string"
          }
        ],
        "transactions": [
          {
            "waypointSymbol": "string",
            "shipSymbol": "string",
            "tradeSymbol": "string",
            "type": "PURCHASE",
            "units": 1,
            "pricePerUnit": 1,
            "totalPrice": 1,
            "timestamp": "2019-08-24T14:15:22Z"
          }
        ],
        "tradeGoods": [
          {
            "symbol": "string",
            "tradeVolume": 1,
            "supply": "SCARCE",
            "purchasePrice": 0,
            "sellPrice": 0
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, Market)

    result = api_client.systems.waypoints.market("test", "test")

    assert obj == result


def test_systems_waypoints_shipyard(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "symbol": "string",
        "shipTypes": [
          {
            "type": "SHIP_PROBE"
          }
        ],
        "transactions": [
          {
            "waypointSymbol": "string",
            "shipSymbol": "string",
            "price": 1,
            "agentSymbol": "string",
            "timestamp": "2019-08-24T14:15:22Z"
          }
        ],
        "ships": [
          {
            "type": "SHIP_PROBE",
            "name": "string",
            "description": "string",
            "purchasePrice": 0,
            "frame": {
              "symbol": "FRAME_PROBE",
              "name": "string",
              "description": "string",
              "condition": 0,
              "moduleSlots": 0,
              "mountingPoints": 0,
              "fuelCapacity": 0,
              "requirements": {
                "power": 0,
                "crew": 0,
                "slots": 0
              }
            },
            "reactor": {
              "symbol": "REACTOR_SOLAR_I",
              "name": "string",
              "description": "string",
              "condition": 0,
              "powerOutput": 1,
              "requirements": {
                "power": 0,
                "crew": 0,
                "slots": 0
              }
            },
            "engine": {
              "symbol": "ENGINE_IMPULSE_DRIVE_I",
              "name": "string",
              "description": "string",
              "condition": 0,
              "speed": 1,
              "requirements": {
                "power": 0,
                "crew": 0,
                "slots": 0
              }
            },
            "modules": [
              {
                "symbol": "MODULE_MINERAL_PROCESSOR_I",
                "capacity": 0,
                "range": 0,
                "name": "string",
                "description": "string",
                "requirements": {
                  "power": 0,
                  "crew": 0,
                  "slots": 0
                }
              }
            ],
            "mounts": [
              {
                "symbol": "MOUNT_GAS_SIPHON_I",
                "name": "string",
                "description": "string",
                "strength": 0,
                "deposits": [
                  "QUARTZ_SAND"
                ],
                "requirements": {
                  "power": 0,
                  "crew": 0,
                  "slots": 0
                }
              }
            ]
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, Shipyard)

    result = api_client.systems.waypoints.shipyard("test", "test")

    assert obj == result


def test_systems_waypoints_jump_gate(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "jumpRange": 0,
        "factionSymbol": "string",
        "connectedSystems": [
          {
            "symbol": "string",
            "sectorSymbol": "string",
            "type": "NEUTRON_STAR",
            "factionSymbol": "string",
            "x": 0,
            "y": 0,
            "distance": 0
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, JumpGate)

    result = api_client.systems.waypoints.jump_gate("test", "test")

    assert obj == result


def test_contracts_list(api_client: AstroTradersClient):
    example = """
    {
      "data": [
        {
          "id": "string",
          "factionSymbol": "string",
          "type": "PROCUREMENT",
          "terms": {
            "deadline": "2019-08-24T14:15:22Z",
            "payment": {
              "onAccepted": 0,
              "onFulfilled": 0
            },
            "deliver": [
              {
                "tradeSymbol": "string",
                "destinationSymbol": "string",
                "unitsRequired": 0,
                "unitsFulfilled": 0
              }
            ]
          },
          "accepted": false,
          "fulfilled": false,
          "expiration": "2019-08-24T14:15:22Z"
        }
      ],
      "meta": {
        "total": 0,
        "page": 0,
        "limit": 0
      }
    }
    """
    obj = serialize_json_to_obj(example, PaginatedObject[ContractSchema])

    result = api_client.contracts.list()

    assert obj == result


def test_contracts_get(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "id": "string",
        "factionSymbol": "string",
        "type": "PROCUREMENT",
        "terms": {
          "deadline": "2019-08-24T14:15:22Z",
          "payment": {
            "onAccepted": 0,
            "onFulfilled": 0
          },
          "deliver": [
            {
              "tradeSymbol": "string",
              "destinationSymbol": "string",
              "unitsRequired": 0,
              "unitsFulfilled": 0
            }
          ]
        },
        "accepted": false,
        "fulfilled": false,
        "expiration": "2019-08-24T14:15:22Z"
      }
    }
    """
    obj = serialize_json_to_obj(example, ContractSchema)

    result = api_client.contracts.get("test")

    assert obj == result


def test_contracts_accept(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "agent": {
          "accountId": "string",
          "symbol": "string",
          "headquarters": "string",
          "credits": 0
        },
        "contract": {
          "id": "string",
          "factionSymbol": "string",
          "type": "PROCUREMENT",
          "terms": {
            "deadline": "2019-08-24T14:15:22Z",
            "payment": {
              "onAccepted": 0,
              "onFulfilled": 0
            },
            "deliver": [
              {
                "tradeSymbol": "string",
                "destinationSymbol": "string",
                "unitsRequired": 0,
                "unitsFulfilled": 0
              }
            ]
          },
          "accepted": false,
          "fulfilled": false,
          "expiration": "2019-08-24T14:15:22Z"
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, AcceptContractResult)

    result = api_client.contracts.accept("test")

    assert obj == result


def test_contracts_deliver(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "contract": {
          "id": "string",
          "factionSymbol": "string",
          "type": "PROCUREMENT",
          "terms": {
            "deadline": "2019-08-24T14:15:22Z",
            "payment": {
              "onAccepted": 0,
              "onFulfilled": 0
            },
            "deliver": [
              {
                "tradeSymbol": "string",
                "destinationSymbol": "string",
                "unitsRequired": 0,
                "unitsFulfilled": 0
              }
            ]
          },
          "accepted": false,
          "fulfilled": false,
          "expiration": "2019-08-24T14:15:22Z"
        },
        "cargo": {
          "capacity": 0,
          "units": 0,
          "inventory": [
            {
              "symbol": "string",
              "name": "string",
              "description": "string",
              "units": 1
            }
          ]
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, DeliverContractResult)

    result = api_client.contracts.deliver("test", "test", "test", 1)

    assert obj == result


def test_contracts_fulfill(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "agent": {
          "accountId": "string",
          "symbol": "string",
          "headquarters": "string",
          "credits": 0
        },
        "contract": {
          "id": "string",
          "factionSymbol": "string",
          "type": "PROCUREMENT",
          "terms": {
            "deadline": "2019-08-24T14:15:22Z",
            "payment": {
              "onAccepted": 0,
              "onFulfilled": 0
            },
            "deliver": [
              {
                "tradeSymbol": "string",
                "destinationSymbol": "string",
                "unitsRequired": 0,
                "unitsFulfilled": 0
              }
            ]
          },
          "accepted": false,
          "fulfilled": false,
          "expiration": "2019-08-24T14:15:22Z"
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, FullfillContractResult)

    result = api_client.contracts.fulfill("test")

    assert obj == result


def test_factions_list(api_client: AstroTradersClient):
    example = """
    {
      "data": [
        {
          "symbol": "string",
          "name": "string",
          "description": "string",
          "headquarters": "string",
          "traits": [
            {
              "symbol": "BUREAUCRATIC",
              "name": "string",
              "description": "string"
            }
          ]
        }
      ],
      "meta": {
        "total": 0,
        "page": 0,
        "limit": 0
      }
    }
    """
    obj = serialize_json_to_obj(example, PaginatedObject[Faction])

    result = api_client.factions.list()

    assert obj == result


def test_factions_get(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "symbol": "string",
        "name": "string",
        "description": "string",
        "headquarters": "string",
        "traits": [
          {
            "symbol": "BUREAUCRATIC",
            "name": "string",
            "description": "string"
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, Faction)

    result = api_client.factions.get("test")

    assert obj == result


def test_fleet_list(api_client: AstroTradersClient):
    example = """
    {
      "data": [
        {
          "symbol": "string",
          "registration": {
            "name": "string",
            "factionSymbol": "string",
            "role": "FABRICATOR"
          },
          "nav": {
            "systemSymbol": "string",
            "waypointSymbol": "string",
            "route": {
              "destination": {
                "symbol": "string",
                "type": "PLANET",
                "systemSymbol": "string",
                "x": 0,
                "y": 0
              },
              "departure": {
                "symbol": "string",
                "type": "PLANET",
                "systemSymbol": "string",
                "x": 0,
                "y": 0
              },
              "departureTime": "2019-08-24T14:15:22Z",
              "arrival": "2019-08-24T14:15:22Z"
            },
            "status": "IN_TRANSIT",
            "flightMode": "CRUISE"
          },
          "crew": {
            "current": 0,
            "required": 0,
            "capacity": 0,
            "rotation": "STRICT",
            "morale": 0,
            "wages": 0
          },
          "frame": {
            "symbol": "FRAME_PROBE",
            "name": "string",
            "description": "string",
            "condition": 0,
            "moduleSlots": 0,
            "mountingPoints": 0,
            "fuelCapacity": 0,
            "requirements": {
              "power": 0,
              "crew": 0,
              "slots": 0
            }
          },
          "reactor": {
            "symbol": "REACTOR_SOLAR_I",
            "name": "string",
            "description": "string",
            "condition": 0,
            "powerOutput": 1,
            "requirements": {
              "power": 0,
              "crew": 0,
              "slots": 0
            }
          },
          "engine": {
            "symbol": "ENGINE_IMPULSE_DRIVE_I",
            "name": "string",
            "description": "string",
            "condition": 0,
            "speed": 1,
            "requirements": {
              "power": 0,
              "crew": 0,
              "slots": 0
            }
          },
          "modules": [
            {
              "symbol": "MODULE_MINERAL_PROCESSOR_I",
              "capacity": 0,
              "range": 0,
              "name": "string",
              "description": "string",
              "requirements": {
                "power": 0,
                "crew": 0,
                "slots": 0
              }
            }
          ],
          "mounts": [
            {
              "symbol": "MOUNT_GAS_SIPHON_I",
              "name": "string",
              "description": "string",
              "strength": 0,
              "deposits": [
                "QUARTZ_SAND"
              ],
              "requirements": {
                "power": 0,
                "crew": 0,
                "slots": 0
              }
            }
          ],
          "cargo": {
            "capacity": 0,
            "units": 0,
            "inventory": [
              {
                "symbol": "string",
                "name": "string",
                "description": "string",
                "units": 1
              }
            ]
          },
          "fuel": {
            "current": 0,
            "capacity": 0,
            "consumed": {
              "amount": 0,
              "timestamp": "2019-08-24T14:15:22Z"
            }
          }
        }
      ],
      "meta": {
        "total": 0,
        "page": 0,
        "limit": 0
      }
    }
    """
    obj = serialize_json_to_obj(example, PaginatedObject[ShipSchema])

    result = api_client.fleet.list()

    assert obj == result


def test_fleet_purchase(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "agent": {
          "accountId": "string",
          "symbol": "string",
          "headquarters": "string",
          "credits": 0
        },
        "ship": {
          "symbol": "string",
          "registration": {
            "name": "string",
            "factionSymbol": "string",
            "role": "FABRICATOR"
          },
          "nav": {
            "systemSymbol": "string",
            "waypointSymbol": "string",
            "route": {
              "destination": {
                "symbol": "string",
                "type": "PLANET",
                "systemSymbol": "string",
                "x": 0,
                "y": 0
              },
              "departure": {
                "symbol": "string",
                "type": "PLANET",
                "systemSymbol": "string",
                "x": 0,
                "y": 0
              },
              "departureTime": "2019-08-24T14:15:22Z",
              "arrival": "2019-08-24T14:15:22Z"
            },
            "status": "IN_TRANSIT",
            "flightMode": "CRUISE"
          },
          "crew": {
            "current": 0,
            "required": 0,
            "capacity": 0,
            "rotation": "STRICT",
            "morale": 0,
            "wages": 0
          },
          "frame": {
            "symbol": "FRAME_PROBE",
            "name": "string",
            "description": "string",
            "condition": 0,
            "moduleSlots": 0,
            "mountingPoints": 0,
            "fuelCapacity": 0,
            "requirements": {
              "power": 0,
              "crew": 0,
              "slots": 0
            }
          },
          "reactor": {
            "symbol": "REACTOR_SOLAR_I",
            "name": "string",
            "description": "string",
            "condition": 0,
            "powerOutput": 1,
            "requirements": {
              "power": 0,
              "crew": 0,
              "slots": 0
            }
          },
          "engine": {
            "symbol": "ENGINE_IMPULSE_DRIVE_I",
            "name": "string",
            "description": "string",
            "condition": 0,
            "speed": 1,
            "requirements": {
              "power": 0,
              "crew": 0,
              "slots": 0
            }
          },
          "modules": [
            {
              "symbol": "MODULE_MINERAL_PROCESSOR_I",
              "capacity": 0,
              "range": 0,
              "name": "string",
              "description": "string",
              "requirements": {
                "power": 0,
                "crew": 0,
                "slots": 0
              }
            }
          ],
          "mounts": [
            {
              "symbol": "MOUNT_GAS_SIPHON_I",
              "name": "string",
              "description": "string",
              "strength": 0,
              "deposits": [
                "QUARTZ_SAND"
              ],
              "requirements": {
                "power": 0,
                "crew": 0,
                "slots": 0
              }
            }
          ],
          "cargo": {
            "capacity": 0,
            "units": 0,
            "inventory": [
              {
                "symbol": "string",
                "name": "string",
                "description": "string",
                "units": 1
              }
            ]
          },
          "fuel": {
            "current": 0,
            "capacity": 0,
            "consumed": {
              "amount": 0,
              "timestamp": "2019-08-24T14:15:22Z"
            }
          }
        },
        "transaction": {
          "waypointSymbol": "string",
          "shipSymbol": "string",
          "price": 1,
          "agentSymbol": "string",
          "timestamp": "2019-08-24T14:15:22Z"
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, PurchaseShipResult)

    result = api_client.fleet.purchase(ShipType.ship_interceptor, "test")

    assert obj == result


def test_fleet_get(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "symbol": "string",
        "registration": {
          "name": "string",
          "factionSymbol": "string",
          "role": "FABRICATOR"
        },
        "nav": {
          "systemSymbol": "string",
          "waypointSymbol": "string",
          "route": {
            "destination": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departure": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departureTime": "2019-08-24T14:15:22Z",
            "arrival": "2019-08-24T14:15:22Z"
          },
          "status": "IN_TRANSIT",
          "flightMode": "CRUISE"
        },
        "crew": {
          "current": 0,
          "required": 0,
          "capacity": 0,
          "rotation": "STRICT",
          "morale": 0,
          "wages": 0
        },
        "frame": {
          "symbol": "FRAME_PROBE",
          "name": "string",
          "description": "string",
          "condition": 0,
          "moduleSlots": 0,
          "mountingPoints": 0,
          "fuelCapacity": 0,
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        },
        "reactor": {
          "symbol": "REACTOR_SOLAR_I",
          "name": "string",
          "description": "string",
          "condition": 0,
          "powerOutput": 1,
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        },
        "engine": {
          "symbol": "ENGINE_IMPULSE_DRIVE_I",
          "name": "string",
          "description": "string",
          "condition": 0,
          "speed": 1,
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        },
        "modules": [
          {
            "symbol": "MODULE_MINERAL_PROCESSOR_I",
            "capacity": 0,
            "range": 0,
            "name": "string",
            "description": "string",
            "requirements": {
              "power": 0,
              "crew": 0,
              "slots": 0
            }
          }
        ],
        "mounts": [
          {
            "symbol": "MOUNT_GAS_SIPHON_I",
            "name": "string",
            "description": "string",
            "strength": 0,
            "deposits": [
              "QUARTZ_SAND"
            ],
            "requirements": {
              "power": 0,
              "crew": 0,
              "slots": 0
            }
          }
        ],
        "cargo": {
          "capacity": 0,
          "units": 0,
          "inventory": [
            {
              "symbol": "string",
              "name": "string",
              "description": "string",
              "units": 1
            }
          ]
        },
        "fuel": {
          "current": 0,
          "capacity": 0,
          "consumed": {
            "amount": 0,
            "timestamp": "2019-08-24T14:15:22Z"
          }
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, ShipSchema)

    result = api_client.fleet.get("test")

    assert obj == result


def test_fleet_cargo_get(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "capacity": 0,
        "units": 0,
        "inventory": [
          {
            "symbol": "string",
            "name": "string",
            "description": "string",
            "units": 1
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, ShipCargo)

    result = api_client.fleet.cargo.get("test")

    assert obj == result


def test_fleet_orbit(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "nav": {
          "systemSymbol": "string",
          "waypointSymbol": "string",
          "route": {
            "destination": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departure": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departureTime": "2019-08-24T14:15:22Z",
            "arrival": "2019-08-24T14:15:22Z"
          },
          "status": "IN_TRANSIT",
          "flightMode": "CRUISE"
        }
      }
    }
    """
    jsoned_data = json.loads(example)
    obj = ShipNav(**jsoned_data["data"]["nav"])

    result = api_client.fleet.orbit("test")

    assert obj == result


def test_fleet_refine(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "cargo": {
          "capacity": 0,
          "units": 0,
          "inventory": [
            {
              "symbol": "string",
              "name": "string",
              "description": "string",
              "units": 1
            }
          ]
        },
        "cooldown": {
          "shipSymbol": "string",
          "totalSeconds": 0,
          "remainingSeconds": 0,
          "expiration": "2019-08-24T14:15:22Z"
        },
        "produced": [
          {
            "tradeSymbol": "string",
            "units": 0
          }
        ],
        "consumed": [
          {
            "tradeSymbol": "string",
            "units": 0
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, ShipRefineResult)

    result = api_client.fleet.refine("test", Produce.fuel)

    assert obj == result


def test_fleet_chart(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "chart": {
          "waypointSymbol": "string",
          "submittedBy": "string",
          "submittedOn": "2019-08-24T14:15:22Z"
        },
        "waypoint": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0,
          "orbitals": [
            {
              "symbol": "string"
            }
          ],
          "faction": {
            "symbol": "string"
          },
          "traits": [
            {
              "symbol": "UNCHARTED",
              "name": "string",
              "description": "string"
            }
          ],
          "chart": {
            "waypointSymbol": "string",
            "submittedBy": "string",
            "submittedOn": "2019-08-24T14:15:22Z"
          }
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, ChartShipResult)

    result = api_client.fleet.chart("test")

    assert obj == result


def test_fleet_cooldown_with_cooldown(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "shipSymbol": "string",
        "totalSeconds": 0,
        "remainingSeconds": 0,
        "expiration": "2019-08-24T14:15:22Z"
      }
    }
    """
    obj = serialize_json_to_obj(example, Cooldown)

    result = api_client.fleet.cooldown("test")

    assert obj == result


def test_fleet_cooldown_with_no_cooldown(api_client: AstroTradersClient):
    example = None
    api_client._httpx_instance.headers["Prefer"] = "code=204"
    result = api_client.fleet.cooldown("test")

    assert example == result


def test_fleet_dock(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "nav": {
          "systemSymbol": "string",
          "waypointSymbol": "string",
          "route": {
            "destination": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departure": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departureTime": "2019-08-24T14:15:22Z",
            "arrival": "2019-08-24T14:15:22Z"
          },
          "status": "IN_TRANSIT",
          "flightMode": "CRUISE"
        }
      }
    }
    """
    jsoned_data = json.loads(example)
    obj = ShipNav(**jsoned_data["data"]["nav"])

    result = api_client.fleet.dock("test")

    assert obj == result


def test_fleet_survey(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "cooldown": {
          "shipSymbol": "string",
          "totalSeconds": 0,
          "remainingSeconds": 0,
          "expiration": "2019-08-24T14:15:22Z"
        },
        "surveys": [
          {
            "signature": "string",
            "symbol": "string",
            "deposits": [
              {
                "symbol": "string"
              }
            ],
            "expiration": "2019-08-24T14:15:22Z",
            "size": "SMALL"
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, CreateSurveyResult)

    result = api_client.fleet.survey("test")

    assert obj == result


def test_fleet_extract_with_survey(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "cooldown": {
          "shipSymbol": "string",
          "totalSeconds": 0,
          "remainingSeconds": 0,
          "expiration": "2019-08-24T14:15:22Z"
        },
        "extraction": {
          "shipSymbol": "string",
          "yield": {
            "symbol": "string",
            "units": 0
          }
        },
        "cargo": {
          "capacity": 0,
          "units": 0,
          "inventory": [
            {
              "symbol": "string",
              "name": "string",
              "description": "string",
              "units": 1
            }
          ]
        }
      }
    }
    """
    survey = Survey(signature="test", symbol="test", deposits=[], expiration="2019-08-24T14:15:22Z", size=Size.large)
    obj = serialize_json_to_obj(example, ExtractResourcesResult)

    result = api_client.fleet.extract("test", survey)

    assert obj == result


def test_fleet_extract_with_no_survey(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "cooldown": {
          "shipSymbol": "string",
          "totalSeconds": 0,
          "remainingSeconds": 0,
          "expiration": "2019-08-24T14:15:22Z"
        },
        "extraction": {
          "shipSymbol": "string",
          "yield": {
            "symbol": "string",
            "units": 0
          }
        },
        "cargo": {
          "capacity": 0,
          "units": 0,
          "inventory": [
            {
              "symbol": "string",
              "name": "string",
              "description": "string",
              "units": 1
            }
          ]
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, ExtractResourcesResult)

    result = api_client.fleet.extract("test")

    assert obj == result


def test_fleet_cargo_jettison(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "cargo": {
          "capacity": 0,
          "units": 0,
          "inventory": [
            {
              "symbol": "string",
              "name": "string",
              "description": "string",
              "units": 1
            }
          ]
        }
      }
    }
    """
    jsoned_data = json.loads(example)
    obj = ShipCargo(**jsoned_data["data"]["cargo"])

    result = api_client.fleet.cargo.jettison("test", "test", 1)

    assert obj == result


def test_fleet_jump(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "cooldown": {
          "shipSymbol": "string",
          "totalSeconds": 0,
          "remainingSeconds": 0,
          "expiration": "2019-08-24T14:15:22Z"
        },
        "nav": {
          "systemSymbol": "string",
          "waypointSymbol": "string",
          "route": {
            "destination": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departure": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departureTime": "2019-08-24T14:15:22Z",
            "arrival": "2019-08-24T14:15:22Z"
          },
          "status": "IN_TRANSIT",
          "flightMode": "CRUISE"
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, ShipJumpResult)

    result = api_client.fleet.jump("test", "test")

    assert obj == result


def test_fleet_navigate(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "fuel": {
          "current": 0,
          "capacity": 0,
          "consumed": {
            "amount": 0,
            "timestamp": "2019-08-24T14:15:22Z"
          }
        },
        "nav": {
          "systemSymbol": "string",
          "waypointSymbol": "string",
          "route": {
            "destination": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departure": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departureTime": "2019-08-24T14:15:22Z",
            "arrival": "2019-08-24T14:15:22Z"
          },
          "status": "IN_TRANSIT",
          "flightMode": "CRUISE"
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, ShipNavigateResult)

    result = api_client.fleet.navigate("test", "test")

    assert obj == result


def test_fleet_flight_mode(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "systemSymbol": "string",
        "waypointSymbol": "string",
        "route": {
          "destination": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "departure": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "departureTime": "2019-08-24T14:15:22Z",
          "arrival": "2019-08-24T14:15:22Z"
        },
        "status": "IN_TRANSIT",
        "flightMode": "CRUISE"
      }
    }
    """
    obj = serialize_json_to_obj(example, ShipNav)

    result = api_client.fleet.flight_mode("test", ShipNavFlightMode.drift)

    assert obj == result


def test_fleet_flight_nav(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "systemSymbol": "string",
        "waypointSymbol": "string",
        "route": {
          "destination": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "departure": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "departureTime": "2019-08-24T14:15:22Z",
          "arrival": "2019-08-24T14:15:22Z"
        },
        "status": "IN_TRANSIT",
        "flightMode": "CRUISE"
      }
    }
    """
    obj = serialize_json_to_obj(example, ShipNav)

    result = api_client.fleet.nav("test")

    assert obj == result


def test_fleet_warp(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "fuel": {
          "current": 0,
          "capacity": 0,
          "consumed": {
            "amount": 0,
            "timestamp": "2019-08-24T14:15:22Z"
          }
        },
        "nav": {
          "systemSymbol": "string",
          "waypointSymbol": "string",
          "route": {
            "destination": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departure": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departureTime": "2019-08-24T14:15:22Z",
            "arrival": "2019-08-24T14:15:22Z"
          },
          "status": "IN_TRANSIT",
          "flightMode": "CRUISE"
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, ShipNavigateResult)

    result = api_client.fleet.warp("test", "test")

    assert obj == result


def test_fleet_cargo_sell(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "agent": {
          "accountId": "string",
          "symbol": "string",
          "headquarters": "string",
          "credits": 0
        },
        "cargo": {
          "capacity": 0,
          "units": 0,
          "inventory": [
            {
              "symbol": "string",
              "name": "string",
              "description": "string",
              "units": 1
            }
          ]
        },
        "transaction": {
          "waypointSymbol": "string",
          "shipSymbol": "string",
          "tradeSymbol": "string",
          "type": "PURCHASE",
          "units": 1,
          "pricePerUnit": 1,
          "totalPrice": 1,
          "timestamp": "2019-08-24T14:15:22Z"
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, SellCargoResult)

    result = api_client.fleet.cargo.sell("test", "test", 0)

    assert obj == result


def test_fleet_scan_systems(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "cooldown": {
          "shipSymbol": "string",
          "totalSeconds": 0,
          "remainingSeconds": 0,
          "expiration": "2019-08-24T14:15:22Z"
        },
        "systems": [
          {
            "symbol": "string",
            "sectorSymbol": "string",
            "type": "NEUTRON_STAR",
            "x": 0,
            "y": 0,
            "distance": 0
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, ScanSystemsResult)

    result = api_client.fleet.scan.systems("test")

    assert obj == result


def test_fleet_scan_waypoints(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "cooldown": {
          "shipSymbol": "string",
          "totalSeconds": 0,
          "remainingSeconds": 0,
          "expiration": "2019-08-24T14:15:22Z"
        },
        "waypoints": [
          {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0,
            "orbitals": [
              {
                "symbol": "string"
              }
            ],
            "faction": {
              "symbol": "string"
            },
            "traits": [
              {
                "symbol": "UNCHARTED",
                "name": "string",
                "description": "string"
              }
            ],
            "chart": {
              "waypointSymbol": "string",
              "submittedBy": "string",
              "submittedOn": "2019-08-24T14:15:22Z"
            }
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, ScanWaypointsResult)

    result = api_client.fleet.scan.waypoints("test")

    assert obj == result


def test_fleet_scan_ships(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "cooldown": {
          "shipSymbol": "string",
          "totalSeconds": 0,
          "remainingSeconds": 0,
          "expiration": "2019-08-24T14:15:22Z"
        },
        "ships": [
          {
            "symbol": "string",
            "registration": {
              "name": "string",
              "factionSymbol": "string",
              "role": "FABRICATOR"
            },
            "nav": {
              "systemSymbol": "string",
              "waypointSymbol": "string",
              "route": {
                "destination": {
                  "symbol": "string",
                  "type": "PLANET",
                  "systemSymbol": "string",
                  "x": 0,
                  "y": 0
                },
                "departure": {
                  "symbol": "string",
                  "type": "PLANET",
                  "systemSymbol": "string",
                  "x": 0,
                  "y": 0
                },
                "departureTime": "2019-08-24T14:15:22Z",
                "arrival": "2019-08-24T14:15:22Z"
              },
              "status": "IN_TRANSIT",
              "flightMode": "CRUISE"
            },
            "frame": {
              "symbol": "string"
            },
            "reactor": {
              "symbol": "string"
            },
            "engine": {
              "symbol": "string"
            },
            "mounts": [
              {
                "symbol": "string"
              }
            ]
          }
        ]
      }
    }
    """
    obj = serialize_json_to_obj(example, ScanShipsResult)

    result = api_client.fleet.scan.ships("test")

    assert obj == result


def test_fleet_refuel(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "agent": {
          "accountId": "string",
          "symbol": "string",
          "headquarters": "string",
          "credits": 0
        },
        "fuel": {
          "current": 0,
          "capacity": 0,
          "consumed": {
            "amount": 0,
            "timestamp": "2019-08-24T14:15:22Z"
          }
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, RefuelShipResult)

    result = api_client.fleet.refuel("test")

    assert obj == result


def test_fleet_cargo_purchase(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "agent": {
          "accountId": "string",
          "symbol": "string",
          "headquarters": "string",
          "credits": 0
        },
        "cargo": {
          "capacity": 0,
          "units": 0,
          "inventory": [
            {
              "symbol": "string",
              "name": "string",
              "description": "string",
              "units": 1
            }
          ]
        },
        "transaction": {
          "waypointSymbol": "string",
          "shipSymbol": "string",
          "tradeSymbol": "string",
          "type": "PURCHASE",
          "units": 1,
          "pricePerUnit": 1,
          "totalPrice": 1,
          "timestamp": "2019-08-24T14:15:22Z"
        }
      }
    }
    """
    obj = serialize_json_to_obj(example, PurchaseCargoResult)

    result = api_client.fleet.cargo.purchase("test", "test", 1)

    assert obj == result


def test_fleet_cargo_transfer(api_client: AstroTradersClient):
    example = """
    {
      "data": {
        "cargo": {
          "capacity": 0,
          "units": 0,
          "inventory": [
            {
              "symbol": "string",
              "name": "string",
              "description": "string",
              "units": 1
            }
          ]
        }
      }
    }
    """
    jsoned_data = json.loads(example)
    obj = ShipCargo(**jsoned_data["data"]["cargo"])

    result = api_client.fleet.cargo.transfer("test", "test", TradeSymbol.fuel, 1)

    assert obj == result
